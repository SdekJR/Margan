# Non-Functional Requirements

Cross-cutting requirements that apply to the whole Margan platform. They answer *what* qualities the system must have and *why* — not how they are implemented.

---

## 1. Languages & Localization

*   **Hebrew is the primary interface language.** Modern Hebrew is the everyday language of the majority of the Haredi public in Israel; all UI, templates (Azmana, Meurasim), and voice output must be Hebrew-first.
*   **Full right-to-left (RTL) support** is mandatory from day one (Hebrew and Yiddish are both RTL, Hebrew script).
*   **Additional languages, in priority order:** Yiddish (primary daily language in many Hasidic communities), English (large Anglo communities in Israel and the US/UK diaspora market), French, Spanish, Portuguese, Russian, and German (significant olim and diaspora communities), added incrementally after the Hebrew/Yiddish/English core.
*   **Hebrew calendar throughout:** all dates are displayed in both civil and Hebrew calendar formats; date pickers must be Hebrew-calendar aware.
*   Community-specific honorifics and phrasing in generated texts (invitations, announcements) follow the Community Profile ([community_customs_parametrization.md](./community_customs_parametrization.md)).

## 2. Shabbat & Holiday Mode

*   The system must **never send outbound communications (push, SMS, email, phone calls) during Shabbat or Jewish holidays**, computed for the recipient's location (default: Israel time zones, candle-lighting to havdalah with standard margins).
*   Scheduled reminders falling inside a prohibited window are automatically shifted to after Shabbat/holiday ends.
*   Deadline calculations must treat Shabbat and holidays as non-working days (e.g., a task "due Friday" must alert on Thursday).
*   **Why:** sending messages on Shabbat would be unacceptable to the entire target audience and would destroy trust in the product.

## 3. Privacy & Data Protection

*   The document vault stores **highly sensitive personal data**: Teudat Zehut scans, parents' Ketubot, Rabbinical status letters, divorce/death certificates. Requirements:
    *   Encryption at rest and in transit.
    *   Access restricted by default to the owning side's admins and the couple (admin-only audience level, per [roles_and_permissions.md](./roles_and_permissions.md)).
    *   Every document access is logged.
    *   **Retention & deletion:** the couple can export and permanently delete all wedding data after the process ends; a default retention prompt is offered after the Sheva Brachot stage.
*   Compliance with the **Israeli Privacy Protection Law**, including Amendment 13 (2024) obligations (data minimization, registration/notification duties, breach handling).
*   Financial data (budgets, ledgers, payments) of one side must never leak to viewers or to the other side when marked side-specific.
*   Vendor contacts see only their own booking's data — never guest lists, budgets, or other vendors' terms.

## 4. Security

*   Server-side enforcement of the permission matrix and the **dual-side approval rule** — clients can never bypass approvals.
*   Strong authentication for web/mobile; for the phone (IVR) channel, Caller ID alone authorizes **read-only** access, and a **PIN is mandatory for any state-changing operation** (see [use_case_kosher_phone_integration.md](./use_case_kosher_phone_integration.md)).
*   Full audit log of decisive actions (payments, approvals, admin grants).

## 5. Accessibility & Reach

*   The product must be usable by participants **without smartphones or email** (kosher phone users): every critical flow (RSVP confirmation, task status, expense logging) needs a phone-channel equivalent (IVR) or a human-mediated path (e.g., the Calling Campaign performed by family members).
*   Web app must work on low-end devices and modest bandwidth; core planning views should tolerate brief offline reading on mobile.

## 6. Reliability

*   The weeks around the wedding date are business-critical: degraded service on the wedding day itself (day-of checklists, contact details, run-sheet) must be mitigated by offline availability of the day-of materials (downloadable/printable versions).
*   All voice/IVR updates must synchronize to web/app in near real time so both families see one consistent state.
