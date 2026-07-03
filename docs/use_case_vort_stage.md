# Use Case: The Vort (Engagement Celebration) Stage

## Overview
The **Vort** (Yiddish: *ווארט* - word/agreement) is the first formal event held immediately after the couple decides to finalize the matchmaking process (*Shidduch* completion) and get married. It represents the public announcement of the engagement.

According to traditional custom in this project, the **Groom's side** is the primary organizer and host of the Vort, which is usually held at the groom's home or in a small community synagogue (*shtiebel*). The guest list is restricted to a tight circle of close family and friends from both sides.

---

## User Scenario: Organizing the Vort

### 1. Venue & Scheduling
*   **What the system does:** Helps the Groom's family select a venue (Groom's home or a local synagogue room) and schedule the date.
*   **Why:** Ensures the event occurs quickly after the decision to marry, aligning with the community's expectation of a prompt celebration.

### 2. Guest List & Automated Invitations
*   **What the system does:** 
    *   Allows the Groom's family and Bride's family to import/add contacts and mark them as "Close Family" or "Close Friends."
    *   Drafts and sends automated invitations via the channels each guest actually has (Email or SMS where available). For kosher-phone guests without SMS/email — a large share of the audience — the system generates a **personal calling list** with the invitation text to read out, split among family members (same mechanism as the RSVP Calling Campaign in [use_case_wedding_prep_stage.md](./use_case_wedding_prep_stage.md)).
    *   Tracks RSVPs in real time, updating the guest headcount.
*   **Why:** The Vort is organized very rapidly. Families need a quick way to invite a small, specific circle of guests and track responses, including guests reachable only by voice call.

### 3. Shopping List & Refreshments Manager
*   **What the system does:** Generates a pre-populated shopping list for light refreshments, pastries, and drinks typical for a Vort, allowing the host to adjust quantities based on the confirmed guest count.
*   **Why:** The host family needs to quickly purchase food and beverages without overlooking essential items.

### 4. Specialized Purchases & Gift Tracking
*   **What the system does:** Creates and tracks tasks for mandatory cultural purchases and gifts:
    *   **Groom's Gift:** The specific engagement gift the groom presents to the bride (e.g., a watch or jewelry).
    *   **Bride's Gift:** The engagement gift the bride/her family presents to the groom (e.g., a set of Shas/Talmud books).
    *   **Vort Decorations:** Traditional decorations for the home or synagogue hall.
    *   **Meurasim Poster:** An engagement poster/sign displayed at the entrance of the event.
*   **Why:** These specific purchases are socially and culturally required, and tracking who is responsible for buying and bringing them prevents last-minute stress.
*   **Note:** The engagement gifts (jewelry for the bride, Shas for the groom) also appear in the [Erusin stage](./use_case_erusin_stage.md). Each gift is a **single task** with purchase and presentation sub-steps; whether it is presented at the Vort or at the Erusin is a Community Profile parameter (see [community_customs_parametrization.md](./community_customs_parametrization.md)) — the system must not create duplicate gift tasks across the two stages.

### 5. Newspaper Announcement ("Meurasim")
*   **What the system does:** 
    *   Provides templates to draft the traditional engagement announcement (*Meurasim*) in the specific community style (matching standard wording used in Orthodox newspapers like *Hamodia*, *Yated Ne'eman*, etc.).
    *   Guides the user on sending/scheduling the announcement in the chosen publications.
*   **Why:** Publicly announcing the engagement in community newspapers is a key milestone. Providing standard formatting ensures the announcement complies with cultural expectations and contains correct spelling and honorary titles.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Targeted RSVP Tracker** | Sends reminders to unconfirmed guests and calculates final headcount. | Host needs accurate numbers for catering and space capacity in small venues. |
| **Vort Checklist Template** | Provides a checklist split by responsibility (Groom's family hosts, Bride's family brings specific gifts). | Clarifies expectations between the two families from day one. |
| **Meurasim Drafter** | Generates standard textual formats for Orthodox newspaper engagement notices. | Prevents formatting mistakes and ensures appropriate community phrasing. |
