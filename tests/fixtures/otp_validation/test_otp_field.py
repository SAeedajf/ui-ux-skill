import unittest

from tests.fixtures.otp_validation.otp_field import LocalOtpField, normalize_digits, parse_otp


class OtpInputContractTests(unittest.TestCase):
    def test_normalizes_supported_digit_sets_without_dropping_content(self):
        self.assertEqual(normalize_digits("۴۸۲۷۳۱"), "482731")
        self.assertEqual(normalize_digits("٤٨٢٧٣١"), "482731")
        self.assertEqual(normalize_digits("482731x"), "482731x")
        self.assertEqual(normalize_digits("4827319"), "4827319")

    def test_accepts_six_digits_and_only_documented_ascii_separators(self):
        for value in ("482731", "۴۸۲۷۳۱", "٤٨٢٧٣١", "48 27-31"):
            with self.subTest(value=value):
                self.assertEqual(parse_otp(value), "482731")

    def test_rejects_short_long_and_unsupported_values(self):
        for value in ("48273", "4827319", "۴۸۲۷۳۱x", "48273100", "48273a", "", "4827/31", "-482731", "482731-", "48--2731"):
            with self.subTest(value=value):
                self.assertIsNone(parse_otp(value))

    def test_invalid_repeated_submit_does_not_count_as_a_valid_submission(self):
        field = LocalOtpField()
        field.paste("۴۸۲۷۳۱۹")
        self.assertFalse(field.submit())
        self.assertEqual(field.value, "4827319")
        self.assertFalse(field.submit())
        self.assertEqual(field.valid_submissions, 0)
        self.assertTrue(field.error)

    def test_corrected_value_clears_error_and_can_be_submitted(self):
        field = LocalOtpField()
        field.input("482731x")
        self.assertFalse(field.submit())
        field.input("۴۸۲۷۳۱")
        self.assertEqual(field.value, "482731")
        self.assertEqual(field.error, "")
        self.assertTrue(field.submit())
        self.assertEqual(field.valid_submissions, 1)

    def test_expired_value_is_cleared_with_a_recovery_message(self):
        field = LocalOtpField()
        field.input("482731")
        self.assertFalse(field.submit(expired=True))
        self.assertEqual(field.value, "")
        self.assertIn("expired", field.error)
        self.assertEqual(field.valid_submissions, 0)


if __name__ == "__main__":
    unittest.main()
