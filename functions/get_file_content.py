import os
from pathlib import Path
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    project_name = Path(__file__).resolve().parent.parent.name
    abs_working_directory_path = os.path.abspath(working_directory)
    abs_directory_path = os.path.abspath(file_path)
    
    if project_name not in os.path.commonpath([abs_working_directory_path, abs_directory_path]):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    full_path = os.path.join(
        abs_working_directory_path, 
        file_path)
    
    if full_path == "" or not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    return _read_file(full_path)
    
def _read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            file_content_string = f.read(MAX_CHARS)
        except Exception as e:
            return f'Error: {e}'
        
        if file_content_string.__sizeof__() >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string