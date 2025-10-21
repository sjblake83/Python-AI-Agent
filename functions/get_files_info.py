import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
        
    return_string = []
    
    if directory == ".":
        return_string.append(f"Result for current directory:")
    else:
        return_string.append(f"Result for '{directory}' directory:")
     
    if not os.path.isdir(target_dir):
        return_string.append(f'Error: "{directory}" is not a directory')
        return "\n".join(return_string)
    if not target_dir.startswith(abs_working_dir):
        return_string.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "\n".join(return_string)
    
    directory_contents = os.listdir(target_dir)
    return_string.extend(_format_output(directory_contents, target_dir))
    return "\n".join(return_string)

def _format_output(directory_output, full_path):
    try:
        return_string = []
        for output in directory_output:
            output_path = os.path.join(full_path, output)
            file_size = os.path.getsize(output_path)
            is_dir = os.path.isdir(output_path)
            return_string.append(f" - {output}: file_size={file_size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error listing files: {e}"
    return return_string