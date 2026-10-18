"""Small local example of lossless OTP normalization and strict parsing.

This is an input-contract fixture only. It has no backend, secret, or verifier.
"""

import re

_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def normalize_digits(value: str) -> str:
    """Map supported numeral scripts while preserving every other character."""
    return str(value).translate(_DIGITS)


def parse_otp(value: str) -> str | None:
    """Accept six digits; ASCII spaces and hyphens are the only separators."""
    normalized = normalize_digits(value)
    if not re.fullmatch(r"\d+(?:[ -]\d+)*", normalized, flags=re.ASCII):
        return None
    digits = normalized.replace(" ", "").replace("-", "")
    return digits if len(digits) == 6 and digits.isascii() and digits.isdigit() else None


class LocalOtpField:
    """Model visible input/error recovery without contacting an auth service."""

    def __init__(self) -> None:
        self.value = ""
        self.error = ""
        self.valid_submissions = 0

    def input(self, value: str) -> None:
        self.value = normalize_digits(value)
        self.error = ""

    paste = input

    def submit(self, *, expired: bool = False) -> bool:
        parsed = parse_otp(self.value)
        if expired:
            self.value = ""
            self.error = "Code expired; request a fresh code."
            return False
        if parsed is None:
            self.error = "Enter exactly six digits."
            return False
        self.error = ""
        self.valid_submissions += 1
        return True
