import os
import pathlib

# Specify the directory containing the Python files
directory = pathlib.Path(__file__).parent.absolute()

# The line you want to prepend
line_to_prepend = "from dodesign.show import show\n"

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.py'):
        filepath = os.path.join(directory, filename)
        
        # Read the existing contents of the file
        with open(filepath, 'r') as file:
            content = file.readlines()
        
        # Prepend the new line to the content
        content.insert(1, line_to_prepend)
        
        # Write the modified content back to the file
        with open(filepath, 'w') as file:
            file.writelines(content)
