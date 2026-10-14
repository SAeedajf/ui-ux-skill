import unittest
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "examples/fixtures/web-store"


class WebFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.css = (ROOT / "styles.css").read_text(encoding="utf-8")
        cls.js = (ROOT / "app.js").read_text(encoding="utf-8")

    def test_fixture_is_persian_rtl_and_has_product_sections(self):
        self.assertIn('<html lang="fa" dir="rtl">', self.html)
        self.assertIn('id="top"', self.html)
        self.assertIn('id="products"', self.html)
        self.assertEqual(self.html.count('class="product-card"'), 3)

    def test_product_actions_and_section_link_have_accurate_names(self):
        self.assertIn('<a href="#newsletter">خبرهای تازه</a>', self.html)
        self.assertNotIn('>دیدن همه</a>', self.html)
        names = re.findall(r'<button class="button add-button"[^>]*aria-label="([^"]+)"', self.html)
        self.assertEqual(len(names), 3)
        self.assertEqual(len(set(names)), 3)
        for product in ('آفتاب', 'خاک', 'زیتون'):
            self.assertTrue(any(product in name for name in names))

    def test_controls_expose_menu_cart_and_form_state(self):
        self.assertIn('aria-controls="primary-navigation"', self.html)
        self.assertIn('aria-expanded="false"', self.html)
        self.assertIn('aria-live="polite"', self.html)
        self.assertIn('autocomplete="email"', self.html)
        self.assertIn('aria-invalid="false"', self.html)
        self.assertIn('role="status"', self.html)
        self.assertIn("setAttribute('aria-invalid', 'true')", self.js)
        self.assertIn("setAttribute('aria-describedby', 'email-hint form-message')", self.js)

    def test_keyboard_focus_and_mobile_layout_are_present(self):
        self.assertIn(':focus-visible{outline:3px solid', self.css)
        self.assertNotIn(':focus{outline:none}', self.css)
        self.assertIn('@media(max-width:760px)', self.css)
        self.assertIn("window.matchMedia('(max-width: 760px)')", self.js)

    def test_escape_closes_mobile_navigation_and_returns_focus(self):
        self.assertIn("event.key !== 'Escape'", self.js)
        self.assertIn("navigation.classList.remove('open')", self.js)
        self.assertIn("menuButton.setAttribute('aria-expanded', 'false')", self.js)
        self.assertIn('menuButton.focus()', self.js)

    def test_loading_error_and_success_recovery_are_defined(self):
        self.assertIn('در حال ثبت…', self.js)
        self.assertIn('در حال ثبت عضویت…', self.js)
        self.assertIn('دوباره تلاش کن؛ ایمیلت پاک نشده است.', self.js)
        self.assertIn('✓ عضویتت ثبت شد. ممنون!', self.js)
        self.assertIn("email.value.endsWith('.fail')", self.js)
        self.assertIn('email.focus()', self.js)
        self.assertIn("message.dataset.state = 'error'", self.js)
        self.assertIn("message.dataset.state = 'pending'", self.js)
        self.assertIn("message.dataset.state = 'success'", self.js)
        self.assertIn('#form-message[data-state="success"]', self.css)
        self.assertIn('#form-message[data-state="error"]', self.css)

    def test_feedback_state_text_colors_meet_normal_text_contrast(self):
        def token(name):
            match = re.search(rf"{name}:(#[0-9a-fA-F]{{6}})", self.css)
            self.assertIsNotNone(match, f"missing color token {name}")
            return match.group(1)

        def luminance(hex_color):
            channels = [int(hex_color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
            linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in channels]
            return sum(channel * weight for channel, weight in zip(linear, (0.2126, 0.7152, 0.0722)))

        for foreground, background in (("--error", "--error-bg"), ("--success", "--success-bg")):
            values = sorted((luminance(token(foreground)), luminance(token(background))), reverse=True)
            contrast = (values[0] + 0.05) / (values[1] + 0.05)
            self.assertGreaterEqual(contrast, 4.5, f"{foreground} on {background} is below 4.5:1")


if __name__ == "__main__":
    unittest.main()
