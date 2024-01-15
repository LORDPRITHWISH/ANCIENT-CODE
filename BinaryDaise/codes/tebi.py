import base64

def decode_data(encoded_data):
    return base64.b64decode(encoded_data.encode("utf-8"))

# Read the combined text file
with open("output\\combined_files.txt", "r") as combined_file:
    lines = combined_file.readlines()

# Decode and combine the Base64-encoded data
binary_data = b''
for line in lines:
    _,_, encoded_data = line.strip().split("|", 2)
    binary_data += decode_data(encoded_data)

# Save the binary data to a binary file
with open("output\\combined_binary.bin", "wb") as binary_file:
    binary_file.write(binary_data)
