# Use Case: Rabbinate Marriage Registration (Rishum Nisuin)

## Overview
To legally marry in Israel under religious law, the couple must open a marriage file (*Tik Nisuin*) with the Chief Rabbinate of Israel (*Rabanut*). This process is initiated immediately after the Erusin (betrothal) stage, between 90 and 21 days before the wedding (ideally 45+ days).

Once the wedding is completed, the officiating Rabbi returns the signed *Ketubah* to the Rabbinate, which then issues an official Marriage Certificate (*Teudat Nisuin*). This certificate is used to update the couple's marital status at the Ministry of Interior (*Misrad HaPnim*).

---

## User Scenario: Registering the Marriage

### 1. File Initialization (Tik Nisuin)
*   **What the system does:** 
    *   Reminds the couple to open the marriage file immediately after Erusin.
    *   Directs them to their local religious council (*Moatza Datit*) or Rabbinate office in Israel (which can be in any city, regardless of where they live).
    *   Collects and manages digitized uploads of necessary documents.
*   **Why:** Starting the process early ensures there is enough time to resolve any bureaucratic or halachic status queries.

### 2. Document Collection & Checklist
*   **What the system does:** Generates a personalized checklist of documents required by the Rabbinate:
    *   *Identification:* Israeli ID (*Teudat Zehut*) with its attachment (*Sefach*), or passports for tourists.
    *   *Passport Photos:* 3 identical photos for both the groom and bride.
    *   *Proof of Judaism:* Parents' marriage certificate (*Ketubah*). If the parents married abroad, the system guides them on how to request a validation from a regional Rabbinical Court.
    *   *Status Verification:* Sourcing a letter from a recognized Rabbi confirming the applicant is Jewish and single. Sourcing divorce/death certificates if applicable.
    *   *Wedding Venue Details:* Location (hall) and a copy of the hall's valid kosher certificate (*Teudat Kasrut*).
    *   *Officiating Rabbi:* Name of the Rabbi conducting the wedding (who must be pre-approved by the Chief Rabbinate).
*   **Why:** Missing documents can cause delays, preventing the wedding from being registered.

### 3. Witness Testimony Coordinator
*   **What the system does:** Prompts the couple to select two Jewish male witnesses (non-relatives) and provides instructions on when and where they must go to testify about the couple's single status.
*   **Why:** The Rabbinate legally requires independent witness testimonies to confirm that both parties are halachically eligible to marry.

### 4. Family Purity Course Verification
*   **What the system does:** Tracks the bride's progress in completing the mandatory family purity (*Taharat HaMinshpacha*) classes and stores the completion letter from her *Kallah* teacher.
*   **Why:** The Rabbinate will not issue the marriage certificate without proof that the bride has completed this instruction.

### 5. Final Ministry of Interior Update
*   **What the system does:** Once the marriage certificate is issued post-wedding, the system guides the couple on how to submit the document to the Ministry of Interior (*Misrad HaPnim*) to update their ID cards.
*   **Why:** Closes the administrative loop, legally registering them as married in the state database.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Document Vault & Status Tracker** | A central repository for uploading and verifying Teudat Zehuts, Ketubahs, and Rabbinical letters. | Keeps all legal and religious documents organized in one place. |
| **Officiating Rabbi & Venue Verifier** | Cross-checks the venue's kosher certificate and the Rabbi's license against the Rabbinate's authorized database. | Prevents booking unauthorized venues or officiants. |
| **Witness Coordination Manager** | Sends schedules and instructions to the selected witnesses. | Ensures witnesses arrive at the Rabbinate office on time. |
| **Post-Wedding Administrative Guide** | Step-by-step checklist for returning the Ketubah and updating Misrad HaPnim. | Ensures the marriage is registered with the state without delay. |
