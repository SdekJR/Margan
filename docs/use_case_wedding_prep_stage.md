# Use Case: Wedding Preparation Stage

## Overview
The **Wedding Preparation Stage** occurs 1 to 2 months before the wedding. It is a highly collaborative phase where both the Groom's and Bride's families coordinate major bookings, design choices, guest lists, and large-scale invitations. 

Unlike previous engagement stages, the wedding itself involves a very wide circle of guests (often 400 to 1,000+ people), requiring robust logistics and vendor coordination.

---

## User Scenario: Preparing for the Wedding

### 1. City & Venue Selection
*   **What the system does:** Helps both families align on a target city (balancing travel distances for both sides) and compare available wedding halls.
*   **Why:** Selecting a central or mutually agreed-upon city is the first step before any venue contract can be signed.

### 2. Catering & Menu Selection
*   **What the system does:** Manages tasks for choosing the caterer (verifying required *Kashrut* supervision), scheduling tastings, selecting the menu items, and tracking specific dishes.
*   **Why:** Food is a major part of the budget. Families need a way to review food options, align them with guest preferences, and track deadlines for final portion counts.

### 3. Music & Sound Setup (Package vs. Individual Bookings)
*   **What the system does:** Allows the coordinators to plan music in two ways:
    *   *All-Inclusive Package:* Booking a unified band, singer, and sound team.
    *   *Piecemeal Booking:* Individually hiring a sound technician (with amplifiers and speakers), the orchestra (*Tizmoret* / band), and a singer.
    *   *Chuppah Music:* Specifying whether a separate singer or specific instrumental music is required for the *Chuppah* ceremony.
*   **Why:** Music preferences and budgets vary. The system must accommodate both simple package deals and complex multi-vendor setups.

### 4. Photography, Videography & Guest Magnets
*   **What the system does:** Tracks the selection and booking of:
    *   A stills photographer (for portraits and event coverage).
    *   A videographer (for the wedding film).
    *   A magnet photography service (photographing guests during the event and printing physical magnets on the spot).
*   **Why:** Preserving memories is a high priority. Magnet photography is also a standard community favor for guests.

### 5. Hall Decoration & Luxury Styling
*   **What the system does:** Manages the optional booking of a wedding decor/styling firm to add elegance and luxury to the banquet hall's setup (e.g., customized table settings, centerpieces, specialized *Chuppah* design).
*   **Why:** Standard hall setups are often basic. Families who want a premium aesthetic need to coordinate external decorators.

### 6. Wedding Attire & Married Life Wardrobe
*   **What the system does:** 
    *   Generates separate, culturally specific shopping checklists for the couple:
        *   *Groom:* Suit, hat, shoes, frock coat (*frak*), dress shirts, and underwear/linens for married life.
        *   *Bride:* Wedding gown, trousseau (linens/underwear), wig (*sheitel*) and head coverings (*kisuyei rosh*).
    *   Allocates the tasks and budgets to the respective families (Groom's side vs. Bride's side) and tracks purchase deadlines.
*   **Why:** Acquiring a complete wardrobe and initial living linens is a structured, high-expense process in Haredi communities that must be completed weeks before the wedding.

### 7. Mass Invitations & RSVP Calling Campaigns
*   **What the system does:** 
    *   Manages the printing and distribution of invitations to a broad circle of relatives, friends, and community members.
    *   Runs a structured pre-wedding "Calling Campaign" where the system divides the list of unconfirmed guests among family members (e.g., bride's parents, groom's parents, couple) to make follow-up phone calls and record confirmations.
*   **Why:** Haredi weddings have huge guest lists. Ensuring an accurate final count requires actively calling guests who did not respond to initial invitations, which directly affects catering costs and table seating.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Vendor Configurator** | Compares all-in-one music/catering bundles vs. separate vendors (orchestra, singer, sound technician). | Helps families optimize costs and manage contracts. |
| **RSVP Calling Campaign Distributor** | Divides the unconfirmed guest list among family members for phone follow-ups and tracks results in a single database. | Streamlines the massive task of calling hundreds of guests to get final RSVPs. |
| **Menu & Dish Tracker** | Stores chosen menus, food restrictions, and counts. | Ensures accurate catering orders and prevents shortages. |
| **Visual Decor Coordinator** | Tracks decor concepts, vendor setup times, and design elements. | Keeps external designers and hall management aligned. |
| **Wardrobe & Trousseau Tracker** | Checklists and deadlines for purchasing personal clothing (suits, gowns, hats, wigs) and household linens. | Organizes personal shopping milestones and monitors spending across families. |
