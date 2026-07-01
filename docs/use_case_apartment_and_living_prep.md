# Use Case: Apartment Sourcing & Married Life Essentials

## Overview
Preparing the new couple's home (*Bayit Ne'eman*) is a major milestone that must be finalized approximately **2 weeks before the wedding**. The search for a rented apartment begins **1.5 months or more prior**, depending on target geographical areas. 

Because apartments in Israel are commonly rented unfurnished, the couple must source, order, and assemble a complete household setup—including specialized furniture matching religious rules, double sets of kitchenware for kosher separation, and electrical appliances.

---

## User Scenario: Preparing the Home

### 1. Apartment Sourcing (Yad2 Integration)
*   **What the system does:** 
    *   Integrates with real estate search platforms (like *Yad2*) to aggregate apartment listings based on preferred geographical areas, budget, and religious neighborhood preferences.
    *   Saves and compares listings, tracking communication with landlords and lease negotiation stages.
*   **Why:** Sourcing an apartment manually across multiple cities is time-consuming. Having an aggregated, filterable dashboard of listings simplifies search logistics.

### 2. Wardrobe & Furniture Purchasing
*   **What the system does:** Generates a purchasing and delivery checklist for essential furniture:
    *   **Beds:** Two separate beds and mattresses (required to comply with the Jewish laws of family purity/*Niddah*).
    *   **Dining:** A dining table and chairs.
    *   **Storage:** A wardrobe/closet (*platyanoj shkaf*) for clothing.
    *   **Judaica:** A small bookcase (*Sifriah* / library cabinet).
*   **Why:** Ensuring that furniture is purchased, delivered, and assembled at least 2 weeks before the wedding avoids last-minute move-in chaos.

### 3. Electrical Appliances (White Goods)
*   **What the system does:** Generates checklists and tracks purchases for:
    *   *Core Appliances:* Refrigerator, washing machine, and a combined gas stove/oven.
    *   *Secondary Appliances:* Microwave, stand mixer, iron, and small kitchen electronics.
*   **Why:** These represent large capital expenses. Tracking orders and scheduling delivery windows ensures the apartment is fully functional before the couple moves in.

### 4. Household Textiles & Judaica Books
*   **What the system does:**
    *   Tracks the purchase of linens (bed sheets, pillows) and towels.
    *   Generates a checklist for a basic Jewish library (holy books like Torah, Siddur, Talmud, halachic guides) if the groom does not already own them.
*   **Why:** A Jewish home requires a baseline of spiritual and practical essentials.

### 5. Double Kosher Kitchenware Sets
*   **What the system does:** Generates a strict "Double Set" shopping list for kitchenware, enforcing separation between **Dairy (*Chalavi*)** and **Meat (*Basari*)** categories:
    *   *Cutlery:* Spoons, forks, knives (1 set for meat, 1 set for dairy).
    *   *Cookware:* Pots, pans, baking dishes (1 set for meat, 1 set for dairy).
    *   *Tableware:* Plates, bowls, glasses (1 set for meat, 1 set for dairy).
    *   *Color-Coding:* Allows the user to assign colors or labels (e.g., red for meat, blue for dairy) to easily track purchases and organize cabinets.
*   **Why:** Orthodox dietary laws (*Kashrut*) require complete separation of meat and dairy utensils. Sourcing these dual sets in advance prevents accidental mixing.

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Yad2 Listing Aggregator** | Pulls and filters apartment listings by price, location, and neighborhood. | Streamlines real estate search. |
| **Double-Set Kosher Kitchen Planner** | A dual checklist ensuring every kitchen utensil purchase has a matching dairy and meat counterpart. | Prevents mistakes in keeping a kosher kitchen setup. |
| **Delivery & Assembly Scheduler** | A calendar that overlays furniture and appliance delivery times with the couple's availability. | Coordinates multiple shipping arrivals to the new apartment. |
| **Married Life Trousseau Checklist** | Lists basic linens, towels, and baseline Jewish library books needed for the household. | Ensures all foundational home items are acquired before move-in. |
