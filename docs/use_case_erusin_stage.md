# Use Case: The Erusin (Formal Betrothal & Tna'im Celebration) Stage

## Overview
The **Erusin** (betrothal celebration, often referred to in modern Haredi circles as the *Tna'im* celebration) is a major event of approximately 200 guests. It is the formal ceremony where the *Shtar Tna'im* (betrothal contract) is signed and mothers traditionally break a plate.

According to traditional custom in this project:
*   The **Bride's side** is the primary organizer and takes full responsibility for the technical, financial, and logistical aspects of the event (venue, catering, music, photography, transportation).
*   The event is hosted in the **city where the bride's family resides**.
*   The **Groom's side** is responsible for arriving with their guests, inviting Yeshiva contacts, preparing the *Shtar Tna'im* document, bringing the plate to break, and presenting the bride with her engagement gift.

> **Note on customs and gifts:** Hosting responsibilities and the stage at which the engagement gifts are presented (Vort vs. Erusin) are Community Profile parameters — see [community_customs_parametrization.md](./community_customs_parametrization.md). The gift tasks listed below are the same single tasks referenced in the [Vort stage](./use_case_vort_stage.md), not duplicates.

---

## User Scenario: Organizing the Erusin

### 1. Venue & Catering (Bride's Side)
*   **What the system does:** Helps the Bride's family search for and book a banquet hall with separate rooms or a partitioning system (*Mechitza*) for 200 guests. It also tracks the catering order details.
*   **Why:** Erusin requires separate seating for men and women, and a hall that matches the community's standards and size.

### 2. Music & Sound System (Bride's Side)
*   **What the system does:** Prompts the booking of basic musical accompaniment (an organist/keyboardist, a DJ, or an MP3 playback system) and tracks the hire of a sound amplification system (speakers and amplifiers).
*   **Why:** Music is required to create a celebratory atmosphere, and sound amplification is essential for announcements and contract readings.

### 3. Photography (Bride's Side)
*   **What the system does:** Manages tasks to hire a photographer who is familiar with Haredi events.
*   **Why:** Families want high-quality photos of the signing of the *Tna'im*, the breaking of the plate, and family portraits.

### 4. Shuttle Transportation Coordinator (Bride's Side)
*   **What the system does:** Coordinates transportation logistics. If the hall is distant from the Groom's Yeshiva or the Bride's Seminary, the system tracks:
    *   Shuttle routes, pick-up points, and departure times.
    *   RSVPs specifically for the shuttle from students (friends of the bride and groom).
*   **Why:** Yeshiva and Seminary friends are key guests but often lack private transportation. Organizing group shuttles ensures high attendance and timely arrival.

### 5. Invitation (*Azmana*) Creator
*   **What the system does:** 
    *   Generates the invitation (*Azmana*) using a traditional community layout and text (*Nusach*).
    *   Formats the invitation for digital sharing (Email/SMS) and PDF generation for printing (to be hung on synagogue and Yeshiva bulletin boards).
*   **Why:** The wording of the invitation must follow strict religious and social protocols depending on the family's community subgroup.

### 6. Groom's Side Responsibilities
*   **What the system does:** Generates a specific checklist for the Groom's family:
    *   **Yeshiva Invitations:** Inviting Yeshiva friends, rabbis, and staff.
    *   **Groom's Gift:** Purchasing the traditional engagement jewelry (usually a gold watch or necklace) for the bride.
    *   **Ritual Items:** Preparing the physical *Shtar Tna'im* document and sourcing the ceramic plate to be broken.
    *   **Festive Clothing:** Purchasing new formal clothing for the groom's siblings and parents.
    *   **Travel Coordination:** Organizing family travel to the bride's city.

### 7. Bride's Side Preparations
*   **What the system does:** Generates a checklist for the Bride's family:
    *   **Bride's Gift:** Purchasing the engagement gift for the groom, traditionally a decorated and customized set of the Babylonian Talmud (*Shas*).
    *   **Festive Clothing:** Purchasing new formal clothing for the bride's siblings and parents.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Azmana Nusach Generator** | Provides traditional text templates for Orthodox invitations. | Ensures the invitations respect religious and social titles. |
| **Shuttle Logistics Planner** | Coordinates bus/shuttle capacities, timings, and routing for Yeshiva/Seminary friends. | Simplifies transport organization for large groups of young guests. |
| **Vendor Contract Tracker** | Tracks deposits, requirements, and statuses for the hall, sound system, and photographer. | Keeps the hosting family organized across multiple vendor categories. |
| **Ritual Items Safeguard** | Send reminders to the groom's side to bring the *Shtar Tna'im* contract and the plate. | Prevents critical ritual objects from being forgotten. |
