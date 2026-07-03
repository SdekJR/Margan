# Margan Product Concept

## Vision
**Margan** is an intelligent, agent-like assistant designed to guide individuals through highly complex, multi-stage life milestones. It goes beyond static checklists by acting as an active planning agent that automates coordination, dynamically manages budgets, matches users with contextual service providers, and automates administrative overhead.

The application is cross-platform, targeting **Web browsers**, **iOS**, and **Android** devices, providing a seamless experience for both event organizers (consumers) and service providers/vendors (contact persons) across desktop and mobile.

---

## Core Product Pillars

### 1. Goal-Driven Agent Planning
*   **What it does:** Instead of requiring users to construct a plan from scratch, the user defines a high-level goal (e.g., "Organize a wedding by date X"). The agent analyzes the goal, its context, and constraints (e.g., cultural, timeline, budget) to generate a fully populated, personalized step-by-step roadmap. It supports early-stage planning (milestones starting long before the main event) and categorizes activities into joint tasks and side-specific tasks.
*   **Why it's needed:** Complex milestones involve hundreds of interdependent tasks and early preparatory phases. A structured roadmap that spans the entire timeline and separates responsibilities keeps all parties aligned.

### 2. Intelligent Budget Management
*   **What it does:** Tracks expenses, projects total costs, and manages multi-party financial contributions. It allows splitting shared expenses under custom rules, assigning specific costs to individual parties (e.g., Groom's family vs. Bride's family), and calculates a financial reconciliation ledger showing who owes what to whom.
*   **Why it's needed:** Major events involve multiple funding parties and complex cost-sharing agreements. Transparency and automated ledger calculations prevent financial disputes and ensure smooth cost settlements.

### 3. Contextual Vendor Matchmaking & Search
*   **What it does:** Recommends and evaluates local businesses and vendors (e.g., venues, caterers, decorators) based on highly specific criteria, constraints, and requirements (e.g., specific kosher certifications, modesty accommodations, capacity).
*   **Why it's needed:** Finding specialized vendors manually is time-consuming. The agent pre-filters options that strictly align with the user's specific rules and preferences.

### 4. AI-Driven Reminders & Automation Agent
*   **What it does:** Acts as an active assistant: computes the full plan and all deadlines **once, at wedding creation** (classifying tasks by whether they determine, constrain, or depend on key dates), tracks deadlines, sends proactive reminders, and drafts vendor communications (e.g., inquiring about pricing or availability) for human review before sending. When a key date changes, timeline adjustments happen through an **explicit re-planning flow with preview and approval** — not continuous background recalculation. See the [Planning Engine & Date Dependencies Use Case](./use_case_planning_engine_and_date_dependencies.md).
*   **Why it's needed:** Complex events involve hundreds of interdependent deadlines. A plan computed up front, with deliberate and transparent re-planning, relieves administrative burden while keeping the families in control of every consequential change.

### 5. Kosher Phone Voice Interface (Voice Agent)
*   **What the system does:** Integrates an Interactive Voice Response (IVR) system powered by a voice AI agent. Users calling from registered phone numbers can query progress, mark tasks complete, and verbally log new budget items using natural language speech or telephone keypads (DTMF).
*   **Why it's needed:** A significant portion of the Haredi community uses non-smart "kosher phones" with no internet/app capabilities. A conversational telephone voice interface provides full system accessibility to all stakeholders.

### 6. Vendor Collaboration & Contracts
*   **What it does:** Facilitates end-to-end interactions between organizers and vendors who both use the Margan system. It provides dual-role calendars (organizer planning vs. vendor scheduling), specialized group and vendor chats, AI-drafted amendment proposals summarized from chat discussions (which enter the contract **only after both parties sign off**), AI-driven extraction of contract duties into simple checklists, and tracking of fiat payments (cash, bank transfer, check). Digital escrow payments ("Stable-Shekel" smart contracts) remain a long-term vision only — see [mvp_scope.md](./mvp_scope.md).
*   **Why it's needed:** Multi-vendor operations involve constant updates (e.g., changing menu options or adding decor). AI-drafted, dual-signed amendments keep agreements current without manual paperwork while preserving legal clarity.

---

## Initial Target Focus: Haredi Wedding Organization
To ground the agent's capabilities in a real-world scenario, the first implementation use case is the **Organization of a Haredi (Ultra-Orthodox Jewish) Wedding**. This domain is highly structured, operates under strict deadlines and religious constraints, and involves multiple stakeholders and highly specific vendor requirements, making it the perfect testbed for an intelligent agent.

---

## Cross-Cutting Specifications
*   [MVP Scope & Release Prioritization](./mvp_scope.md) — what ships in v1, v2, and what stays long-term vision.
*   [Roles & Permissions Model](./roles_and_permissions.md) — root admins (the couple), side admins, viewers, and the dual-side approval rule for payments and agreed items.
*   [Domain Glossary & Entity Model](./domain_glossary.md) — shared vocabulary for all specifications.
*   [Non-Functional Requirements](./non_functional_requirements.md) — languages/RTL, Shabbat mode, privacy of sensitive documents, security.
*   [Community Customs Parametrization](./community_customs_parametrization.md) — stage customs as configurable Community Profile parameters.
*   [Monetization Strategy](./monetization.md) — deferred; options recorded.
