input_binary_file = 'output_binary.txt'
output_zip_file = 'restored_file.zip'

# Read the binary representation from the text file
with open(input_binary_file, 'r') as text_file:
    binary_representation = text_file.read()

# Convert the binary representation back to bytes
restored_binary_data = bytes(int(binary_representation[i:i+8], 2) for i in range(0, len(binary_representation), 8))

# Write the restored binary data back to a zip file
with open(output_zip_file, 'wb') as zip_file:
    zip_file.write(restored_binary_data)

print(f"Binary representation from {input_binary_file} has been restored and written to {output_zip_file}")
