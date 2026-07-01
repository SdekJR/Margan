import os
import json
import re
import sys

# Ensure UTF-8 output
if sys.stdout:
    sys.stdout.reconfigure(encoding='utf-8')

CATEGORIES_DIR = r"c:\Users\shimo\OneDrive\Projects\WeddingData\categories"
VENDORS_OUT_DIR = r"c:\Users\shimo\OneDrive\Projects\Margan\docs\vendors"

# Category mapping from compile_data.py
CATEGORY_MAPPING = {
    "מקום לאירוע": "event_venue",
    "צילום": "photo",
    "מוזיקה": "music",
    "קייטרינג": "catering",
    "איפור ועיצוב שיער": "makeup_and_hair",
    "שמלות כלה": "wedding_dresses",
    "שמלות ערב": "evening_dresses",
    "פאות": "wigs",
    "קוסמטיקה": "cosmetics",
    "תכשיטים": "jewelry",
    "כובעים לחתן": "hats_groom",
    "חליפות חתן": "grooms_suit",
    "נדוניה": "dowry",
    "כובעי נשים": "womens_hats",
    "הזמנות": "invitations",
    "עיצוב אירועים": "event_design",
    "הפקת אירועים": "event_production",
    "רישום נישואין": "marriage",
    "מוהלים": "mohels",
    "גמ\"חים": "gemachim"
}

def clean_filename(name):
    # Remove chars unsafe for Windows filenames
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    clean = clean.strip().replace(" ", "_")
    return clean if clean else "vendor"

def main():
    if not os.path.exists(CATEGORIES_DIR):
        print(f"Error: Categories directory not found at {CATEGORIES_DIR}")
        return

    print("Initializing vendors output directory...")
    if not os.path.exists(VENDORS_OUT_DIR):
        os.makedirs(VENDORS_OUT_DIR)

    categories_summary = []
    
    # Process each category file
    for filename in os.listdir(CATEGORIES_DIR):
        if not filename.endswith(".json"):
            continue
            
        file_path = os.path.join(CATEGORIES_DIR, filename)
        print(f"Processing category file: {filename}...")
        
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                records = json.load(f)
            except Exception as e:
                print(f"  Error reading {filename}: {e}")
                continue
                
        if not records:
            continue
            
        hebrew_cat = records[0].get("category", filename.replace(".json", ""))
        english_slug = CATEGORY_MAPPING.get(hebrew_cat, filename.replace(".json", ""))
        
        cat_dir = os.path.join(VENDORS_OUT_DIR, english_slug)
        if not os.path.exists(cat_dir):
            os.makedirs(cat_dir)
            
        categories_summary.append({
            "hebrew": hebrew_cat,
            "english": english_slug,
            "count": len(records)
        })
        
        # Create a card for each vendor
        for v in records:
            post_id = v.get("post_id", "unknown")
            biz_name = v.get("business_name", "Unnamed Business")
            address = v.get("address", "N/A")
            phones = v.get("phones", [])
            image_url = v.get("image_url", "")
            detail_url = v.get("detail_page_url", "")
            
            details = v.get("details", {})
            description = details.get("description", "")
            email = details.get("email", "")
            
            socials = details.get("social_links", {})
            facebook = socials.get("facebook", "")
            instagram = socials.get("instagram", "")
            whatsapp = socials.get("whatsapp", "")
            
            reviews = details.get("reviews", [])
            gallery = details.get("gallery_images", [])
            
            # Formulate safe filename
            safe_biz = clean_filename(biz_name)
            card_filename = f"{safe_biz}_{post_id}.md"
            card_path = os.path.join(cat_dir, card_filename)
            
            # Build markdown content
            md = []
            md.append(f"# {biz_name}\n")
            md.append(f"**Category (Hebrew):** {hebrew_cat}  ")
            md.append(f"**Category (English):** {english_slug}  ")
            md.append(f"**Post ID:** {post_id}\n")
            
            md.append("## Contact & Location Details")
            md.append(f"- **Address:** {address}")
            if phones:
                md.append(f"- **Phones:** {', '.join(phones)}")
            if email:
                md.append(f"- **Email:** {email}")
            if detail_url:
                md.append(f"- **Website/Detail Link:** [{biz_name} Profile]({detail_url})")
            md.append("")
            
            if facebook or instagram or whatsapp:
                md.append("## Social Links")
                if facebook:
                    md.append(f"- **Facebook:** [Facebook Link]({facebook})")
                if instagram:
                    md.append(f"- **Instagram:** [Instagram Link]({instagram})")
                if whatsapp:
                    md.append(f"- **WhatsApp:** [WhatsApp Chat]({whatsapp})")
                md.append("")
                
            if description:
                md.append("## Description")
                md.append(f"{description}\n")
                
            if image_url or gallery:
                md.append("## Gallery & Images")
                if image_url:
                    md.append(f"![Main Image]({image_url})\n")
                if gallery:
                    md.append("### Extra Images")
                    for img in gallery:
                        md.append(f"- ![Gallery Image]({img})")
                    md.append("")
                    
            if reviews:
                md.append("## Client Reviews")
                for rev in reviews:
                    rev_text = rev.get("raw_text", "").strip()
                    rev_date = rev.get("date", "").strip()
                    date_str = f" ({rev_date})" if rev_date else ""
                    md.append(f"> {rev_text}{date_str}\n")
                md.append("")
                
            md.append("## Client Bookings & Notes")
            md.append("- **Status:** `[ ] Contacted` / `[ ] Quote Received` / `[ ] Booked` / `[ ] Paid`")
            md.append("- **Quote/Pricing Details:** ")
            md.append("- **Meeting Notes:** ")
            md.append("- **Special Requests:** ")
            
            # Save file
            with open(card_path, "w", encoding="utf-8") as out:
                out.write("\n".join(md))
                
    # Generate README index file
    readme_path = os.path.join(VENDORS_OUT_DIR, "README.md")
    readme_md = []
    readme_md.append("# Margan - Wedding Vendors Directory\n")
    readme_md.append("This directory contains individual profile cards (*kartis*) for all wedding vendors compiled from the database. The vendors are grouped by category:\n")
    
    readme_md.append("| Category (Hebrew) | Category (English) | Vendor Count | Browse Link |")
    readme_md.append("| :--- | :--- | :--- | :--- |")
    
    # Sort categories by english slug
    categories_summary.sort(key=lambda x: x["english"])
    
    for cat in categories_summary:
        hebrew = cat["hebrew"]
        english = cat["english"]
        count = cat["count"]
        # Use relative link for markdown navigation
        readme_md.append(f"| {hebrew} | {english} | {count} | [Browse {english}](./{english}/) |")
        
    readme_md.append("\n## How to Re-generate Cards")
    readme_md.append("If the source database updates, run this script to rebuild the markdown vendor cards:")
    readme_md.append("```bash")
    readme_md.append("python scripts/generate_vendor_cards.py")
    readme_md.append("```")
    
    with open(readme_path, "w", encoding="utf-8") as out:
        out.write("\n".join(readme_md))
        
    print(f"\nSuccessfully generated vendor cards index at {readme_path}")
    print(f"Generated cards in {len(categories_summary)} categories.")

if __name__ == "__main__":
    main()
