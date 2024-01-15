# Read the content of the text file
with open("input.txt", "r") as text_file:
    text_content = text_file.read()

# Convert text content to binary (UTF-8 encoded)
binary_data = text_content.encode("utf-8")

# Write binary data to a binary file
with open("output.bin", "wb") as binary_file:
    binary_file.write(binary_data)
