zip_file_path = 'zippy\\test.zip'
output_binary_file = 'output\\sample0110.txt'

with open(zip_file_path, 'rb') as zip_file:
    binary_data = zip_file.read()

# Convert binary data to binary representation
binary_representation = ''.join(format(byte, '08b') for byte in binary_data)

# Write the binary representation to a text file
with open(output_binary_file, 'w') as text_file:
    text_file.write(binary_representation)

print(f"Binary data from {zip_file_path} has been written in binary representation to {output_binary_file}")
