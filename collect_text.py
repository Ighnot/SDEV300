import os

# Specify the directory containing the files you want to concatenate
directory_path = '/'

# Specify the output file where the concatenated code will be saved
output_file = 'concatenated_code.txt'

# Initialize an empty string to store the concatenated code
concatenated_code = ''

# Iterate through files in the directory and its subdirectories
for root, _, files in os.walk(directory_path):
    for filename in files:
        if (filename.endswith('app.py') or
                filename.endswith('.html') or
                filename.endswith('.css')):
            file_path = os.path.join(root, filename)
            with open(file_path, 'r') as file:
                code = file.read()
                concatenated_code += f'\n# Code from: {filename}\n\n'
                concatenated_code += code

# Write the concatenated code to the output file
with open(output_file, 'w') as outfile:
    outfile.write(concatenated_code)

