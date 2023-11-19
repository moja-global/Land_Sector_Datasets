# GEOSPATIAL ANALYSIS DOCUMENTATION

**DATASETS**
1. Biodiversity Hotspot
2. World Soil Resources

# BIODIVERSITY HOTSPOT ANALYSIS

**Perimeter Analysis**

The result of the area_stats shows summary statistics for the **"Shape_Length"** variable.

count: there are 53 observations.

mean: The mean is approximately 150.46.

std: The standard deviation, which measures the amount of variation or dispersion, is approximately 280.34, indicating a relatively high degree of variability.

min: The minimum value of "Shape_Length" is approximately 1.65, indicating the smallest area in the dataset.

25%: The 25th percentile, which is the value below which 25% of the data falls. It is approximately 27.49.

50%: The 50th percentile, also known as the median is approximately 73.22.

75%: The 75th percentile, which is the value below which 75% of the data falls is approximately 170.56.

max: The maximum value of "Shape_Length" is approximately 1909.52, indicating the largest area in the dataset.

Overall, the summary statistics provide insights into the distribution and variation of the "Shape_Length" variable. The relatively high standard deviation and the difference between the mean and median suggest that the dataset has some outliers or is positively skewed. The range between the minimum and maximum values is also quite large.

**Area Analysis**

In summary, the "Shape_Area" values in the dataset vary widely, with a relatively high standard deviation. There are small to very large geographic areas represented. The median is considerably smaller than the mean, indicating that there may be some larger outliers or skewed distribution towards larger areas. The majority of areas (50% to 75%) are relatively small, while a few areas are significantly larger (outliers).

The distribution of "Shape_Area" is negatively skewed 

**Density Analysis**

"Total Biodiversity Hotspot Density: 6646.16 hotspots per square kilometer," indicates a very high density of biodiversity hotspots in the biodiversity dataset.

This high density suggests that, on average, there are more than 6,000 biodiversity hotspots within every square kilometer of the areas included in your dataset. It implies that your dataset contains a concentrated distribution of biodiversity hotspots.

**Distribution of Hotspot area and Outer limit**

From the information and the bar chart you've provided, we can draw the following inferences:

Large Outer Limit Area: The total area covered by "Outer Limits" in the biodiversity dataset is significantly larger than the total area of "Hotspot Areas." This indicates that the "Outer Limits" are extensive and often surround or buffer the core "Hotspot Areas."

Hotspot Areas Concentration: The total area of "Hotspot Areas" is comparatively smaller. These areas contain a concentration of biodiversity that may be of higher conservation importance.

Buffering and Conservation: The extensive "Outer Limits" play a role in buffering and protecting the core "Hotspot Areas." Conservation efforts should consider the entire ecosystem, including both hotspots and their outer limits, for effective protection.

Management Implications: Management and conservation strategies should consider both the core hotspots and their surrounding areas to ensure the preservation of biodiversity across different spatial extents.

The large difference in area between "Outer Limits" and "Hotspot Areas" emphasizes the importance of understanding the spatial distribution of biodiversity and the areas dedicated to conservation efforts.

**Choropleth Map**

In the choropleth map, "hotspot areas"  and "outer limits" are represented as its color is displayed on the legend

This map helps you understand where biodiversity hotspots are concentrated and where the outer limits of these hotspots are.

You can use this map to plan conservation efforts, study the distribution of different types of hotspots, and identify areas with specific characteristics.

**Scatter plot of Shape_Length and Shape_Area**

The scatter plot helps visualize the relationship between 'Shape_Length' and 'Shape_Area' for each data point.
You can observe whether there is any correlation or pattern between these two variables.
Some of the points are randomly scattered, which suggests that there might not be a strong linear relationship between 'Shape_Length' and 'Shape_Area' in those areas while the bottom left area of the plot shows there is a potential relationship between the two variables.

**Spatial AutoCorrelation**

Unfortunately, due to the my Laptop specification, I can't plot the Spatial Autocorrelation map because I can't install python 3.8 ( higher version) 

