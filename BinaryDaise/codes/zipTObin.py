zip_file_path = 'zippy\\test.zip'
output_binary_file = 'output\\data.bin'

with open(zip_file_path, 'rb') as zip_ref:
    binary_data = zip_ref.read() 

# Write the binary data to a new binary file
with open(output_binary_file, 'wb') as bin_file:
    bin_file.write(binary_data)

print(f"Binary data from {zip_file_path} has been stored in {output_binary_file}")
