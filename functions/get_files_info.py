import os

def get_files_info(working_directory, directory="."):
    abs_working_directory_path = os.path.abspath(working_directory)
    abs_directory_path = os.path.abspath(directory)
    
    if directory == ".":
        print(f"Result for current directory:")
    else:
        print(f"Result for '{directory}' directory:")
     
    
    
    if abs_directory_path == "":
        print(f'Error: "{directory}" is not a directory')
        return
    if os.path.commonpath([abs_working_directory_path, abs_directory_path]) == "":
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
    
    full_path = os.path.join(
        abs_working_directory_path, 
        directory)
    directory_contents = os.listdir(full_path)
    format_output(directory_contents, full_path)

def format_output(directory_output, full_path):
    for output in directory_output:
        output_path = os.path.join(full_path, output)
        file_size = os.path.getsize(output_path)
        is_dir = os.path.isdir(output_path)
        print(f" - {output}: file_size={file_size} bytes, is_dir={is_dir}")