# Persian and bidirectional interface checks

- Begin with **56–64** in the registry for Arabic/Persian layout requirements, bidirectional text, Persian typography, and Android text. Confirm the source's current scope before relying on a particular implementation detail.
- Use logical properties (start/end, inline/block) and Unicode bidirectional isolation for Latin identifiers embedded in Persian text. Test URLs, email, product codes, account numbers, and punctuation in context.
- Verify Persian glyph coverage, shaping, line height, font fallback, weight availability, and line wrapping with actual copy. Avoid presenting a specific font as universally required.
- Test Persian and Latin digits according to product/locale policy; check dates, currency, separators, phone numbers, OTP, and numeric keyboards.
- Mirror directional navigation only when the action is directional. Do not mirror logos, clocks, play/pause, or other direction-neutral semantics automatically.
- Confirm focus and reading order, error association, screen-reader pronunciation, zoom/text scaling, responsive layout, and both light/dark themes. Keep LTR locale behavior intact.
