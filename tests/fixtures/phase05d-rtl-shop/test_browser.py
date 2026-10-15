"""Behavioral Chromium checks for the isolated Phase 05-D fixture.

Install Playwright and its test browser in a temporary environment, then run:
  python3 -m unittest discover -s tests/fixtures/phase05d-rtl-shop -p 'test_browser.py' -v
"""
from pathlib import Path
import unittest

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
URL = ROOT.joinpath("index.html").as_uri()


class PhoneFormBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.context = type(self).browser.new_context(viewport={"width": 1280, "height": 900})
        self.page = self.context.new_page()
        self.external_requests = []
        self.page.on("request", lambda request: self.external_requests.append(request.url) if request.url.startswith(("http://", "https://")) else None)
        self.page.goto(URL)

    def tearDown(self):
        self.context.close()

    def submit(self):
        self.page.locator("#contact button[type=submit]").click()

    def test_empty_and_invalid_values_show_associated_errors_and_focus(self):
        for value in ("", "12345"):
            self.page.locator("#phone").fill(value)
            self.submit()
            self.assertEqual("true", self.page.locator("#phone").get_attribute("aria-invalid"))
            self.assertIn("error", self.page.locator("#phone").get_attribute("aria-describedby"))
            self.assertTrue(self.page.locator("#error").inner_text())
            self.assertEqual("phone", self.page.evaluate("document.activeElement.id"))
            self.assertFalse(self.page.locator("#status").inner_text())

    def test_valid_number_succeeds_without_network_submission(self):
        self.page.locator("#phone").fill("09123456789")
        self.submit()
        self.assertEqual("false", self.page.locator("#phone").get_attribute("aria-invalid"))
        self.assertFalse(self.page.locator("#error").inner_text())
        self.assertIn("در این آزمون معتبر است", self.page.locator("#status").inner_text())
        self.assertEqual([], self.external_requests)

    def test_recovery_clears_previous_error_and_retains_corrected_value(self):
        self.page.locator("#phone").fill("123")
        self.submit()
        self.page.locator("#phone").fill("09123456789")
        self.submit()
        self.assertEqual("09123456789", self.page.locator("#phone").input_value())
        self.assertEqual("false", self.page.locator("#phone").get_attribute("aria-invalid"))
        self.assertFalse(self.page.locator("#error").inner_text())
        self.assertIn("در این آزمون معتبر است", self.page.locator("#status").inner_text())

    def test_duplicate_valid_submission_is_idempotent(self):
        self.page.locator("#phone").fill("09123456789")
        self.submit()
        first_status = self.page.locator("#status").inner_text()
        self.submit()
        self.assertEqual(first_status, self.page.locator("#status").inner_text())
        self.assertEqual([], self.external_requests)

    def test_accessible_name_error_association_and_live_region(self):
        self.assertEqual("phone", self.page.get_by_label("شماره تماس").get_attribute("id"))
        self.assertIn("error", self.page.locator("#phone").get_attribute("aria-describedby"))
        self.assertEqual("alert", self.page.locator("#error").get_attribute("role"))
        self.assertEqual("polite", self.page.locator("#status").get_attribute("aria-live"))

    def test_requested_viewports_report_actual_width_rtl_and_no_overflow(self):
        for requested in (320, 390, 768, 1280):
            self.page.set_viewport_size({"width": requested, "height": 900})
            self.page.reload()
            actual = self.page.evaluate("window.innerWidth")
            direction = self.page.evaluate("getComputedStyle(document.documentElement).direction")
            overflow = self.page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
            columns = self.page.locator("#products").evaluate("el => getComputedStyle(el).gridTemplateColumns.split(' ').length")
            self.assertEqual(requested, actual, f"requested={requested}, actual={actual}")
            self.assertEqual("rtl", direction)
            self.assertFalse(overflow, f"horizontal overflow at {actual}px")
            self.assertEqual(1 if requested < 640 else 2 if requested < 960 else 3, columns)

    def test_mobile_menu_escape_closes_and_restores_focus(self):
        trigger = self.page.locator("#menu-trigger")
        trigger.click()
        self.assertEqual("true", trigger.get_attribute("aria-expanded"))
        self.page.locator("#mobile-menu a").focus()
        self.page.keyboard.press("Escape")
        self.assertEqual("false", trigger.get_attribute("aria-expanded"))
        self.assertEqual("menu-trigger", self.page.evaluate("document.activeElement.id"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
