# Margan Wedding Vendors Database Guide

The project includes a pre-downloaded database of wedding service providers located at `c:\Users\shimo\OneDrive\Projects\WeddingData\`. This directory contains `wedding_vendors.json` and a SQL database `wedding_vendors.db`, containing records categorized for Orthodox and general Jewish weddings.

---

## 1. Vendor Categories Summary

Based on the database structure, the service providers are sorted into the following categories:

| Category (Hebrew) | Category (English Slug) | Description & Custom Relevance |
| :--- | :--- | :--- |
| **מקום לאירוע** | `event_venue` | Wedding halls and banquet venues matching separate-seating standards. |
| **קייטרינג** | `catering` | Catering services with specific kosher (*Hechsher*) certifications. |
| **מוזיקה** | `music` | Orchestra (*Tizmoret*), singers, and sound technicians. |
| **צילום** | `photo` | Stills and video photographers, and guest magnet makers. |
| **עיצוב אירועים** | `event_design` | Design and decoration companies for banquet halls and Chuppahs. |
| **חליפות חתן** | `grooms_suit` | Formal suits and coats (*frak*) for the groom. |
| **כובעים לחתן** | `hats_groom` | Hats and headwear for the groom. |
| **שמלות כלה** | `wedding_dresses` | Modest (*Tznius*) wedding gown rental and design services. |
| **שמלות ערב** | `evening_dresses` | Festive evening gowns for the mothers and sisters of the couple. |
| **פאות** | `wigs` | Custom wig (*sheitel*) designers and retailers for the bride. |
| **כובעי נשים** | `womens_hats` | Head coverings (*kisuyei rosh*) and hats for the bride. |
| **נדוניה** | `dowry` | Bed linens, towels, and initial household textiles. |
| **תכשיטים** | `jewelry` | Rings (*Tabat Erusin*) and wedding jewelry for the bride. |
| **הזמנות** | `invitations` | Print and design shops for wedding invitations (*Azmana*). |
| **רישום נישואין** | `marriage` | Marriage registration guides and Rabbinical council contacts. |
| **גמ"חים** | `gemachim` | Community charity funds (*Gemach*) renting gowns, books, or ritual objects. |
| **מוהלים** | `mohels` | Ritual circumcision performers (for future milestones). |
| **הפקת אירועים** | `event_production` | Wedding planners and event production agencies. |
| **קוסמטיקה** | `cosmetics` | Cosmetics and styling salons. |

---

## 2. Generating Vendor Cards

To create individual markdown profiles (*kartis*) for all vendors in your workspace under `docs/vendors/`, you can run the automated generation script. 

### How to Run:
Open your local terminal and execute the following Python command from your workspace directory:
```bash
python scripts/generate_vendor_cards.py
```

### Result:
*   The script creates the folder `docs/vendors/` and generates subfolders for each category.
*   Each vendor is exported to their own card: `docs/vendors/<category_slug>/<business_name>_<post_id>.md`.
*   A master directory file `docs/vendors/README.md` is generated, linking to all categories and showing vendor counts.
*   Each card features a checklist to track contact, quote, and booking status for that vendor.
