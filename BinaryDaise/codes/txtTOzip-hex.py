import base64

input_base64_file = 'base64_encoded.txt'
output_zip_file = 'restored_file.zip'

# Read the Base64-encoded data from the text file
with open(input_base64_file, 'rb') as text_file:
    base64_encoded_data = text_file.read()

# Decode the Base64-encoded data back to binary
restored_binary_data = base64.b64decode(base64_encoded_data)

# Write the restored binary data back to a zip file
with open(output_zip_file, 'wb') as zip_file:
    zip_file.write(restored_binary_data)

print(f"Base64-encoded data from {input_base64_file} has been decoded and restored to {output_zip_file}")
 