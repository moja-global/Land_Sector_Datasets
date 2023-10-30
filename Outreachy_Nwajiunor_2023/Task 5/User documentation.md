# User Documentation

Effective land sector management plays a crucial role in ensuring sustainable agriculture, biodiversity conservation, and overall environmental quality. This user documentation provides a comprehensive guide on how to work with the Land Sector Dataset repository for in-depth data analysis. The documentation includes an overview of the tasks, tools used, and key insights derived from the analysis.

## Table of Contents

1. Getting Started
2. SDGs Alignment/ Mapping
3. Geospatial Analysis
4. Data Visualization
5. Results
6. FAQs
7. Conclusion

### 1. Getting Started

**Objective**
The primary goal of this project was to analyze the Land Sector Dataset repository. This repository contains data related to administrative, biological and ecological, soil, land cover and climate. The project aimed to extract meaningful insights, spatial patterns and relationships from these datasets. 

**Prerequisites**
Before proceeding, it is assumed that you would have met some conditions:

a. Basic understanding of geospatial data and the concepts of SDGs. 

b. You will also need a performant desktop machine or laptop with a minimum storage of 128GB and 8GB RAM  is required for pre-processing global open-source datasets, as spatial datasets can be memory-intensive.

**Datasets**
- Administrative
- Biodiveersity, AgroClimatic and Ecological Zones
- Land Cover
- Soil 

### 2. SDGs Alignment/Mapping
Datasets are matched with relevant SDGs to identify goals related to land sector data, including land use, environmental impact, and social implications.

### 3. Geospatial Analysis

Focused on global patterns, specifically examining the interplay between soil types, ecosystem services, protected areas, and road networks on a global scale. These insights have the potential to inform diverse domains, encompassing environmental management, infrastructure planning, and ecological research.

### 4. Data Visualization

The visualization tools provide valuable insights into the alignment between various datasets and the Sustainable Development Goals (SDGs). Here's how you can effectively use these tools:

Exploring Unassigned Entries: The visual representations reveal that a substantial number of entries (188,415) remain unassigned to specific SDGs. Users can delve into these entries, particularly those categorized as "unspecified" or "contested" based on the "Ownership Structure" column within the "Protected Areas" dataset. This exploration can help uncover hidden information and assist in SDG mapping.

Focusing on Specific SDGs: Users can filter the visualizations to focus on a particular SDG of interest. For example, if they want to understand how road types align with SDG 11: Sustainable Cities & Communities, they can use the visualization tools to explore these connections in detail.

Identifying Spatial Overlaps: The red areas on the map represent the intersection of the Mapped SDG Roads and Mapped SDG World Resources. Users can study these regions to understand where these datasets spatially overlap and how they are interconnected.

Gaining Insights: Users can draw meaningful insights from the visual representations, such as understanding the alignment of road types with specific SDGs. This information can be valuable for research, decision-making, and policy development.

### 5. Results
- The clear mapping of soil resources to SDG 15 underscores the significance of these resources in achieving the SDG's objectives, particularly related to terrestrial ecosystem conservation.

- The alignment of road types with SDG 11 emphasizes the role of infrastructure in creating sustainable and resilient urban environments.

- Spatial intersections pinpoint areas where mapped SDG Roads coincide with world resources, providing opportunities for in-depth analysis of resource accessibility and infrastructure development.

- The presence of 188,415 unassigned entries in the "Protected Areas" dataset underscores the need for further data categorization, likely driven by issues such as "unspecified" or "contested" classifications.

- The majority of mapped entries (51,686) aligned with SDG 15, highlighting a strong focus on the conservation and sustainable management of terrestrial ecosystems within the "Protected Areas" dataset.

### 6. FAQs

Q1. Who can use this documentation?

A. This is designed for researchers, policymakers, analysts, and anyone interested in exploring the impact of land attributes on sustainability goals.

Q2. What do I need to get started?

A. To get started, you will need;

- Basic understanding of geospatial data and the concepts of SDGs. 
- You need a desktop or laptop with a minimum storage of 128GB and 8GB RAM  is required for pre-processing global open-source datasets. 
-  Python installed on your system
- An internet connection is required for data retrieval.

Q3. How do I install Python on my system?

A. You can download and install Python by following the official Python installation guide. Visit the Python website at [python.org](https://www.python.org/)  

Q4. Do I need to install the GeoPandas library?

A. Yes, the Land Sector Data utilizes geospatial analysis and mapping features, which require the GeoPandas library. To install the GeoPandas library, use this command `pip install geopandas` in the terminal or console. 

Q5. What kind of data would I work with?

A. You would be working with various datasets related to land use, environmental impact, and social implications, all aligned with specific SDGs.

Q6. Is this an open source project?

A: Yes, this is an open source project. It means that the source code of the software is freely available, and anyone can view, modify, and distribute it according to the terms of its open source license. This openness encourages collaboration, transparency, and the community's active participation in its development.

Q7. Can I explore specific attributes in the data?

A. Yes, you can select specific attributes within the datasets to analyze and visualize their relationship with SDGs.

**Contact Information:** For all inquiries, feedback, or technical support, the support team is readily available to assist you. Please feel free to contact via info@moja.global

### 7. Conclusion

This document is a complete guide for understanding integrated land sector data and how to use visualization tools. It helps users in land management, conservation, and following global SDG goals. With the provided data, tools, and interactive prototype, users can make well-informed decisions in land management and sustainable development, all aligned with the SDGs.