# Use Case: The Wedding Day (Run-Sheet, Kibbudim Execution & Money Gifts)

## Overview
The wedding day itself is a tightly timed sequence of ceremonies and receptions involving both families, dozens of honorees, and all booked vendors simultaneously. The system's role on this day shifts from *planning* to *execution support*: a minute-by-minute run-sheet, day-of vendor verification checklists, honor (Kibbud) prompts, and the registration of money gifts received from guests.

Ceremony components and their order vary by community (e.g., *Badeken*, outdoor vs indoor Chuppah, *Mitzvah Tantz* in Hasidic communities) and are configured by the **Community Profile** ([community_customs_parametrization.md](./community_customs_parametrization.md)).

---

## User Scenario 1: The Day-Of Run-Sheet

*   **What the system does:** Generates a chronological run-sheet from the confirmed bookings and ceremony plan, for example:
    *   Vendor setup slots (hall, decor, sound check, catering buffet readiness — pulled from the AI contract checklists in [use_case_vendor_collaboration_and_contracts.md](./use_case_vendor_collaboration_and_contracts.md)).
    *   *Kabbalat Panim* (bride's reception) and *Chosson's Tisch* (groom's reception, with the Tna'im/Ketubah signing per custom) — running in parallel in separate areas.
    *   *Badeken* (veiling), procession order to the Chuppah, the Chuppah ceremony itself (with its Kibbudim sequence), *Yichud* room, first dance sets, meal courses, and *Sheva Brachot* after *Birkat HaMazon*.
    *   Each entry has a time, location within the venue, responsible person, and required items (ring, Ketubah, kittel, candles).
*   **Why:** On the day itself nobody has time to search chats and contracts; one printed/offline-available timeline keeps both families and vendors synchronized. The run-sheet must be available offline/printable (see [non_functional_requirements.md](./non_functional_requirements.md) §6).

## User Scenario 2: Kibbudim Execution

*   **What the system does:** Takes the honor assignments from the Kibbudim planner and operationalizes them on the day:
    *   Confirms attendance of each honoree (witnesses for the Ketubah and Kiddushin, blessing reciters, Chuppah holders where customary).
    *   Slots each Kibbud into the run-sheet with the exact moment and location.
    *   Provides the *Mesader Kiddushin* (officiating Rabbi) coordinator with the final honors list.
    *   Flags critical no-shows early (e.g., a Ketubah witness stuck in traffic) so a substitute can be assigned — witness eligibility rules are shown as a reminder (two adult male non-relatives).
*   **Why:** Double-assigned or forgotten honors cause real social damage; missing valid witnesses is a *halachic* show-stopper for the ceremony.

## User Scenario 3: Ritual Items Final Check

*   **What the system does:** Presents a morning-of checklist of the critical physical items and who carries each: the *Tabat Erusin* (ring, purchased with the groom's own funds), the *Shtar Ketubah* (verified Nusach), the kittel, candles, the plate/glass for breaking, and the couple's documents.
*   **Why:** These items are small, owned by different people, and irreplaceable on short notice.

## User Scenario 4: Money Gifts Registry (Cash, Checks, Transfers)

*   **What the system does:**
    *   Provides a **gift registration log** for the wedding evening (and the Sheva Brachot week): a designated trusted person records each envelope — giver (matched against the guest list), amount, and form (cash / check / bank transfer / app transfer).
    *   Supports quick entry (search guest by name, amount, method) and an "unidentified envelope" holding state for later matching.
    *   Produces totals by form of payment for safe handling and deposit tracking (e.g., checks to be deposited, cash counted and verified by two people).
    *   Feeds totals into the family **Ledger/Reconciliation** if the sides have agreed that gift income offsets shared costs — applying any such offset rule is a **decisive action** requiring dual-side approval ([roles_and_permissions.md](./roles_and_permissions.md)).
    *   Generates a thank-you tracking list (who gave, so the couple can acknowledge afterwards).
*   **Why:** Money gifts at Israeli weddings are substantial and arrive in hundreds of envelopes in one evening. Losing track causes both financial loss and social embarrassment (failing to thank a giver); linking gifts to the ledger closes the financial loop of the whole project.

## User Scenario 5: Vendor Day-Of Verification

*   **What the system does:** Surfaces each vendor's AI-extracted contract checklist (what/when they must deliver) as check-off lists assigned to responsible family members (e.g., an uncle verifies the buffet at 18:30).
*   **Why:** The couple and parents are occupied by the ceremony; delegated, simple checklists let helpers verify vendor performance without reading contracts.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Run-Sheet Generator** | Builds the minute-by-minute day timeline from bookings, ceremony plan, and Community Profile; printable/offline. | One source of truth during the highest-pressure day. |
| **Kibbudim Day-Of Tracker** | Confirms honorees, slots honors into the timeline, and manages substitutions. | Prevents social friction and halachic gaps (witnesses). |
| **Ritual Items Checklist** | Morning-of verification of ring, Ketubah, and ceremony items with named carriers. | These items are irreplaceable on the day. |
| **Money Gifts Registry** | Logs envelopes (giver, amount, form), totals by payment form, feeds the ledger, and builds the thank-you list. | Protects significant sums and preserves social obligations. |
| **Delegated Vendor Checklists** | Assigns contract-derived verification items to helpers. | Lets the family verify vendor delivery without legal reading. |
