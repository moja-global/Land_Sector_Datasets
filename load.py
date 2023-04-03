import pandas as pd

data_path = 'Data/forest-management-data-2015/reference_data_set_updated.csv'
metafile_path = 'Data/forest-management-data-2015/metafile.txt'

# Load the dataset
df = pd.read_csv(data_path)

# Load the metafile
with open(metafile_path,'r',encoding='utf-8') as f:
    metafile_contents = f.read()

# Process the data and save the result
df=df.dropna()
# Save the whole DataFrame to pickle
df.to_pickle('Data/loaded_data.pkl')
