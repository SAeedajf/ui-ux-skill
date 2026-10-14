"""Intentionally failing pre-agent checks for the isolated RTL fixture."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent

class Elements(HTMLParser):
    def __init__(self):
        super().__init__(); self.buttons=[]; self.labels=[]; self.attrs=[]; self.text=[]; self._button=None; self._label=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.attrs.append((tag,a))
        if tag=='button': self._button={'attrs':a,'text':''}; self.buttons.append(self._button)
        if tag=='label': self._label=a.get('for')
    def handle_endtag(self, tag):
        if tag=='button': self._button=None
        if tag=='label': self._label=None
    def handle_data(self, data):
        if self._button is not None: self._button['text'] += data.strip()

class FixtureBaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html=(ROOT/'index.html').read_text(); cls.css=(ROOT/'style.css').read_text(); cls.js=(ROOT/'app.js').read_text()
        cls.elements=Elements(); cls.elements.feed(cls.html)

    def test_product_buttons_have_accessible_names(self):
        carts=[b for b in self.elements.buttons if 'cart' in b['attrs'].get('class','')]
        self.assertEqual(3,len(carts))
        self.assertTrue(all(b['attrs'].get('aria-label') or b['text'] for b in carts))
        self.assertFalse(any(b['text']=='🛒' and not b['attrs'].get('aria-label') for b in carts))

    def test_form_field_has_associated_label_and_error_description(self):
        self.assertRegex(self.html,r'<label[^>]+for=["\']phone["\']')
        self.assertRegex(self.html,r'<input[^>]+aria-describedby=["\'][^"\']*error')
        self.assertIn("document.querySelector('#phone').focus()",self.js)

    def test_mobile_menu_exposes_state_and_restores_focus_on_escape(self):
        self.assertRegex(self.html,r'id=["\']menu-trigger["\'][^>]*aria-expanded=')
        self.assertRegex(self.js,r'addEventListener\(["\']keydown')
        self.assertRegex(self.js,r"trigger\.focus\(\)")

    def test_layout_adapts_without_fixed_width_overflow(self):
        self.assertNotRegex(self.css,r'\.page\s*\{[^}]*width:\s*720px')
        self.assertIn('@media',self.css)

    def test_error_text_contrast_meets_wcag_aa_normal_text(self):
        match=re.search(r'\.error\s*\{[^}]*color:\s*(#[0-9a-fA-F]{6})[^}]*background:\s*(#[0-9a-fA-F]{6})',self.css,re.S)
        self.assertIsNotNone(match)
        def luminance(h):
            values=[int(h[i:i+2],16)/255 for i in (1,3,5)]
            values=[v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in values]
            return .2126*values[0]+.7152*values[1]+.0722*values[2]
        fg,bg=map(luminance,match.groups())
        self.assertGreaterEqual((max(fg,bg)+.05)/(min(fg,bg)+.05),4.5)

if __name__=='__main__': unittest.main(verbosity=2)
