import cv2

# Parameters for the video and decoding
video_filename = "binary_video.avi"
output_zip_filename = "recovered_files.zip"
threshold = 128  # Adjust this based on your encoding process

# Read video frames
cap = cv2.VideoCapture(video_filename)
binary_data = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Analyze pixel values
    binary_data.extend([1 if pixel[0] > threshold else 0 for row in frame for pixel in row])

cap.release()

# Convert binary data to bytes
binary_bytes = bytearray()
for i in range(0, len(binary_data), 8):
    byte = 0
    for j in range(8):
        byte |= (binary_data[i + j] << (7 - j))
    binary_bytes.append(byte)

# Save as ZIP file
with open(output_zip_filename, "wb") as zip_file:
    zip_file.write(binary_bytes)
