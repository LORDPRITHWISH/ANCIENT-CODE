import os
import base64

# Function to convert a file to binary
def file_to_binary(filename):
    with open(filename, "rb") as file:
        binary_data = file.read()
    return binary_data

# Parameters
input_folder = "zippy"  # Folder containing files to convert
output_binary_filename = "output\\combined_files.txt"  # Output combined binary file

# Convert files to binary and encode using Base64
binary_data = b''
for filename in os.listdir(input_folder):
    filepath = os.path.join(input_folder, filename)
    if os.path.isfile(filepath):
        file_type = filename.split('.')[-1]
        file_binary = file_to_binary(filepath)
        file_size = len(file_binary).to_bytes(4, 'big')
        file_type_bytes = file_type.encode()
        binary_data += file_size + file_type_bytes + file_binary

# Encode binary data using Base64
encoded_data = base64.b64encode(binary_data)

# Save encoded data to a text file
with open(output_binary_filename, "wb") as file:
    file.write(encoded_data)
