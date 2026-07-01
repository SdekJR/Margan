import json
import os

JSON_PATH = r"c:\Users\shimo\OneDrive\Projects\WeddingData\wedding_vendors.json"

if not os.path.exists(JSON_PATH):
    print("Error: JSON not found")
else:
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Total vendors: {len(data)}")
    
    categories = {}
    for item in data:
        cat = item.get("category", "Unknown")
        categories[cat] = categories.get(cat, 0) + 1
        
    for cat, count in categories.items():
        print(f"Category '{cat}': {count} vendors")
