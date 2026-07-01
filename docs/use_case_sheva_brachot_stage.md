# Use Case: Sheva Brachot & Shabbat Sheva Brachot Stage

## Overview
Following the wedding, the couple celebrates the **Sheva Brachot** (Seven Blessings) for seven consecutive days. Each evening, a festive meal is hosted where the wedding blessings are repeated in the presence of guests. 

Additionally, the Shabbat falling within these seven days (**Shabbat Sheva Brachot**) is a major logistical event. It is traditionally hosted by the **Bride's family** in their city of residence, requiring accommodation for the Groom's family and out-of-town guests who cannot travel on Shabbat.

---

## User Scenario: Planning the Sheva Brachot Week

### 1. 7-Day Evening Meal Scheduling
*   **What the system does:** Provides a master calendar for the 7 days post-wedding. It allows the coordinator to assign each evening's meal to a specific host (Bride's family, Groom's family, or external hosts like relatives or friends) and a specific venue.
*   **Why:** Coordinating seven separate events hosted by different people in different locations requires a single, shared source of truth to avoid scheduling conflicts.

### 2. Multi-Host Coordination & Budgets
*   **What the system does:** Allows external hosts (e.g., an uncle or community friend) to log in and manage their assigned evening's guest list and details, keeping their budget independent from the main wedding budget.
*   **Why:** Different people sponsor and pay for different evening meals, so financial tracking and RSVP management must be segmented.

### 3. Guest List Segmentation per Meal
*   **What the system does:** Manages independent guest lists for each of the 7 Sheva Brachot meals.
*   **Why:** Each evening meal is typically smaller and targeted to specific groups (e.g., one night for Yeshiva friends, another for close family, another for community neighbors).

### 4. Shabbat Sheva Brachot Venue & Menu Planning (Bride's Side)
*   **What the system does:** 
    *   Helps the Bride's family search for and book a local hall or rent a large venue (e.g., community center, synagogue hall, school room) if their family home is too small to host the Shabbat meals.
    *   Manages the menu and catering coordination for the multiple meals required over Shabbat (Friday night dinner, Saturday lunch, and the Third Meal / *Shalosh Seudot*).
*   **Why:** Shabbat hosting requires feeding dozens of guests over multiple large sittings, requiring precise logistical planning for space and food.

### 5. Shabbat Lodging & Accommodation Coordinator
*   **What the system does:** 
    *   Catalogs local lodging options (rented apartments, guest houses, hotel rooms, or volunteer host families) within walking distance of the meal venue.
    *   Assigns arriving guests—specifically the **Groom's family** and close out-of-town relatives—to these lodging spaces.
    *   Tracks lodging costs, check-in details, and payments.
*   **Why:** Since driving is forbidden on Shabbat, out-of-town guests and the groom's entire family must stay overnight in the bride's neighborhood. Sourcing and allocating close proximity housing is one of the biggest logistical hurdles of the wedding week.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **7-Day Master Scheduler** | Displays all 7 days with assigned hosts, venues, and status (e.g., "Planned," "Awaiting RSVPs"). | Provides the couple and families with a complete overview of the post-wedding week. |
| **Shabbat Lodging Allocator** | Maps out guest lodging capacities and matches them to specific arriving families, tracking walking distances. | Automates the complex process of housing the groom's family and guests nearby. |
| **Independent RSVP Dashboards** | Allows external hosts to manage RSVPs for their specific hosted meal. | Prevents main coordinators from being overwhelmed with guest management for minor dinners. |
| **Shabbat Meal & Hall Planner** | Tracks venue rental contracts and multi-meal menus for the Shabbat weekend. | Keeps the bride's family organized during a high-stress, multi-meal event. |
