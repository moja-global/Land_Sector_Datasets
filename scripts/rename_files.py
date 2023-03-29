import os

current_directory = os.getcwd()
target_parent_dir = os.path.join(current_directory, r'tmp_unzip_path/data')
if os.path.exists(target_parent_dir):
    for file_name in os.listdir(target_parent_dir):
        if '\\' in file_name:
            old_file_name = os.path.join(target_parent_dir, file_name)
            filename = os.fsdecode(file_name)
            changed_name = filename.replace("\\", "_")
            new_file_name = os.path.join(target_parent_dir, changed_name)
            os.rename(old_file_name,new_file_name)