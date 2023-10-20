## SDG Mapping Prototype

This document outlines the Sustainable Development Goal (SDG) mapping prototypes developed for various land sector datasets. Each section details the specific dataset used, the attributes analyzed, the rationale behind the mapping, and the outcomes of the process.

---

### Climate Dataset

#### SDG 13: Climate Action

*Dataset Attributes*:
- `Value`: Represents various climate zones, including Warm Temperate (Moist/Dry), Cool Temperate (Moist/Dry), Polar (Moist/Dry), Boreal (Moist/Dry), and Tropical Montane.

*Mapping Explanation*:
- The dataset's classification of areas into specific climate zones provides vital information for climate action initiatives, helping identify the most vulnerable areas and informing suitable mitigation and adaptation strategies.

*Python Mapping Result*:
- All entries were mapped to "SDG 13: Climate Action" due to their relevance to climate categorization and the implications for climate change mitigation and adaptation.

---

### Soil Dataset

#### SDG 15: Life on Land 

*Dataset Attributes*:
- `SNAME`: Soil name abbreviation.
- `IPCC`: Classification of soil types according to IPCC categories.

*Mapping Explanation*:
- The dataset's classification of soil types is crucial for understanding land health and usage, biodiversity, carbon sequestration, and other ecological factors.

*Python Mapping Result*:
- All soil types were mapped to both "SDG 15: Life on Land" due to its importance in  land ecosystem health.

---

### Global Biodiversity Hotspots Dataset

#### SDG 14: Life Below Water & SDG 15: Life on Land

*Dataset Attributes*:
- `NAME`: The name of the biodiversity hotspot.

*Mapping Explanation*:
- The dataset identifies areas critical for biodiversity conservation. The `map_biodiversity_to_sdg` function categorizes these areas into either marine or terrestrial hotspots. This distinction is based on a predefined list of locations known for their marine biodiversity. If a hotspot is on this list, it is mapped to "SDG 14: Life Below Water"; otherwise, it defaults to "SDG 15: Life on Land."

*Python Mapping Result*:
- Entries corresponding to known marine hotspots, such as 'New Caledonia', 'Caribbean Islands', 'East Melanesian Islands', 'Polynesia-Micronesia', 'Coral Triangle', and 'Madagascar and the Indian Ocean Islands', were mapped to "SDG 14: Life Below Water."
- All other entries were mapped to "SDG 15: Life on Land" due to their relevance to terrestrial biodiversity conservation.

---

