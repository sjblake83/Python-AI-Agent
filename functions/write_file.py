import os
from pathlib import Path

def write_file(working_directory, file_path, content):
    project_name = Path(__file__).resolve().parent.parent.name
    abs_working_directory_path = os.path.abspath(working_directory)
    abs_directory_path = os.path.abspath(file_path)
    
    if project_name not in os.path.commonpath([abs_working_directory_path, abs_directory_path]):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    full_path = os.path.join(
        abs_working_directory_path, 
        file_path)
    
    if not os.path.isfile(full_path):
        try:
            os.makedirs(full_path, 0o777, False)
        except Exception as e:
            return f'Error: {e}'
    
    try:
        with open(full_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: {e}'