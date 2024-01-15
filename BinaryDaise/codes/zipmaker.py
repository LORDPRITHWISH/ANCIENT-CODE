import zipfile
import os
import tqdm

# Paths to the files you want to include in the zip
# file_paths = ['file1.txt', 'file2.txt', 'image.jpg']

filename='test'

input_folder='raw'
output_zip_path = f'zippy\\{filename}.zip'
# print(files)

files=[r'C:\Users\PRITHWISH\Desktop\appstore.png',r'C:\Users\PRITHWISH\Desktop\madness.png']

# files=[]
def address():  
    files=os.listdir(input_folder)
    for i,nam in enumerate(files):
        files[i]=os.path.join(input_folder,nam)

# print(files)

# Path to the output zip file

def zipp():
    with zipfile.ZipFile(output_zip_path, 'w') as zip_ref:
        for file_path in tqdm.tqdm(files):
            zip_ref.write(file_path)

    print(f"Successfully created {output_zip_path}")



# address()
zipp()