But from The Moran's I statistic result which quantifies spatial autocorrelation, the p-value is 0.07 (close to 0), which suggests that Shape_Area exhibits strong spatial autocorrelation.

# SOIL

**Univariate Analysis**

Diversity of Soil Classifications: The analysis reveals that there is a wide diversity of soil classifications present in the dataset. There are 30 unique soil classifications represented.

Frequency of Soil Classifications: we can see the frequency (count) of each soil classification in the dataset. 'HAC' appears 2 times, 'Albeluvisol' appears 1 time, 'Kastanozem' appears 1 time, and etc.

Relative Abundance: The count of each classification provides an idea of how prevalent or rare each type of soil is within the dataset. For example, 'HAC' is the most common, occurring twice, while most classifications appear only once, indicating lower prevalence.

Imbalanced Data: The data appears to be imbalanced, with some soil classifications occurring more frequently than others. This imbalance may have implications when conducting further analyses or modeling.

**Distribution of Soil Area**

Variability in Soil Area: The calculated areas of soil polygons vary significantly, as indicated by the wide range of values. Some soil polygons are relatively small (e.g., around 1.62e+11 square meters), while others are much larger (e.g., around 6.17e+13 square meters).

Spatial Heterogeneity: The variation in soil areas suggests spatial heterogeneity in soil distribution. Some regions may have concentrated soil types with larger areas, while others may have more diverse but smaller soil areas.

Outliers: There may be some outliers in the data, representing exceptionally large or small soil areas. These outliers could be due to various factors, including natural geography, land use, or data quality.

# Spatial Overlay of World Soil Resources on Biodiversity Hotspots

Leptosol: Leptosol soil type has the largest total intersection area with biodiversity areas, with an area of approximately 9.02 trillion square meters.

Acrisol: Acrisol soil type also has a significant intersection area, with an area of approximately 6.79 trillion square meters.

Lixisol: Lixisol has an intersection area of approximately 1.58 trillion square meters, making it one of the larger intersections.

Vertisol: Vertisol has an intersection area of approximately 1.15 trillion square meters, indicating a substantial overlap with biodiversity areas.

Ferralsol: Ferralsol has an intersection area of around 4.69 trillion square meters.

Arenosol: Arenosol soil type intersects with biodiversity areas with an area of approximately 2.16 trillion square meters.

Luvisol: Luvisol has an intersection area of around 2.96 trillion square meters.

**Summary Statistics for Intersection Areas by Soil Type**

Count: This tells us the number of instances or occurrences of each soil type in the dataset. Some soil types have higher counts than others, indicating their prevalence in the dataset.

Mean (Average): The mean intersection area for each soil type represents the average area covered by that soil type where it intersects with biodiversity data. Some soil types have larger mean intersection areas than others, suggesting that they cover larger geographical areas on average.

Standard Deviation (std): The standard deviation measures the variation or spread of intersection areas for each soil type. A higher standard deviation indicates greater variability in intersection areas. Soil types with a high standard deviation have more diverse intersection areas, while a low standard deviation indicates more consistent intersection areas.

Min (Minimum): This represents the smallest intersection area for each soil type. It shows the smallest extent of geographical coverage for each soil type.

25% (First Quartile): The first quartile is the value below which 25% of the data falls. It provides insight into the lower range of intersection areas for each soil type.

50% (Median): The median is the middle value of the dataset. It separates the lower 50% of intersection areas from the upper 50%. It's a measure of central tendency.

75% (Third Quartile): The third quartile is the value below which 75% of the data falls. It represents the upper range of intersection areas for each soil type.

Max (Maximum): This is the largest intersection area observed for each soil type. It indicates the maximum geographical coverage for each soil type.

The distribution and variation in these statistics provide insights into the diversity and spread of different soil types in the regions where they intersect with biodiversity data. Some soil types are more widespread, while others are more concentrated in specific areas. The standard deviation also tells us how much the intersection areas for each soil type deviate from their respective means. This information is valuable for understanding the spatial characteristics of soil types in relation to biodiversity.