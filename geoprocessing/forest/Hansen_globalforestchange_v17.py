# Title: Hansen v1.7 Global Forest Change
# Description: Results from time-series analysis of Landsat images in characterizing global forest extent and change from 2000 through 2019. For additional information about these results, please see the associated journal article (Hansen et al., Science 2013).
# Original source: http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.7.html
# Licence: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made. 
## Data display: Use the following credit when these data are displayed: "Source: Hansen/UMD/Google/USGS/NASA"
## Citation: Use the following credit when these data are cited: Hansen, M. C., P. V. Potapov, R. Moore, M. Hancher, S. A. Turubanova, A. Tyukavina, D. Thau, S. V. Stehman, S. J. Goetz, T. R. Loveland, A. Kommareddy, A. Egorov, L. Chini, C. O. Justice, and J. R. G. Townshend. 2013. “High-Resolution Global Maps of 21st-Century Forest Cover Change.” Science 342 (15 November): 850–53. Data available on-line from: http://earthenginepartners.appspot.com/science-2013-global-forest.
# Format: global coverage tiled(503) geo tiff (.tif), cell size 0.00025 degree, resolution 40000 x 40000 Pixels, cordinate system EPSG:4326 WGS84
# Metadata: full metadata can be viewed here http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.7.html
# Dataset names: treecover2000, loss, gain, datamask, first and last:
## Tree canopy cover for year 2000 (treecover2000) - Tree cover in the year 2000, defined as canopy closure for all vegetation taller than 5m in height. Encoded as a percentage per output grid cell, in the range 0–100.
## Global forest cover gain 2000–2012 (gain) Forest gain during the period 2000–2012, defined as the inverse of loss, or a non-forest to forest change entirely within the study period. Encoded as either 1 (gain) or 0 (no gain).
## Year of gross forest cover loss event (lossyear) Forest loss during the period 2000–2019, defined as a stand-replacement disturbance, or a change from a forest to non-forest state. Encoded as either 0 (no loss) or else a value in the range 1–17, representing loss detected primarily in the year 2001–2019, respectively.
## Data mask (datamask) Three values representing areas of no data (0), mapped land surface (1), and permanent water bodies (2).
## Circa year 2000 Landsat 7 cloud-free image composite (first) Reference multispectral imagery from the first available year, typically 2000. If no cloud-free observations were available for year 2000, imagery was taken from the closest year with cloud-free data, within the range 1999–2012.
## Circa year 2019 Landsat cloud-free image composite (last) Reference multispectral imagery from the last available year, typically 2019. If no cloud-free observations were available for year 2019, imagery was taken from the closest year with cloud-free data, within the range 2010–2015.
# Note: tiles may contain no data if over the ocean and updates are intended so please check back at the #original source.

# FLINT: This dataset is suitable for use in FLINT and is made available for download via the moja-global Land Sector Dataset google drive: https://drive.google.com/drive/folders/15ZguDQXecJJ8UV49MNZxN_xb2YlPvOjQ?usp=sharing

#Bulk download tiles
#Text URLS treecover2000.txt, loss.txt, gain.txt, datamask.txt, first.txt, last.txt
#Python 3
import urllib.request
import os.path

# text file containing urls for download downloaded from https://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.7.html (see download instructions)
links = open('C:\\enterpath\\gain.txt', 'r')

# directory to save tifs into (insert your own folder path)
folder = 'C:\\enterpath\\'

# open and download links in bulk
for link in links:
	link = link.strip()
	name = link.rsplit('/', 1)[-1]
	filename = os.path.join(folder, name)
	if not os.path.isfile(filename):
		print('Downloading: '+ filename)
	try:
		urllib.request.urlretrieve(link, filename)
	except Exception as inst:
		print(inst)
		print('  Encountered unknown error. Continuing.')
