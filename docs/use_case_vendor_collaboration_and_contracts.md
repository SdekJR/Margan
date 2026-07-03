# Use Case: Vendor Collaboration, Shared Calendars, and Smart Contracts

## Overview
Wedding planning involves intense, dynamic coordination between the organizing families (Groom's family, Bride's family, and the couple) and multiple external service providers (e.g., catering agencies, decorators, photographers, waiters, music bands). 

**Margan** provides a collaborative ecosystem where both organizers and vendors interact. Through web browsers or native mobile app installations, parties can synchronize their calendars, maintain structured communication channels, log agreed modifications, keep service agreements up to date through signed amendments, and track payments (fiat currency; digital escrow is a long-term vision — see [mvp_scope.md](./mvp_scope.md)).

---

## User Scenarios

### Scenario A: Multi-Platform Onboarding & Role Assignment
1. **Accessing the System:** 
   - The organizing couple (Groom and Bride) and their relatives download the Margan app on their mobile devices or log in via a web browser.
   - The primary contact person for a booked service provider (e.g., the catering manager, lead photographer, or decorator) is sent an invitation link. They can open it directly in a web browser or install the app on their phone.
2. **Role Mapping:** The system establishes the correct permissions:
   - *Organizers:* Access the full wedding roadmap, budget split ledger, and vendor directory.
   - *Vendor Contacts:* Access only the files, chats, calendar entries, and contracts related to their specific service category and client.

### Scenario B: Dual Calendar Management
1. **Organizer's Planning Calendar:** 
   - The Groom, Bride, and their families use a calendar that tracks planning milestones, family meetings, menu tasting dates, wardrobe fittings, and payment deadlines.
2. **Vendor's Schedule Calendar:**
   - The vendor contact person manages a separate calendar inside their view. It shows their business availability, scheduled preparation times, setup deadlines (e.g., when the decorator needs to start setting up the *Chuppah*), and active client bookings.
3. **Synchronized Bookings:** When the organizers finalize a booking with a vendor, the event automatically populates the vendor's calendar as a booked slot, showing client contact details, event date, and location.

### Scenario C: Collaborative Multi-Party Chats
1. **Private Couple Chat:** A dedicated channel for the Groom (*Chosson*) and Bride (*Kallah*) to discuss private preparations, gifts, and personal matters.
2. **Side-Specific Family Chats:** 
   - *Groom's Side Chat:* Includes the Groom and his relatives/parents to coordinate responsibilities assigned to their family (e.g., organizing the Vort, buying the bride's jewelry).
   - *Bride's Side Chat:* Includes the Bride and her relatives/parents to coordinate bride-specific logistics (e.g., booking the wedding dress, the trousseau shopping).
3. **Vendor Channels:** Separate channels are created for each hired service provider (e.g., "Margan Chat: Caterer", "Margan Chat: Waiter Service", "Margan Chat: Decorator").

### Scenario D: Chat-Based Contract Updates & Document Generation
1. **Discussing Adjustments:** The Bride chat-messages the waiter coordinator, requesting to add custom bar decorations and extra high-quality glassware. Similarly, she chats with the catering manager to replace one of the main course salads.
2. **Summarizing Chat Iterations:** The system's AI assistant tracks the conversation. At the end of a detailed discussion or upon request, it **automatically drafts** a structured **Agreement Digest** (amendment proposal) summarizing:
   - What changes were discussed (e.g., "Add custom tableware for 150 guests, replace Caesar salad with Mediterranean salad").
   - The estimated budget adjustments.
3. **Dual Signature & Contract Update:** The Agreement Digest is only a *proposal*. Nothing enters the final **Service Agreement / Contract** until it is explicitly signed off by **both** parties: the organizers (a decisive action requiring dual-side approval per [roles_and_permissions.md](./roles_and_permissions.md)) and the vendor contact. Only after both signatures does the system append the amendment to the contract and adjust the active budget ledger. The contract is never modified automatically without these signatures.

### Scenario E: AI-Generated Vendor Checklist (Contract Digest)
1. **Uploading the Contract:** The organizers upload the service contract received from the vendor (or capture it via mobile camera).
2. **AI Analysis:** The system analyzes the contract to extract a simplified checklist of the vendor's responsibilities:
   - *What* they must deliver (e.g., "300 portions of salmon starter, 3 decorated main buffet tables").
   - *When* they must deliver it (e.g., "Buffet setup complete by 18:30, starters served at 19:30").
   - *Operational Rules:* How to handle adjustments or verify execution (e.g., "Portion buffer of 10% on standby").
3. **Actionable Checklist:** The organizers receive a concise, chronological list of duties to check off on the day of the wedding or during vendor setup.

### Scenario F: Dual-Mode Payment Settlement
1. **Selecting Payment Type:** Organizers navigate to the payment section of the specific vendor contract. Recording or editing any payment is a decisive action requiring dual-side approval ([roles_and_permissions.md](./roles_and_permissions.md)).
2. **Current Scope — Fiat Currency:** The user records payments made via traditional cash, bank transfers, or checks. The budget updates accordingly.
3. **Long-Term Vision (out of scope for v1/v2) — Digital Escrow ("Stable-Shekel" Smart Contract):**
   - A possible future option in which both parties lock the agreed amount in a digital escrow released on predefined milestones (e.g., 20% on contract signature, 60% on arrival at the venue, 20% after successful event completion).
   - Deferred because no widely adopted stable-shekel instrument exists today, the regulatory burden is high, and the target audience is conservative about digital money. See [mvp_scope.md](./mvp_scope.md).

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Multi-Platform Access** | Runs as a mobile app (iOS/Android) or a web browser application for organizers and vendors. | Ensures all parties can access the platform from any device, even if the vendor does not want to install a native app. |
| **Dual Calendar Synchronization** | Separates organizer task calendars from vendor-specific scheduling calendars while syncing finalized booking times. | Prevents scheduling overlaps and ensures vendors know their setup and delivery times for each wedding. |
| **Specialized Communication Channels** | Hosts private couple chats, side-specific family chats, and direct vendor channels. | Keeps discussions organized and prevents vendors from seeing private family planning debates. |
| **Agreement Digest Generator** | Summarizes chat discussions into structured PDF/Markdown agreements capturing updates and notes. | Generates a clean audit trail of changes discussed during the planning phase. |
| **AI-Proposed Contract Amendments** | Automatically drafts amendment proposals from chat-negotiated changes; appends them to the contract only after explicit sign-off by both the organizers (dual-side approval) and the vendor. | Eliminates manual paperwork drafting while ensuring the contract only ever changes with both parties' signatures. |
| **AI Contract Digest Extractor** | Parses uploaded contracts to generate a simplified task checklist for the wedding day. | Saves the couple from reading lengthy legal documents on the wedding day to verify if the vendor is doing their job. |
| **Payment Tracker (Fiat)** | Records cash, bank transfer, and check payments against contracts, with dual-side approval. Digital escrow ("Stable-Shekel") remains a long-term vision only. | Covers how the target audience actually pays today; keeps the escrow option open without committing to it. |
