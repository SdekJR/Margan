# Use Case: Kosher Phone Voice Integration (IVR & Voice Agent)

## Overview
In Haredi communities, a significant portion of the population uses "kosher phones"—approved mobile devices that are strictly limited to voice calls, having no web browsers, apps, or SMS capabilities. 

To ensure complete accessibility, **Margan** provides a voice-based interface. Users can dial a dedicated phone number from a pre-registered line to interact with the AI planning agent using natural language speech or telephone keypad commands (*DTMF*).

---

## User Scenarios

### Scenario A: Authentication & Progress Inquiry
1.  **Call & Automated Greeting:** A user (e.g., the Groom's father) dials the Margan system number. The system recognizes the caller's phone number (*Caller ID / CLI*) and maps it to the active wedding file.
    *   *Voice Output:* *"Shalom, Moshe. Regarding the wedding of Chaim and Leah, planning is 68% complete. You have 4 pending tasks for this week."*
2.  **Voice Query:** The user asks: *"What is left to do for the Shabbat Chatan?"*
3.  **Status Report:** The AI agent processes the speech, queries the database, and reads back the pending tasks.
    *   *Voice Output:* *"For Shabbat Chatan, you still need to: one, confirm the caterer count, and two, allocate lodging for the groom's brothers. Would you like to update any of these?"*

### Scenario B: Verbal Task Completion
1.  **Instruction:** The user says: *"Yes, mark the lodging task as completed."*
2.  **Action & Confirmation:** The system updates the task status in the database and confirms verbally.
    *   *Voice Output:* *"Lodging for siblings has been marked as completed. You have 3 tasks remaining for this week."*

### Scenario C: Logging a Forgotten Budget Expense
1.  **Instruction:** The user says: *"I want to add a new expense. I paid 600 shekels in cash for the Vort drinks."*
2.  **Action & Categorization:** The AI agent:
    *   Creates a new budget item of 600 ILS.
    *   Categorizes it under "Vort - Refreshments".
    *   Allocates the cost to the Groom's side (since the user is the Groom's father).
    *   *Voice Output:* *"Recorded 600 shekels for Vort refreshments, paid by the Groom's side. Your updated family budget balance is 12,400 shekels."*

---

## Key Functional Requirements

### 1. Two-Level Phone Authentication (CLI + Mandatory PIN for Changes)
*   **What the system does:** Maps inbound phone numbers to specific user accounts, roles (Groom's family vs. Bride's family), and wedding IDs. Access is tiered:
    *   *Read-only access* (querying progress, hearing checklists): granted by recognized Caller ID alone. Unrecognized numbers require a PIN even for read access.
    *   *State-changing operations* (marking tasks complete, adding budget items, any data modification): **always require the user's personal PIN**, even from a recognized number.
*   **Why:** Caller ID can be spoofed and household phones are shared. Requiring a PIN for every modification prevents unauthorized changes while keeping simple status queries frictionless.

### 2. Conversational Speech-to-Text (STT) & Text-to-Speech (TTS)
*   **What the system does:** Transcribes the user's spoken Hebrew or Yiddish, extracts planning-related intents (query status, complete task, add expense), and reads back responses using clear synthesized speech.
*   **Why:** Allows natural, hands-free interaction for users who do not have screens.

### 3. Keypad (DTMF) Interface — First Delivery Phase
*   **What the system does:** Provides a structured menu system using the phone keypad (e.g., *"Press 1 for task updates, press 2 to log an expense, press 3 for budget totals"*).
*   **Why:** Works in noisy environments and when speech recognition fails.
*   **Rollout note:** The DTMF menu system (with Hebrew voice prompts) is the **first phase** of the phone channel (see [mvp_scope.md](./mvp_scope.md)). The conversational speech interface (§2) follows once Hebrew STT quality is validated; Yiddish speech recognition is a later addition, as current STT quality for Yiddish is insufficient.

### 4. Real-Time Web & App Synchronization
*   **What the system does:** Instantly synchronizes any updates made via voice call (e.g., marking a task as done or adding a budget item) so they appear immediately on the web and smartphone apps used by other family members.
*   **Why:** Keeps both families aligned, regardless of whether they access the system via smart app or kosher phone.
