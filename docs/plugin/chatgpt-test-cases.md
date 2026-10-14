# ChatGPT test cases

These cases are prepared for an owner-run ChatGPT test. All are **NOT_RUN** in Phase 03 because no ChatGPT account/plugin was accessed. Do not change this status based on Codex discovery or package validation.

For each executed case, record the surface (ChatGPT Work web/Desktop/Mobile), date, plugin version, whether the plugin was selected, observed Skills, response, and any trace or UI evidence. A response that mentions a Skill name is not proof that the Skill file was loaded. If ChatGPT exposes no per-Skill trace, keep activation evidence limited to what is observable.

| Test | Prompt | Expected Skills | Status |
|---|---|---|---|
| 01 — Persian Mobile UI | «یک صفحه فروشگاهی فارسی برای موبایل دارم. طراحی و ساختار آن را از نظر خوانایی، فاصله‌ها و RTL بررسی کن.» | `persian-rtl-localization`, `interface-layout`, `responsive-design` | NOT_RUN |
| 02 — Form UX | «فرم ثبت‌نام من خطاهای نامفهوم دارد و کاربران در تکمیل آن مشکل دارند.» | `forms-input`, `accessibility-inclusive-design` | NOT_RUN |
| 03 — Design System | «می‌خواهم رنگ‌ها، کامپوننت‌ها و Design Tokens بین صفحات سایت یکپارچه شوند.» | `design-systems`, `color-systems` | NOT_RUN |
| 04 — Information Architecture | «کاربران محصولات را در دسته‌بندی‌های سایت پیدا نمی‌کنند.» | `information-architecture`, `navigation-controls` | NOT_RUN |
| 05 — Customer Journey | «می‌خواهم مسیر کاربر از ورود به صفحه محصول تا ثبت سفارش بررسی شود.» | `journey-mapping`, `ui-ux-review` | NOT_RUN |
| 06 — Negative Activation | «یک تابع Python برای مرتب‌سازی اعداد بنویس.» | No UI/UX Skill should be selected without a UI/UX need. | NOT_RUN |
| 07 — Explicit Invocation | In a fresh Work chat, select `UI/UX Pro` through `@` and ask: «ساختار یک صفحهٔ محصول فارسی را از نظر RTL و دسترسی‌پذیری بررسی کن.» | Explicit plugin selection; likely `persian-rtl-localization`, `ui-ux-review`, and/or `accessibility-inclusive-design` as needed. | NOT_RUN |

## Duplicate-source check

Phase 02 confirmed that Codex exposes both the 15 plugin-prefixed Skills and 15 legacy Skills when both sources are present. This result is not automatically carried over to ChatGPT. To check ChatGPT, inspect Personal Skills and the plugin's own Skills list, then run one implicit and one explicit case. Record whether the same title appears twice, whether the plugin card lists the installed Skills, and whether the model reports or exposes an actual source trace. Keep `DUPLICATE_SKILLS=NEEDS_REVIEW` if the UI/model does not establish precedence.
