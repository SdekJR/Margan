import os

VENDORS_OUT_DIR = r"c:\Users\shimo\OneDrive\Projects\Margan\docs"
PRESENTATION_PATH = os.path.join(VENDORS_OUT_DIR, "presentation.md")

def main():
    print("Generating Marp-compatible presentation slide deck...")
    
    slides = []
    
    # Slide 1: Title
    slides.append("""---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f5f5f5
color: #333333
---

# **MARGAN**
### Intelligent Agent for Complex Life Milestones
*Initial Case: Haredi Wedding Organization*

---""")

    # Slide 2: Vision
    slides.append("""# **1. Product Vision**
- **What is Margan?** An active, AI-driven planning assistant for high-complexity milestones.
- **Platforms:** Web Browsers, iOS, Android.
- **Core Strategy:**
  - AI-Driven Planning Roadmaps
  - Multi-Party Financial Splits & Reconciliation
  - Highly Contextual Vendor Matchmaking
  - Automated Reminders & Kosher Phone Voice Support
---""")

    # Slide 3: Chronology
    slides.append("""# **2. Planning Chronology**
- **Phase 1:** Matchmaking (*Shidduch*) & Initial Agreements.
- **Phase 2:** Engagement: Vort (Small, Groom-hosted) & Erusin (Large, Bride-hosted).
- **Phase 3:** Marriage Registration (Rabanut) & Reciprocal Shabbat Visits.
- **Phase 4:** Technical & Living Prep (Apartment, Furniture, Kosher utensils).
- **Phase 5:** Pre-Wedding Week & Shabbat Chatan.
- **Phase 6:** Wedding Day & Sheva Brachot Week.
---""")

    # Slide 4: Vort & Erusin Logistics
    slides.append("""# **3. Vort & Erusin Stages**
- **The Vort (Sub-stage 2A):**
  - Hosted at groom's home / small synagogue.
  - Refreshments shopping list, close family invites, newspaper announcement (*Meurasim*).
- **The Erusin / Tna'im (Sub-stage 2B):**
  - Large celebration (~200 guests) hosted by the bride's side.
  - Booking hall, catering, sound system/musicians, guest shuttle logistics.
  - Shtar Tna'im document signing & plate-breaking.
---""")

    # Slide 5: Rabbinate & Shabbat Visits
    slides.append("""# **4. Rabanut & Shabbat Visits**
- **Marriage Registration (*Rabanut*):**
  - Opened immediately after Erusin (90-21 days before wedding).
  - Document collection, witness testimonies, *Kallah* class completion.
- **Reciprocal Shabbat Visits:**
  - Host side books neighborhood guest lodging, stocks room with refreshments (*Kibbud*).
  - Guest side purchases and brings family gifts for parents and siblings.
---""")

    # Slide 6: Apartment & Living Prep
    slides.append("""# **5. Living Prep (Bayit Ne'eman)**
*Must be finalized 2 weeks before the wedding (search starts 1.5 months prior)*
- **Renting:** Sourcing unfurnished apartments (via portals like Yad2).
- **Furniture:** 2 separate beds/mattresses (for Niddah compliance), dining set, wardrobe, *Sifriah*.
- **Appliances:** Refrigerator, washing machine, gas stove/oven combo.
- **Kosher Utensils:** Strict dual-set kitchenware (Dairy/Meat separation).
---""")

    # Slide 7: Wedding & Sheva Brachot
    slides.append("""# **6. Wedding Day & Sheva Brachot**
- **Wedding Day:**
  - Separate receptions (*Kabbalat Panim* for bride, *Tisch* for groom).
  - *Badeken* (veiling), *Chuppah*, *Yichud* room, separate dancing.
- **Sheva Brachot Week:**
  - 7 days of post-wedding festive dinners hosted by different family/friends.
  - **Shabbat Sheva Brachot:** Large logistical Shabbat hosted in bride's city (hall rental, guest lodging, multi-meal catering).
---""")

    # Slide 8: Kosher Phone Voice Integration
    slides.append("""# **7. Kosher Phone Voice Agent**
*Critical accessibility feature for the Haredi community*
- **The Challenge:** Many Haredi users use internet-disabled, voice-only "kosher phones."
- **The Solution:** Interactive Voice Response (IVR) phone line:
  - Caller ID (CLI) automated authentication.
  - Conversational speech-to-text queries in Hebrew/Yiddish.
  - Voice task updates ("Mark task as done").
  - Verbal budget tracking ("Add 500 shekels for Vort drinks").
---""")

    # Slide 9: Competitor Analysis & Gaps
    slides.append("""# **8. Competitor Gap Analysis**
- **Market Players:** Israeli directories (mit4mit, Mitchatnim), agencies (Easywed), and global giants (The Knot, Zola, Joy).
- **What Competitors Lack:**
  - Multi-Party Collaboration (shared/split budgets and tasks).
  - Religious Jewish calendar calculations.
  - Orthodox logistics (gender-segregated guest lists, Niddah beds, double kitchenware).
  - Post-wedding Sheva Brachot coordination.
---""")

    # Slide 10: Summary & Conclusion
    slides.append("""# **9. Margan Summary**
- **Value Proposition:** Margan is the only wedding/milestone planner customized for complex Orthodox family requirements.
- **Next Steps:**
  - Finalize specifications and UI mockups.
  - Design the database schema based on split-budget/multi-user logic.
  - Develop the telephony interface architecture.

### **Thank You!**""")

    # Save to file
    with open(PRESENTATION_PATH, "w", encoding="utf-8") as out:
        out.write("\n".join(slides))
        
    print(f"Presentation saved successfully to: {PRESENTATION_PATH}")

if __name__ == "__main__":
    main()
