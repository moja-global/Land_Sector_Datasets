# Title: Hansen v1.7 Global Forest Change
# Info: Results from time-series analysis of Landsat images in characterizing global forest extent and change from 2000 through 2019. For additional information about these results, please see the associated journal article (Hansen et al., Science 2013).
# Original source: http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.7.html
# Licence: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made. 
## Data display: Use the following credit when these data are displayed: "Source: Hansen/UMD/Google/USGS/NASA"
## Citation: Use the following credit when these data are cited: Hansen, M. C., P. V. Potapov, R. Moore, M. Hancher, S. A. Turubanova, A. Tyukavina, D. Thau, S. V. Stehman, S. J. Goetz, T. R. Loveland, A. Kommareddy, A. Egorov, L. Chini, C. O. Justice, and J. R. G. Townshend. 2013. “High-Resolution Global Maps of 21st-Century Forest Cover Change.” Science 342 (15 November): 850–53. Data available on-line from: http://earthenginepartners.appspot.com/science-2013-global-forest.
# Metadata: http://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.7.html
# Format: tile tiff (.tif), cell size 0.00025 degree, resolution 40000 x 40000 Pixels, cordinate system EPSG:4326 WGS84
# Dataset names: treecover2000, loss, gain, datamask, first and last. Information on each of these types is available at the #Access link. This dataset is tiled and can be downloaded in bulk using text files accessed from https://earthenginepartners.appspot.com/science-2013-global-forest/download_v1.7.html or by manually selecting tiles of interest and downloading directly. Bulk download code is provided below.
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
