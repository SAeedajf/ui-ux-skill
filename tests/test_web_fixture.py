import unittest
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

    def test_loading_error_and_success_recovery_are_defined(self):
        self.assertIn('در حال ثبت…', self.js)
        self.assertIn('دوباره تلاش کن؛ ایمیلت پاک نشده است.', self.js)
        self.assertIn('عضویتت ثبت شد. ممنون!', self.js)
        self.assertIn("email.value.endsWith('.fail')", self.js)
        self.assertIn('email.focus()', self.js)


if __name__ == "__main__":
    unittest.main()
