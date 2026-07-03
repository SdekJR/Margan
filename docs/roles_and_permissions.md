# Roles & Permissions Model

This document defines who can see and change what inside a wedding workspace. It is a cross-cutting specification: every feature (tasks, budget, guests, contracts, documents) must respect this model.

---

## 1. Roles

### 1.1 Root Admins — the Couple
*   The **Groom** and the **Bride** are the two Root Admins, created automatically when the wedding is created. They cannot be removed or downgraded.
*   Only the Groom and the Bride, **acting together**, can grant admin rights to any other person: every admin grant requires an explicit confirmation from *both* the Groom and the Bride.

### 1.2 Side Admins — the Parents (default) and Optional Relatives
*   Admins are always assigned to exactly one side: **Groom's Side Admin** or **Bride's Side Admin**.
*   The four parents — Groom's father, Groom's mother, Bride's father, Bride's mother — are the standard Side Admins. They are proposed automatically during onboarding and activated through the same dual confirmation by the couple.
*   Additional relatives (siblings, uncles, grandparents, etc.) are **optional** admins. Each one is added individually and requires confirmation by both the Groom and the Bride.

### 1.3 Viewers — Everyone Else
*   Any other invited participant (siblings not granted admin rights, extended family, helpers) is a **Viewer**: read-only access, no editing rights.

### 1.4 Vendor Contacts
*   Vendor contact persons are external users scoped to their own service: they see only the chats, calendar entries, files, and contract items of their booking (see [use_case_vendor_collaboration_and_contracts.md](./use_case_vendor_collaboration_and_contracts.md)). They are never admins or viewers of the wedding workspace itself.

---

## 2. Admin Capabilities & the Dual-Side Approval Rule

### 2.1 Regular Actions (single-admin)
An admin may freely **add, edit, and remove** items within their visibility scope: tasks, guests, shopping items, notes, draft budget entries, etc.

### 2.2 Decisive Actions (dual-side approval required)
Any action that touches **money** or modifies an item that has already been **agreed by both sides** requires the approval of **one admin from the Groom's side AND one admin from the Bride's side**. This includes:

*   Recording, editing, or deleting a payment.
*   Approving a vendor booking, contract, or contract amendment.
*   Changing the agreed amount, terms, or scope of an already-approved item.
*   Cancelling or replacing an already-approved vendor or booking (e.g., a caterer both sides agreed on and paid a deposit for: changing the sum, switching the caterer, or removing the booking — each requires fresh dual-side approval).
*   Changing budget split rules between the sides.

**Example flow:** a Bride's Side Admin proposes replacing the agreed caterer → the system marks the item "Pending approval" → any Groom's Side Admin approves or rejects → only on approval does the change take effect and the budget ledger update.

The proposing side's approval is counted implicitly; the system must always obtain the *other* side's confirmation before applying the change. The enforcement is server-side and every decisive action is recorded in an audit log (who proposed, who approved, when).

---

## 3. Visibility Levels

Every item has two independent visibility dimensions:

### 3.1 Audience Level
*   **Admin-only:** visible only to admins (e.g., budget negotiations, vendor quotes, sensitive documents).
*   **All participants:** visible to admins and viewers (e.g., the event schedule, public checklists, shuttle times).

### 3.2 Side Scope (from the task model)
*   **Joint:** visible to both sides.
*   **Side-specific:** visible only to the owning side (e.g., the bridal gown budget is visible only to Bride's side admins/viewers).

### 3.3 Resulting Matrix

| | Groom's Side Admin | Bride's Side Admin | Groom's Side Viewer | Bride's Side Viewer |
| :--- | :--- | :--- | :--- | :--- |
| Joint, all-participants | edit | edit | view | view |
| Joint, admin-only | edit | edit | — | — |
| Groom-side, all-participants | edit | — | view | — |
| Groom-side, admin-only | edit | — | — | — |
| Bride-side, all-participants | — | edit | — | view |
| Bride-side, admin-only | — | edit | — | — |

The Groom and Bride (Root Admins) each belong to their own side for side-scoped items, but both can always see **joint** items and manage workspace-level settings (participants, admin grants).

*Special case:* documents in the document vault default to **admin-only** within the owning side, per [non_functional_requirements.md](./non_functional_requirements.md).

---

## 4. Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Dual Couple Confirmation for Admin Grants** | Admin rights activate only after both the Groom and the Bride confirm the specific person. | Keeps control of the workspace in the couple's hands and prevents unilateral admin appointments. |
| **Dual-Side Approval Engine** | Blocks decisive actions (payments, changes to agreed items) until an admin from each side approves; tracks pending approvals. | Prevents unilateral financial decisions and inter-family disputes. |
| **Visibility Enforcement** | Applies the audience level × side scope matrix to every item server-side. | Protects each side's private logistics and sensitive admin data. |
| **Audit Log** | Records every decisive action with proposer, approver, and timestamp. | Provides a trusted history for resolving disagreements. |
