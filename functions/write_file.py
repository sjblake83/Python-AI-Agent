import os
from pathlib import Path

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_folder_path = os.path.dirname(abs_file_path)
    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_folder_path):
        try:
            os.makedirs(abs_folder_path, 0o777, False)
        except Exception as e:
            return f'Error: {e}'
    
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: {e}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'