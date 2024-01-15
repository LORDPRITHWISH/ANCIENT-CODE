import base64

zip_file_path = 'zippy\\test.zip'
output_text_file = 'output\\sample.txt'

with open(zip_file_path, 'rb') as zip_file:
    binary_data = zip_file.read()

# Encode the binary data using Base64
base64_encoded_data = base64.b64encode(binary_data)

# Write the encoded data to a text file
with open(output_text_file, 'wb') as text_file:
    text_file.write(base64_encoded_data)

print(f"Binary data from {zip_file_path} has been encoded and written to {output_text_file}")
