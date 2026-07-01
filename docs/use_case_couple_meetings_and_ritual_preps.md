# Use Case: Structured Couple Meetings & Ritual Preparations

## Overview
In the Haredi community, the period between the Erusin (betrothal) and the wedding is characterized by a very limited and highly structured number of meetings between the groom (*Chosson*) and the bride (*Kallah*). Each meeting is planned with specific locations, duration limits, and reciprocal gift exchanges accompanied by written letters.

Additionally, the groom must prepare key halachic ritual items for the wedding day—specifically the *Shtar Ketubah* (marriage contract) and the *Tabat Erusin* (betrothal ring)—which vary depending on the family's specific community customs (Ashkenazi, Sephardic, Hasidic).

---

## User Scenario 1: Planning Couple Meetings & Gift Exchange

### 1. Meeting Scheduler & Venue Planner
*   **What the system does:** 
    *   Helps the couple schedule their limited meetings (e.g., usually only 3 to 5 meetings during the entire engagement period).
    *   Maintains a catalog of recommended, culturally appropriate locations that afford privacy while adhering to modesty (*Tznius*) and seclusion (*Yichud*) laws (e.g., quiet hotel lobbies, specific garden parks, private family rooms).
    *   Allows the couple to set and track the duration of each meeting.
*   **Why:** Meetings are deliberately limited to maintain spiritual preparation and anticipation. Proper venue selection prevents social discomfort and halachic violations.

### 2. Meeting Gifts & Personal Letters (*Michtavim*)
*   **What the system does:** 
    *   Reminds both the groom and bride to prepare a gift for each scheduled meeting.
    *   Prompts them to write a personal letter (*Michtav*) to accompany the gift, tracking the completion of the letter.
*   **Why:** Exchanging gifts and letters at each meeting is a key custom to build connection and document their engagement journey.

---

## User Scenario 2: Pre-Wedding Gifts & Wedding Jewelry

### 1. Pre-Wedding Gift Checklist
*   **What the system does:** Tracks the groom's checklist for standard gifts that must be purchased and delivered to the bride before the wedding day (e.g., a jewelry box, watch, perfume, or specialized books).
*   **Why:** These gifts are culturally expected and represent the groom's commitment to building their future home.

### 2. Wedding Day Jewelry
*   **What the system does:** Tracks the selection and purchase of the specific jewelry items traditionally given to the bride on the wedding day (e.g., a gold bracelet or pearl necklace).
*   **Why:** Wedding day gifts are presented during specific moments of the celebration and must be prepared and kept safe in advance.

---

## User Scenario 3: Halachic Ritual Preparations (Groom's Side)

### 1. Shtar Ketubah Sourcing & Custom Verification
*   **What the system does:** 
    *   Guides the groom to source the physical *Shtar Ketubah* (marriage contract document).
    *   Prompts the groom to verify the exact text (*Nusach*) required based on their specific community customs (e.g., Ashkenazi, Sephardic, Hasidic text variations differ significantly regarding monetary values and obligations).
    *   Prompts the groom to review the document details with the officiating Rabbi (*Mesader Kiddushin*) before the wedding.
*   **Why:** An incorrect word or signature in the *Ketubah* can invalidate the marriage under Jewish law.

### 2. Betrothal Ring (*Tabat Erusin*) Kosher Check
*   **What the system does:** 
    *   Provides a checklist of halachic rules for purchasing the wedding ring:
        *   Must be made of plain metal (typically yellow gold) with **no gemstones, engravings, or cut-outs** on the inside or outside, to avoid any valuation ambiguity.
        *   Must be purchased entirely with the groom's own funds (not a gift or loan).
    *   Reminds the groom to have the officiating Rabbi inspect the ring prior to the *Chuppah*.
*   **Why:** The ring must meet strict halachic criteria to effect a legally binding betrothal under the canopy.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Meeting Coordinator** | Schedules the limited dates, sets durations, and provides a database of approved quiet locations. | Helps the couple coordinate within their community guidelines. |
| **Gift & Letter Tracker** | Generates tasks for buying meeting gifts and writing accompanying letters. | Ensures couples are prepared with reciprocal gifts and notes for every meeting. |
| **Nusach Ketubah Validator** | Asks questions about community origin and generates the correct *Ketubah* preparation checklist. | Avoids legal errors in the marriage contract text. |
| **Ring Halacha Checklist** | Walk the groom through purchasing a plain gold ring with his own funds. | Ensures the ring is halachically valid for the Kiddushin. |
