# Private ChatGPT acceptance cases

All cases are currently `NOT_RUN`. Plugin Creator metadata confirms that the private user-scoped plugin exists; this does not prove installation, discovery, invocation, or Skill execution. Follow [the existing-plugin owner procedure](chatgpt-personal-plugin.md). Keep each test in a fresh conversation and never infer activation from answer text alone.

| Test | Setup and prompt | Expected observation | Status |
|---|---|---|---|
| T01 — Explicit invocation | Select the existing `UI/UX Pro` plugin in a fresh Work chat. Ask: «ساختار یک صفحهٔ محصول فارسی را از نظر RTL و دسترسی‌پذیری بررسی کن.» | Explicit selection is visible; relevant UI/UX guidance is applied. Record any Skill trace. This tests explicit invocation, not automatic activation. | NOT_RUN |
| T02 — RTL / responsive positive | In a new chat, leave the plugin unselected. Ask: «یک فروشگاه فارسی روی موبایل دارم؛ ریسپانسیو بودن، ترتیب RTL، متن‌های ترکیبی و اسکرول افقی را از روی کد بررسی کن.» | Evidence-based review of viewport behavior, RTL, mixed-direction content, and known limitations. Only mark Skill activation PASS if a trace identifies the loaded packaged Skill. | NOT_RUN |
| T03 — Forms | «فرم ثبت‌نام فارسی در خطای شماره تلفن پیام مبهمی نشان می‌دهد. اعتبارسنجی، ارتباط خطا با فیلد، نگه‌داشتن مقدار و مدیریت Focus را بررسی کن.» | Concrete form states, error recovery, and focus checks with accessible names/associations. | NOT_RUN |
| T04 — Accessibility | «این صفحه را از نظر نام کنترل‌ها، کنتراست و پیمایش کامل با کیبورد بررسی کن؛ هر چیزی را که از شواهد نمی‌شود تأیید کرد جدا بگو.» | Findings tied to inspected controls and measured contrast; no blanket conformance claim. | NOT_RUN |
| T05 — Design system | «توکن‌های رنگ، فاصله و تایپوگرافی این رابط با کامپوننت‌هایش ناهماهنگ است. موارد واقعی را پیدا کن و یک اصلاح کوچک و سازگار پیشنهاد بده.» | Identifies actual tokens/components and a scoped consistent change; preserves working patterns. | NOT_RUN |
| T06 — Information architecture | «کاربران دسته‌بندی محصولات را پیدا نمی‌کنند. ساختار فعلی و مسیرهای ناوبری را بررسی کن و تغییر پیشنهادی را با شواهد توضیح بده.» | Assessment of labels, grouping, wayfinding, and relevant user task evidence. | NOT_RUN |
| T07 — Negative control | In a fresh chat with the plugin unselected, ask: «یک تابع Python برای مرتب‌سازی لیست اعداد بنویس.» | No UI/UX Skill should be selected or loaded unless the user adds a UI/UX need. A useful Python answer is expected. | NOT_RUN |

## Per-test evidence record

```text
Test ID:
Date/time and timezone:
ChatGPT surface and account/workspace scope:
Plugin ID / version:
Installed state:
Discovered in picker:
Explicitly selected (yes/no):
Prompt (exact):
Observed Skills / trace paths:
Response or visible error:
Screenshot, trace, or evidence location:
Result: PASS / FAIL / BLOCKED / NOT_RUN / NEEDS_REVIEW
Limitations:
```

## Duplicate Skills check

Compare the plugin's installed Skill inventory with any legacy/personal Skills. Record IDs, namespace/path, and count for each source. If ChatGPT only shows a plugin card or a response without a source trace, discovery may be confirmed but precedence, selection, and activation stay `NEEDS_REVIEW`. Codex's 15 + 15 duplicate discovery result does not establish ChatGPT behavior.
