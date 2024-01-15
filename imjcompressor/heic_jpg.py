from PIL import Image

def convert_heic_to_jpg(heic_file, jpg_file):
    try:
        img = Image.open(heic_file)
        img.convert("RGB").save(jpg_file, "JPEG")
        print("Conversion successful!")
    except Exception as e:
        print(f"Conversion failed: {str(e)}")

# Usage example
convert_heic_to_jpg(r"C:\Users\PRITHWISH\Desktop\test\20210908_125701.heic", "output_image.jpg")
