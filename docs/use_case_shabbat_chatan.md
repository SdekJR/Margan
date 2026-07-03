# Use Case: Shabbat Chatan (Aufruf) Stage

## Overview
The **Shabbat Chatan** is the festive Shabbat centered on the groom, when he is called up to the Torah (*Aliyah*) in the synagogue and the community celebrates with him. In the Ashkenazi custom (the default in this project) it is held on the **Shabbat before the wedding** (*Aufruf*); in most Sephardic communities the celebratory Shabbat Chatan takes place on the **Shabbat after the wedding**. The timing is therefore a **Community Profile parameter** (see [community_customs_parametrization.md](./community_customs_parametrization.md)).

The **Groom's side** is the organizer and host, in the groom's community.

---

## User Scenario: Organizing the Shabbat Chatan

### 1. Synagogue Coordination
*   **What the system does:** Tracks coordination with the groom's synagogue: confirming the date with the Rabbi and *Gabbai*, reserving the groom's *Aliyah*, and scheduling any additional honors (e.g., *Maftir*, extra Aliyot for fathers and brothers — linked to the Kibbudim planner).
*   **Why:** The Aliyah slot and honors must be arranged with the synagogue in advance; forgetting the Gabbai coordination is a common and embarrassing failure.

### 2. Kiddush & Festive Meals
*   **What the system does:** Manages the plan for the post-services *Kiddush* (sponsored refreshments for the whole congregation) and the festive Shabbat meals for invited guests (Friday night dinner, Shabbat lunch, *Shalosh Seudot*): venue (home vs rented hall), catering order or home-cooking checklist, and headcounts per meal.
*   **Why:** Feeding both the congregation (Kiddush) and personal guests (meals) requires separate headcounts and orders.

### 3. Guest Invitations & Lodging
*   **What the system does:** Manages the Shabbat Chatan guest list (family, Yeshiva friends, Rabbis), tracks RSVPs per meal, and — for out-of-town guests, including the bride's family where customary — allocates walking-distance lodging using the same lodging tracker as the Reciprocal Shabbat visits.
*   **Why:** Guests cannot travel on Shabbat; every confirmed out-of-town guest needs a bed within walking distance.

### 4. Candy Bags (*Pekelach*) & Traditional Items
*   **What the system does:** Generates a shopping checklist for the traditional items: candy bags thrown at the groom after the Aliyah (*pekelach*), refreshments, and any community-specific extras (e.g., a *tish* on Friday night in Hasidic communities — a Community Profile parameter).
*   **Why:** These small customary items are easily forgotten in the pre-wedding rush.

### 5. Pre-Wedding Week Checklist (Adjacent Tasks)
*   **What the system does:** Bundles the same-week reminders adjacent to the Shabbat Chatan: final headcount confirmations to the caterer, final gown/suit pickups, wedding-day logistics confirmation with all vendors, and the bride's side's parallel pre-wedding events.
*   **Why:** The last week concentrates many small deadlines; grouping them under one view reduces the risk of misses.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Synagogue & Honors Coordinator** | Tracks Rabbi/Gabbai confirmations and Aliyah/honor assignments (linked to Kibbudim). | Ensures the ritual core of the Shabbat is arranged in time. |
| **Multi-Meal Headcount Planner** | Separate headcounts and orders for Kiddush and each Shabbat meal. | Prevents food shortages across distinct sittings. |
| **Shabbat Lodging Tracker (reused)** | Allocates out-of-town guests to walking-distance lodging. | Same constraint as all Shabbat events: no travel on Shabbat. |
| **Custom Timing Parameter** | Schedules the Shabbat Chatan before or after the wedding per Community Profile. | Ashkenazi and Sephardic customs differ fundamentally. |
