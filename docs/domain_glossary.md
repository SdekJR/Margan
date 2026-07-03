# Domain Glossary & Entity Model

A shared vocabulary for all Margan specifications. Every use case document should use these terms consistently. Relations are described in plain language (what/why), not as a database schema.

---

## 1. Workspace & People

| Entity | Definition | Key Relations |
| :--- | :--- | :--- |
| **Wedding** | The central workspace ("wedding file") covering the full journey from Shidduch finalization to the end of the Sheva Brachot week. | Has exactly two Sides, one Community Profile, one Wedding Date (plus dates of sub-events), many Stages, Tasks, Budget Items, Guests, Bookings. |
| **Side** | One of the two family parties: **Groom's Side** or **Bride's Side**. | Owns side-specific Tasks, Budget Items, Guests, and its own admin group. |
| **Participant** | A person with access to the Wedding: the couple, relatives, helpers. | Has exactly one Role and belongs to one Side. |
| **Role** | Access level of a Participant: **Root Admin** (Groom, Bride), **Side Admin**, or **Viewer**. See [roles_and_permissions.md](./roles_and_permissions.md). | Determines edit rights and visibility. |
| **Vendor Contact** | External user representing a booked Vendor; scoped to their own Booking only. | Linked to one Vendor and one or more Bookings. |
| **Community Profile** | The wedding's cultural configuration (e.g., Hasidic, Litvish/Yeshivish, Sephardic, plus sub-community options). See [community_customs_parametrization.md](./community_customs_parametrization.md). | Selects stage templates, hosting customs, Nusach texts, and default task sets. |

## 2. Planning

| Entity | Definition | Key Relations |
| :--- | :--- | :--- |
| **Stage** | A chronological phase of the roadmap (Vort, Erusin, Reciprocal Shabbats, Prep Period, Shabbat Chatan, Wedding Day, Sheva Brachot week…). | Contains Tasks and Events; ordered on the timeline. |
| **Event** | A concrete dated happening inside a stage: the Vort gathering, the Erusin celebration, a couple meeting, a Shabbat visit, the Chuppah, each Sheva Brachot meal. | Has a date/venue; Guests RSVP to Events; Bookings serve Events. |
| **Task** | A unit of work with an owner side (**Joint** or **Side-Specific**), a due date, a status, and an audience level (admin-only / all participants). | Belongs to a Stage; may be **date-determining** (see below); may reference a Booking, Budget Item, or Gift. |
| **Date-Determining Task** | A task whose outcome fixes or constrains a key date (e.g., booking the hall fixes the wedding date; the Rabbinate file must open 90–21 days before). See [use_case_planning_engine_and_date_dependencies.md](./use_case_planning_engine_and_date_dependencies.md). | Anchors other tasks' deadlines. |
| **Checklist Template** | A reusable pre-populated set of tasks/items for a stage or purpose (Vort refreshments, double kosher kitchenware, Rabbinate documents), instantiated according to the Community Profile. | Generates Tasks at wedding creation. |
| **Kibbud** | A ceremonial honor (witnessing the Ketubah, reciting a blessing) assigned to a specific guest. | Assigned to a Guest; scheduled within an Event. |

## 3. Money

| Entity | Definition | Key Relations |
| :--- | :--- | :--- |
| **Budget Item** | A planned or actual expense. Allocation is **Shared** (split by percentage or fixed amounts) or **Side-Specific**. | Belongs to a category and optionally a Booking; accumulates Payments. |
| **Payment** | A recorded money transfer (cash, bank transfer, check) against a Budget Item or Booking. Recording/editing a payment is a **decisive action** requiring dual-side approval. | Made by a Side (or the couple); feeds the Ledger. |
| **Ledger / Reconciliation** | The real-time computed balance of who paid what versus their agreed share, with the final "who owes whom" settlement. | Derived from Budget Items and Payments. |
| **Money Gift** | Cash, check, or transfer received from a guest at the wedding (or Sheva Brachot). See [use_case_wedding_day.md](./use_case_wedding_day.md). | Linked to a Guest; feeds the Ledger and thank-you tracking. |

## 4. Guests & Hospitality

| Entity | Definition | Key Relations |
| :--- | :--- | :--- |
| **Guest** | An invited person with gender (for separate seating), side (groom's / bride's / joint community), relation group, and contact channels. | RSVPs per Event; may receive a Kibbud, a seat assignment, a Lodging Assignment, or shuttle slot. |
| **RSVP** | A guest's attendance status for a specific Event, obtainable digitally or via the Calling Campaign. | One per Guest per Event. |
| **Lodging Assignment** | Allocation of an out-of-town guest (or the visiting bride/groom) to a nearby sleeping place for a Shabbat event. | Links a Guest to a lodging option; tracks cost and walking distance. |
| **Gift** | A customary physical gift obligation (engagement jewelry, Shas, meeting gifts, host-family gifts) with a giver side, recipient, and stage. | Backed by a Task; stage attribution may depend on the Community Profile. |

## 5. Vendors & Agreements

| Entity | Definition | Key Relations |
| :--- | :--- | :--- |
| **Vendor** | A service provider from the directory (venue, caterer, band, photographer…), with category, city, and kosher certification attributes. | Sourced from the vendor database; has Vendor Contacts. |
| **Booking** | An engagement of a Vendor for a specific Event (date, venue, price). Approving a booking is a decisive action. | Links Vendor ↔ Event; owns a Contract and Payments. |
| **Contract** | The stored service agreement for a Booking. | Modified only via signed Amendments. |
| **Amendment (Agreement Digest)** | A structured change proposal to a Contract — drafted automatically by the AI from chat discussions — that takes effect only after both the organizers and the vendor sign off. | Belongs to a Contract; updates the Budget Item on approval. |
| **Contract Checklist** | The AI-extracted list of vendor duties (what/when) used for day-of verification. | Derived from a Contract. |

## 6. Documents & Communication

| Entity | Definition | Key Relations |
| :--- | :--- | :--- |
| **Document** | A file in the vault (Teudat Zehut scans, Ketubah, Rabbinical letters, kosher certificates). Sensitive by default — see [non_functional_requirements.md](./non_functional_requirements.md). | Owned by a Side or the couple; referenced by Tasks (e.g., Rabbinate checklist). |
| **Channel** | A scoped chat: private couple chat, side-specific family chat, or vendor channel. | Membership derives from Roles and Bookings. |
| **Notification** | An outbound reminder or update (push, email, SMS, phone call), subject to Shabbat/holiday suppression rules. | Targets Participants or Guests via their available channels. |
