import os
import base64

# Function to decode Base64-encoded data
def decode_data(encoded_data):
    return base64.b64decode(encoded_data.encode("utf-8"))

# Function to restore files from the text format
def restore_files(combined_filename, output_folder):
    with open(combined_filename, "r") as combined_file:
        lines = combined_file.readlines()

    for line in lines:
        filename, data_length, encoded_data = line.strip().split("|", 2)
        decoded_data = decode_data(encoded_data)
        
        output_filepath = os.path.join(output_folder, filename)
        with open(output_filepath, "wb") as output_file:
            output_file.write(decoded_data)

# Parameters
input_combined_filename = "output\\combined_files.txt"  # Combined text-based file
output_folder = "restore"  # Output folder for restored files

# Restore files from the combined text file
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

restore_files(input_combined_filename, output_folder)
