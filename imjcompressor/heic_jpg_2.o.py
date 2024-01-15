from PIL import Image
import pyheif

def convert_heic_to_jpg(heic_file, jpg_file):
    try:
        heif_image = pyheif.read(heic_file)
        img = Image.frombytes(
            heif_image.mode, 
            heif_image.size, 
            heif_image.data,
            "raw",
            heif_image.mode,
            heif_image.stride,
        )
        img.convert("RGB").save(jpg_file, "JPEG")
        print("Conversion successful!")
    except Exception as e:
        print(f"Conversion failed: {str(e)}")

# Usage example
convert_heic_to_jpg(r"C:\Users\PRITHWISH\Desktop\test\20210908_125701.heic", "output_image.jpg")
