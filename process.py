import pandas as pd
import subprocess

data_path = 'Data/loaded_data.pkl'
output_path = 'Data/processed_data.csv'

# Load the data
df = pd.read_pickle(data_path)

# Process the data
df = df.dropna()
df = df.reset_index(drop=True)

# Save the processed data
df.to_csv(output_path, index=False)

# Add the output file to DVC
subprocess.run(['dvc', 'add', output_path])
