# MVP Scope & Release Prioritization

This document defines what is included in the first release (MVP / v1) of Margan, what is deferred to later releases, and what remains long-term vision. It resolves the scope ambiguity of the six product pillars described in [product_concept.md](./product_concept.md).

---

## 1. V1 (MVP) — Core Planning Product

The MVP focuses on the features that are (a) unique differentiators versus competitors and (b) fully deterministic (no dependency on external APIs, telephony infrastructure, or payment networks).

| # | Feature | Source Use Case | Notes |
| :--- | :--- | :--- | :--- |
| 1 | **Stage-based planning roadmap** with Joint vs Side-Specific tasks, generated at wedding creation from templates and the community profile. | [use_case_haredi_wedding.md](./use_case_haredi_wedding.md), all stage use cases, [use_case_planning_engine_and_date_dependencies.md](./use_case_planning_engine_and_date_dependencies.md) | Plan is computed once at creation; re-planning is an explicit user action, not continuous background recalculation. |
| 2 | **Multi-party budget & financial reconciliation** (shared splits, side-specific costs, "who owes whom" ledger). | [use_case_haredi_wedding.md](./use_case_haredi_wedding.md) §3 | Highest-value deterministic feature; no competitor offers it. |
| 3 | **Roles & permissions with dual-side approval** for payments and agreed items. | [roles_and_permissions.md](./roles_and_permissions.md) | Foundation for all collaborative features; must be in v1. |
| 4 | **Halachic date validator** (Hebrew calendar engine filtering prohibited dates). | [use_case_haredi_wedding.md](./use_case_haredi_wedding.md) §1 | Technically simple, high perceived value. |
| 5 | **Gender-split guest list, RSVP tracking, and Calling Campaign distributor**. | [use_case_wedding_prep_stage.md](./use_case_wedding_prep_stage.md) §7 | Includes separate men/women headcounts and seating counts. |
| 6 | **Vendor directory (read-only)** from the pre-collected vendor database, filterable by category, city, and kosher certification. | [vendors_guide.md](./vendors_guide.md) | No vendor-side accounts in v1; organizers track contact/quote/booking status manually. |
| 7 | **Document vault** (uploads of IDs, certificates, Rabbinical letters) with restricted access. | [use_case_rabanut_registration.md](./use_case_rabanut_registration.md) | Subject to the privacy requirements in [non_functional_requirements.md](./non_functional_requirements.md). |
| 8 | **Money gifts registry** (cash/checks/transfers received at the wedding), feeding into the reconciliation ledger. | [use_case_wedding_day.md](./use_case_wedding_day.md) | Simple registry; no payment processing. |
| 9 | **Community customs parametrization** (stage templates configurable by community profile). | [community_customs_parametrization.md](./community_customs_parametrization.md) | Ship with the default custom set documented in the stage use cases; add profiles incrementally. |

**Platforms for v1:** Web (responsive) first; native iOS/Android wrappers follow once the web core is stable.

**Monetization in v1:** none — see [monetization.md](./monetization.md).

---

## 2. V2 — Vendor Collaboration & Kosher Phone Access

| # | Feature | Source Use Case | Notes |
| :--- | :--- | :--- | :--- |
| 1 | **Vendor accounts & shared workspace** (vendor calendars, vendor channels, scoped permissions). | [use_case_vendor_collaboration_and_contracts.md](./use_case_vendor_collaboration_and_contracts.md) | Turns the product into a two-sided platform; requires vendor onboarding effort. |
| 2 | **AI-proposed contract amendments** (Agreement Digest): the AI drafts the amendment automatically from chat discussions; it takes effect only after explicit sign-off by both parties. | Scenario D of the vendor collaboration use case | The AI proposes; humans sign. The contract is never modified without dual signature. |
| 3 | **AI contract checklist extraction** (upload contract → wedding-day duty checklist). | Scenario E of the vendor collaboration use case | |
| 4 | **Kosher phone IVR — DTMF-first** (keypad menus for status, task completion, expense logging), with mandatory PIN for state-changing operations. | [use_case_kosher_phone_integration.md](./use_case_kosher_phone_integration.md) | Hebrew voice output; conversational speech input deferred to v3. |
| 5 | **Multi-party chats** (couple chat, side chats, vendor channels). | Scenario C of the vendor collaboration use case | |

---

## 3. V3+ / Long-Term Vision

| Feature | Status & Rationale |
| :--- | :--- |
| **Conversational voice agent (Hebrew, later Yiddish)** | Deferred: Yiddish speech recognition quality is currently insufficient; start with Hebrew STT after the DTMF system proves demand. |
| **Digital escrow payments ("Stable-Shekel" smart contracts)** | Vision only. No widely adopted stable-shekel instrument exists today, the regulatory burden is high, and the target audience is conservative about digital money. V1/V2 record fiat payments (cash, transfer, check) only. |
| **Real-estate listing integration (Yad2)** | Dependent on a data partnership; Yad2 has no public API. Until then the apartment search module is a manual listing tracker (see [use_case_apartment_and_living_prep.md](./use_case_apartment_and_living_prep.md)). |
| **Rabbinate registry verification** | No public API exists; the Rabbinate registration module uses guided manual verification checklists (see [use_case_rabanut_registration.md](./use_case_rabanut_registration.md)). |
| **Monetization activation** | Options documented in [monetization.md](./monetization.md); decision deferred. |
