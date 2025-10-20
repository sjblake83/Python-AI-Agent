import os
from pathlib import Path

def get_files_info(working_directory, directory="."):
    project_name = Path(__file__).resolve().parent.parent.name
    abs_working_directory_path = os.path.abspath(working_directory)
    abs_directory_path = os.path.abspath(directory)
    return_string = []
    
    if directory == ".":
        return_string.append(f"Result for current directory:")
    else:
        return_string.append(f"Result for '{directory}' directory:")
     
    if abs_directory_path == "":
        return_string.append(f'Error: "{directory}" is not a directory')
        return "\n".join(return_string)
    if project_name not in os.path.commonpath([abs_working_directory_path, abs_directory_path]):
        return_string.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "\n".join(return_string)
    
    full_path = os.path.join(
        abs_working_directory_path, 
        directory)
    directory_contents = os.listdir(full_path)
    return_string.extend(_format_output(directory_contents, full_path))
    return "\n".join(return_string)

def _format_output(directory_output, full_path):
    return_string = []
    for output in directory_output:
        output_path = os.path.join(full_path, output)
        file_size = os.path.getsize(output_path)
        is_dir = os.path.isdir(output_path)
        return_string.append(f" - {output}: file_size={file_size} bytes, is_dir={is_dir}")
    return return_string