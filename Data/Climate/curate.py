import os
import subprocess
import shutil

# Retrieve the remote storage information from environment variables or secrets
remote_storage = os.environ.get("REMOTE_STORAGE_PATH")
climate_folder = os.path.join(remote_storage, "Climate")

# Create the Climate folder if it doesn't exist
os.makedirs(climate_folder, exist_ok=True)

# Change the working directory to the remote storage
os.chdir(remote_storage)

# Listen for DVC push commands
while True:
    command = input("Enter DVC push command (or 'exit' to quit): ")

    if command.strip() == "exit":
        break

    # Run the DVC push command
    try:
        subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing DVC push command: {e}")
        continue

    # Get the DVC file paths from the command
    dvc_files = []
    for arg in command.split():
        if arg.endswith(".dvc"):
            dvc_files.append(arg)

    # Curation only for pushed DVC files
    if dvc_files:
        # Move the DVC files to the Climate folder
        for dvc_file in dvc_files:
            dvc_filename = os.path.basename(dvc_file)
            climate_dvc_path = os.path.join(climate_folder, dvc_filename)

            try:
                shutil.move(dvc_file, climate_dvc_path)
                print(f"Moved {dvc_file} to {climate_dvc_path}")
            except Exception as e:
                print(f"Error moving {dvc_file} to {climate_dvc_path}: {e}")

        # Push the curated DVC files to remote storage
        try:
            subprocess.check_output("dvc push", shell=True)
            print("Pushed curated DVC files to remote storage")
        except subprocess.CalledProcessError as e:
            print(f"Error pushing curated DVC files to remote storage: {e}")
    else:
        print("No DVC files pushed.")
