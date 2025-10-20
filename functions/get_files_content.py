import os
from pathlib import Path

def get_files_info(working_directory, file_path):
    project_name = Path(__file__).resolve().parent.parent.name
    abs_working_directory_path = os.path.abspath(working_directory)
    abs_directory_path = os.path.abspath(file_path)
    return_string = []
    
    if project_name not in os.path.commonpath([abs_working_directory_path, abs_directory_path]):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    full_path = os.path.join(
        abs_working_directory_path, 
        file_path)
    
    if full_path == "" or os.path.isfile(full_path):
        return f'Error: "File not found or is not a regular file: "{file_path}"'
    
    # file reading goes here
    
def _read_file(file_path):
    MAX_CHARS = 10000

def _format_output(directory_output, full_path):
    return_string = []
    for output in directory_output:
        output_path = os.path.join(full_path, output)
        file_size = os.path.getsize(output_path)
        is_dir = os.path.isdir(output_path)
        return_string.append(f" - {output}: file_size={file_size} bytes, is_dir={is_dir}")
    return return_string