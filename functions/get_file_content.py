import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    return _read_file(abs_file_path)
    
def _read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            file_content_string = f.read(MAX_CHARS)
        except Exception as e:
            return f'Error: {e}'
        
        if file_content_string.__sizeof__() >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string