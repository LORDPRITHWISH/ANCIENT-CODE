import os

# Function to convert a file to binary
def file_to_binary(filename):
    with open(filename, "rb") as file:
        binary_data = file.read()
    return binary_data

# Function to convert binary data back to files
def binary_to_files(binary_data, output_folder):
    file_start = 0
    while file_start < len(binary_data):
        file_size = int.from_bytes(binary_data[file_start:file_start+4], 'big')
        file_type = binary_data[file_start+4:file_start+8].decode()
        file_content = binary_data[file_start+8:file_start+8+file_size]
        
        output_filename = os.path.join(output_folder, f"restored_{file_type}.{file_type}")
        with open(output_filename, "wb") as file:
            file.write(file_content)
        
        file_start += 8 + file_size

# Parameters
input_folder = "zippy"  # Folder containing files to convert
output_binary_filename = "output\\combined_files.bin"  # Output binary file
output_folder = "restore"  # Output folder for restored files

# Convert files to binary
binary_data = b''
for filename in os.listdir(input_folder):
    filepath = os.path.join(input_folder, filename)
    if os.path.isfile(filepath):
        file_type = filename.split('.')[-1]
        file_binary = file_to_binary(filepath)
        file_size = len(file_binary).to_bytes(4, 'big')
        file_type_bytes = file_type.encode()
        binary_data += file_size + file_type_bytes + file_binary

# Save binary data to a file
with open(output_binary_filename, "wb") as file:
    file.write(binary_data)

# Convert binary data back to files
binary_to_files(binary_data, output_folder)
