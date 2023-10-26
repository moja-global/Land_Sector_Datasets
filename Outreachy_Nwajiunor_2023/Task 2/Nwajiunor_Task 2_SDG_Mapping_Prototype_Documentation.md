## SDG Mapping Prototype

This document presents prototypes for mapping Sustainable Development Goals (SDGs) within the administrative land sector dataset. Each section provides information about the dataset under consideration, the attribute considered, the idea for mapping, and the resulting outcomes.

The two SDGs chosen in relevance to the administrative land sector dataset category are Goal 11 and Goal 15.

Goal 11: Sustainable Cities and Communities. It is about making cities and human settlements inclusive, safe, resilient and sustainable. While Goal 15: Life on Land. It is about conserving life on land. It is to protect and restore terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and stop biodiversity loss.

## Administrative Land Sector Dataset

### World Soil Boundary

#### SDG 15: Life on Land

#### Dataset Attribute:

- `IPCC`: IPCC stands for Intergovernmental Panel on Climate Change. The soil names are classified based on the IPCC classificication.

#### Mapping Explanation:

- `Mapped_SDGs`: Is the column that results from mapping. It associates each soil type(resources) with its relevant SDG. In other words, the mapping helps identify which specific SDG(s) are relevant to different soil types, with most of them being associated with SDG 15: Life on Land. However, some entries are not mapped to any SDG, indicating that they might not have a direct association with the two relevant SDGs identified for this task. The number of world soil types that were mapped to SDG 15 were 31 in number while only two world soil resources were not mapped.

SDG 15: Life on Land: This SDG is associated with various soil types listed in the world soil resources dataset. It suggests that these soil types are directly related to SDG 15, which focuses on protecting, restoring, and promoting the sustainable use of terrestrial ecosystems found on the earth's surface.

Not Mapped: This category is for entries that do not directly correspond to either of the aforementioned SDG. They are not explicitly associated with the SDG goals relevant to the task due to their classification as "waterbodies" or "glaciers." These categories, "waterbodies" and "glaciers," do not pertain to soil types. "Waterbodies" encompass features like rivers, lakes, and ponds, which are aquatic in nature and not classified as soil resources. On the other hand, "glaciers" refer to slow-moving bodies of ice, including ice sheets that cover large land areas. While both "waterbodies" and "glaciers" are significant in their own right, they are not categorized as soil resources, yet they play essential roles in the Earth's ecosystem.

### World Protected Areas

#### SDG 11: Sustainable Cities and Communities & SDG 15: Life on Land

#### Dataset Attribute
- `OWN_TYPE`: This column refers to the ownership type or category for the world protected areas. 

#### Mapping Explanation:

- `Mapped_SDGs`: This column associates each ownership type with its relevant SDG. This mapping helps in identifying which SDGs are being addressed by various protected areas, providing insights into the contributions of these areas to global sustainability goals.  Some entries (ownership type) are not mapped to any SDG, indicating that they might not have a direct link with the two relevant SDGs identified for this task, some others were mapped to SDG 11: Sustainable Cities and Communities and the rest were mapped to SDG 15: Life on Land. The number of entereries that were not mapped were 188415 and those that were mapped to SDG 15 were 51686. Only 64 were mapped to SDG 11.

SDG 11: Sustainable Cities and Communities: This SDG is associated with the "for-profit organisations" ownership type as their involvement could influence urban development in cities and communities. 

SDG 15: Life on Land: This SDG is associated with the "Non-profit organisations", "Individual landowners", "Multiple ownership", "Communual", and "Joint ownership" categories. These ownnership types have impact on the protect areas for biodiversity conservation, land protection and management of natural areas.

Not Mapped: This indicates that these protected areas did not fit the criteria for direct mapping to either of the relevant SDG for this task. Ownership types that fall under this is the "Not Reported" and "Contested" categories. It is challenging to link the "Not Reported" category to the relevant SDG without more information, as well as the "Contested" category because nature of the disputes and their implications for land conservation cannot be ascertained.

### Roads

#### SDG 11: Sustainable Cities and Communities

#### Dataset Attribute
- `FCLASS`: This column refers to the column, which represents functional road types. They are represented with integers from 0 - 6. The different road types represented with integers are defined as follows; 1=Highway, 2=Primary, 3=Secondary, 4=Tertiary, 5=Local/Urban, 6=Trail, 0=unspecified.

#### Mapping Explanation:

- `Mapped_SDGs`: This column associates each functional road type with its relevant SDG. This mapping helps in identifying which SDGs are being addressed by various protected areas, providing insights into the contributions of these areas to global sustainability goals. All enteries (functional classes) were mapped to SDG 11 which equated to a total of 1101300. 

SDG 11: Sustainable Cities and Communities: The functional road types are all related to urban and rural infrastructure, transportation, and accessibility within cities and communities. Therefore,they can map be mapped to SDG 11, as it addresses the goal of making cities and human settlements inclusive, safe, resilient, and sustainable. The different road types are essential components of urban and rural infrastructure, and their quality and accessibility are important factors in achieving this sustainability goal.

[To access the saved mapped datasets for each section of the administrative land sector category, click on this link.](https://drive.google.com/drive/folders/1ZGqZaco55mJDn8uVXH6Y6l3DcVe-Gu6m?usp=share_link)

#### References

These references aided the research process for this task. 

[SDGs Definition by UNDP](https://www.undp.org/sustainable-development-goals#:~:text=What%20are%20the%20Sustainable%20Development,people%20enjoy%20peace%20and%20prosperity)

[SDG 11](https://www.un.org/sustainabledevelopment/cities/#:~:text=Goal%2011%3A%20Make%20cities%20inclusive%2C%20safe%2C%20resilient%20and%20sustainable&text=Goal%2011%20is%20about%20making,half%20living%20in%20urban%20areas)

[SDG 15](http://wdpa.s3.amazonaws.com/WDPA_Manual/English/WDPA_Manual_1_4_EN_FINAL.pdf)

[World Database of Protected Areas](http://wdpa.s3.amazonaws.com/WDPA_Manual/English/WDPA_Manual_1_4_EN_FINAL.pdf)

[Global Roads Open Access Dataset Documentation](https://sedac.ciesin.columbia.edu/downloads/docs/groads/groads-v1-documentation.pdf)

