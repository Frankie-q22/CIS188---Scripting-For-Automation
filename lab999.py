import zipfile

countJPG = 0
countPDF = 0

with zipfile.ZipFile('C:/Users/Frank/Downloads/files.zip','r') as my_zip:
    print(my_zip.namelist())
    my_zip.extractall('files')
    
import os
import shutil
from pathlib import Path

# Function to move files to the specified directories
def move_files(src_dir, dest_pdf_dir, dest_images_dir):
    for subdir, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith('.pdf'):
                shutil.move(os.path.join(subdir, file), os.path.join(dest_pdf_dir, file))
            elif file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                shutil.move(os.path.join(subdir, file), os.path.join(dest_images_dir, file))

# Create the PDF and images directories
pdf_dir = 'PDF'
images_dir = 'images'
os.makedirs(pdf_dir, exist_ok=True)
os.makedirs(images_dir, exist_ok=True)

# Assuming the zip file is already extracted, replace 'extracted_folder' with the actual path
source_directory = ':/Users/Frank/Downloads/files'

# Move files to the respective directories
move_files(source_directory, pdf_dir, images_dir)

# Print the directory listings
print(f'\nPDF Directory Listing:')
print('\n'.join(sorted(os.listdir(pdf_dir))))

print(f'\nImages Directory Listing:')
print('\n'.join(sorted(os.listdir(images_dir))))

# Print the total number of files
pdf_files_count = len(os.listdir(pdf_dir))
images_files_count = len(os.listdir(images_dir))
print(f'\nTotal PDF Files: {pdf_files_count}')
print(f'Total Image Files: {images_files_count}')