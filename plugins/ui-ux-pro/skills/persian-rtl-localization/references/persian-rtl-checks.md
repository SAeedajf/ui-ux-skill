# Persian and bidirectional interface checks

- Begin with **56–64** in the registry for Arabic/Persian layout requirements, bidirectional text, Persian typography, and Android text. Confirm the source's current scope before relying on a particular implementation detail.
- Use logical properties (start/end, inline/block) and Unicode bidirectional isolation for Latin identifiers embedded in Persian text. Test URLs, email, product codes, account numbers, and punctuation in context.
- Verify Persian glyph coverage, shaping, line height, font fallback, weight availability, and line wrapping with actual copy. Avoid presenting a specific font as universally required.
- Test Persian and Latin digits according to product/locale policy; check dates, currency, separators, phone numbers, OTP, and numeric keyboards.
- Before implementation, record the selected locale(s) and policy for each value. Do not assume Persian implies `fa-IR`, Jalali dates, toman, Persian digits, or an Iranian phone format.

| Value | Display policy | Accepted input | Stored/API form | Direction and verification |
|---|---|---|---|---|
| Numerals and decimals | Record locale-specific digit and separator choice | Test supported digit sets and separators | Record canonical representation | Test selection, copy/paste, parsing, and bidi punctuation |
| Dates and calendar | Record locale calendar and timezone | Record accepted entry/display formats | Record timezone and canonical form | Verify labels, ordering, and boundary dates |
| Currency | Record currency code and display convention | Accept only documented forms | Preserve currency and exact minor-unit policy | Test mixed-script amounts and separators |
| Phone and OTP | Record country/region and visible formatting | Test keypad, paste, autofill, and provider-supported characters | Preserve canonical number/code and never infer from display | Isolate LTR value; check caret, punctuation, and error text |
| URLs, email, IDs | Keep identifier syntax intact | Test realistic punctuation and case policy | Preserve canonical identifier rules | Isolate LTR runs and test cursor movement/copy/paste |

This is a policy capture table, not a locale default. Resolve each row with product, legal, and backend requirements before prescribing behavior.

For OTP or other fixed-format values, keep digit normalization separate from parsing and validation: normalize only the documented Persian, Arabic-Indic, or ASCII digits; preserve unsupported characters and excess digits until validation can reject the full value; and accept only product-approved separators. Do not apply a global non-digit-stripping rule to identity, phone, currency, or other inputs. Verify the rendered error and correction path in mixed RTL/LTR context.
- Mirror directional navigation only when the action is directional. Do not mirror logos, clocks, play/pause, or other direction-neutral semantics automatically.
- Confirm focus and reading order, error association, screen-reader pronunciation, zoom/text scaling, responsive layout, and both light/dark themes. Keep LTR locale behavior intact.
- For identity inputs, test actual value transitions (email → localized phone → code) in the same field. Record direction and alignment by value type, accepted numeral sets, and the locale's phone/prefix rules; keep the RTL form layout independent from an individual value's LTR reading order.
- Test punctuation at both edges of mixed RTL/LTR strings, cursor movement, selection, copy/paste, autofill, validation, and the actual numeric keyboard on the target platform.
- For localized error messages, use [S129](https://design-system.service.gov.uk/components/error-message/) only as a prompt to check field/service error distinction, association, and recovery. GOV.UK text and component markup are not Persian localization evidence; validate translated copy and bidi behavior in the target product.
