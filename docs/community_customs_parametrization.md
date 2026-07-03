# Community Customs Parametrization

## Overview
Haredi wedding customs differ significantly between communities (Hasidic, Litvish/Yeshivish, Sephardic, and their sub-groups). The stage use cases in this project describe **one default custom set** ("According to traditional custom in this project…"). This document establishes that those customs are **configurable parameters of a Community Profile**, not hard-coded rules.

At wedding creation, the couple selects (or customizes) a Community Profile; the planning engine ([use_case_planning_engine_and_date_dependencies.md](./use_case_planning_engine_and_date_dependencies.md)) instantiates stage templates according to it. Any individual parameter can be overridden per wedding, because real families frequently mix customs.

---

## Parameter Catalog (initial set)

| Parameter | Options (examples) | Default in this project | Affects |
| :--- | :--- | :--- | :--- |
| **Vort host** | Groom's side / Bride's side / joint | Groom's side | Vort stage template ([use_case_vort_stage.md](./use_case_vort_stage.md)) |
| **Erusin/Tna'im host & location** | Bride's side in bride's city / other | Bride's side, bride's city | Erusin stage template ([use_case_erusin_stage.md](./use_case_erusin_stage.md)) |
| **Tna'im signing moment** | At the Erusin celebration / at the Vort / at the wedding (before Chuppah) | At the Erusin | Ritual items tasks, run-sheet |
| **Engagement gift stage (jewelry to bride, Shas to groom)** | Presented at the Vort / at the Erusin | Purchased around the Vort, presented at the Erusin | Gift tasks — defined **once**, with purchase and presentation sub-tasks attached to the right stages (avoids the duplicate tasks currently implied by the Vort and Erusin documents) |
| **Ketubah Nusach** | Ashkenazi / Sephardic / Hasidic variants | Per family origin | Ketubah sourcing checklist ([use_case_couple_meetings_and_ritual_preps.md](./use_case_couple_meetings_and_ritual_preps.md)) |
| **Shabbat Chatan timing** | Before the wedding (Aufruf) / after the wedding | Before (Ashkenazi) | Shabbat Chatan stage ([use_case_shabbat_chatan.md](./use_case_shabbat_chatan.md)) |
| **Shabbat Sheva Brachot lead** | Bride's side / Groom's side / shared | Bride's side | Sheva Brachot stage ([use_case_sheva_brachot_stage.md](./use_case_sheva_brachot_stage.md)) |
| **Couple meetings norm** | Number range and venue types | 3–5 meetings, quiet public venues | Meeting scheduler |
| **Ceremony components & order** | Badeken, outdoor/indoor Chuppah, Mitzvah Tantz, plate vs glass customs | Standard Ashkenazi-Haredi sequence | Wedding day run-sheet ([use_case_wedding_day.md](./use_case_wedding_day.md)) |
| **Invitation/announcement Nusach** | Community-specific wording and honorifics | Standard Litvish wording | Azmana & Meurasim generators |
| **Music style preset** | Hasidic / Yeshivish / Sephardic repertoire | Per community | Vendor matchmaking filters |

---

## Key Functional Requirements

| Feature | What it does | Why it is needed |
| :--- | :--- | :--- |
| **Community Profile Selector** | At creation, the couple picks a base profile (Hasidic / Litvish / Sephardic / custom) and answers a short questionnaire for ambiguous parameters. | Families identify strongly with their customs; wrong defaults undermine trust immediately. |
| **Per-Wedding Overrides** | Any parameter can be changed for a specific wedding (with re-templating of not-yet-started tasks only). | Mixed-community couples (e.g., Hasidic groom, Sephardic bride) are common. |
| **Template Binding** | Every stage template declares which parameters it consumes, so profiles automatically produce the right hosts, gifts, texts, and run-sheet. | Keeps customs data-driven instead of hard-coded in features. |
