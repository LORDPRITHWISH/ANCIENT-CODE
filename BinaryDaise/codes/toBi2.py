import os
import base64

# Function to encode binary data using Base64 and metadata
def encode_file(filename):
    with open(filename, "rb") as file:
        binary_data = file.read()
    
    encoded_data = base64.b64encode(binary_data).decode("utf-8")
    metadata = f"{os.path.basename(filename)}|{len(encoded_data)}|"
    
    return metadata + encoded_data

# Parameters
input_folder = "zippy"  # Folder containing files to convert
output_text_filename = "output\\combined_files.txt"  # Output text-based combined file

# Encode files and save to the combined text file
with open(output_text_filename, "w") as combined_file:
    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)
        if os.path.isfile(filepath):
            encoded_file = encode_file(filepath)
            combined_file.write(encoded_file + "\n")
