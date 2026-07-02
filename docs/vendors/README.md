# Margan - Wedding Vendors Directory

This directory contains individual profile cards (*kartis*) for all wedding vendors compiled from the database. The vendors are grouped by category:

| Category (Hebrew) | Category (English) | Vendor Count | Browse Link |
| :--- | :--- | :--- | :--- |
| קייטרינג | catering | 212 | [Browse catering](./catering/) |
| קוסמטיקה | cosmetics | 171 | [Browse cosmetics](./cosmetics/) |
| נדוניה | dowry | 1 | [Browse dowry](./dowry/) |
| שמלות ערב | evening_dresses | 148 | [Browse evening_dresses](./evening_dresses/) |
| עיצוב אירועים | event_design | 116 | [Browse event_design](./event_design/) |
| הפקת אירועים | event_production | 30 | [Browse event_production](./event_production/) |
| מקום לאירוע | event_venue | 374 | [Browse event_venue](./event_venue/) |
| חליפות חתן | grooms_suit | 88 | [Browse grooms_suit](./grooms_suit/) |
| כובעים לחתן | hats_groom | 20 | [Browse hats_groom](./hats_groom/) |
| הזמנות | invitations | 62 | [Browse invitations](./invitations/) |
| תכשיטים | jewelry | 144 | [Browse jewelry](./jewelry/) |
| איפור ועיצוב שיער | makeup_and_hair | 459 | [Browse makeup_and_hair](./makeup_and_hair/) |
| רישום נישואין | marriage | 20 | [Browse marriage](./marriage/) |
| מוהלים | mohels | 1 | [Browse mohels](./mohels/) |
| מוזיקה | music | 387 | [Browse music](./music/) |
| צילום | photo | 295 | [Browse photo](./photo/) |
| שמלות כלה | wedding_dresses | 111 | [Browse wedding_dresses](./wedding_dresses/) |
| פאות | wigs | 261 | [Browse wigs](./wigs/) |
| כובעי נשים | womens_hats | 1 | [Browse womens_hats](./womens_hats/) |

## How to Re-generate Cards
If the source database updates, run this script to rebuild the markdown vendor cards:
```bash
python scripts/generate_vendor_cards.py
```