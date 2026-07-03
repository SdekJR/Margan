# Use Case: Planning Engine — Plan Generation & Date Dependencies

## Overview
This use case defines *when* and *how much* the planning agent computes. The guiding principle:

> **The full plan is computed once, at wedding creation. The agent does not continuously recalculate timelines in the background.** Changes to key dates are handled through an explicit, user-triggered re-planning flow.

To make this possible, every task template is classified by its relationship to the key dates: some tasks **determine** a date, others merely **depend on** it, and others are date-independent.

---

## 1. Plan Generation at Wedding Creation

*   **What the system does:** When the couple creates the wedding, they provide the goal inputs: target timeframe (or fixed date), the two families' cities, the Community Profile, expected guest scale, and initial budget expectations. The engine then instantiates the complete roadmap in one pass:
    *   All stages (Vort → Sheva Brachot) with their joint and side-specific task sets from the community-specific templates.
    *   Deadlines for every task, computed from the anchor dates (see §2).
    *   Halachically valid date suggestions from the Hebrew calendar engine for any anchor not yet fixed.
*   **Why:** Computing everything up front gives the families a complete, stable picture they can trust and commit to. Silent background re-planning would erode confidence in deadlines and create confusion about "who moved my task."

## 2. Date Anchors & Task Classification

Every task template carries a classification:

| Class | Meaning | Examples |
| :--- | :--- | :--- |
| **Date-determining** | Its outcome fixes or constrains an anchor date. Until it completes, dependent deadlines are provisional. | Booking the wedding hall (fixes the wedding date); booking the Erusin hall (fixes the Erusin date); the bride's side confirming the Shabbat Sheva Brachot venue. |
| **Date-constrained (window)** | Must occur inside a fixed window relative to an anchor. | Opening the Rabbinate file: 90–21 days before the wedding (ideally 45+); final catering headcount: typically 3–7 days before; apartment search start: 1.5+ months before. |
| **Date-dependent (offset)** | Deadline derived as an offset from an anchor but flexible within reason. | Ordering invitations (after the hall is fixed); gown fittings; furniture delivery (2 weeks before). |
| **Date-independent** | No dependency on anchors. | Writing meeting letters; assembling the Jewish library; choosing gift items. |

**Anchor dates** are: Vort date, Erusin date, wedding date, and the derived dates (Shabbat Chatan, Sheva Brachot week, reciprocal Shabbat visits).

*   **What the system does:** Displays for each anchor which tasks determine it and which depend on it, so the families always know *what must be decided first* (e.g., "The wedding date is not final until the hall is booked — 34 deadlines are provisional").
*   **Why:** Making the dependency direction explicit prevents families from committing money to dependent bookings (band, invitations) before the determining decision (hall) is locked.

## 3. Explicit Re-Planning on Date Change

*   **What the system does:** If an anchor date changes (e.g., the hall offers a different date), an admin triggers the **Re-Planning flow**:
    1.  The engine computes a *preview* of all affected deadlines and window violations (e.g., "Rabbinate window at risk: only 19 days remain").
    2.  It lists every already-approved booking/payment affected by the change.
    3.  The change is a **decisive action**: it takes effect only after dual-side approval ([roles_and_permissions.md](./roles_and_permissions.md)).
    4.  On approval, deadlines are shifted in one atomic update and all admins are notified of the delta.
*   **Why:** A date change has financial and contractual consequences for both sides; it must be a deliberate, reviewed decision — never an automatic background adjustment.

## 4. What the Agent Does *Not* Do

*   No continuous background recalculation of the timeline.
*   No autonomous outbound communication: the AI may **draft** vendor messages, amendments, and announcements, but a human always reviews and sends/signs them.
*   No automatic modification of approved bookings, contracts, or payments — these always go through the dual-side approval flow.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **One-Pass Plan Generator** | Instantiates the full stage/task roadmap with deadlines at wedding creation, per Community Profile. | Gives families a complete, stable plan from day one. |
| **Anchor & Dependency Map** | Marks each task as date-determining, window-constrained, offset-dependent, or independent, and visualizes what blocks what. | Shows which decisions must be made first and which deadlines are provisional. |
| **Re-Planning Preview & Approval** | Simulates a date change, shows affected deadlines/bookings, and applies it only after dual-side approval. | Makes date changes deliberate and transparent instead of silent. |
| **Window Guard** | Warns when a fixed window (e.g., Rabbinate 90–21 days) is at risk given the current anchors. | Prevents legally or halachically blocking misses. |
