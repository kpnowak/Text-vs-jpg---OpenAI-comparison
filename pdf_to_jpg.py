from pdf2image import convert_from_path
import os

# Function to convert PDF to JPG
def pdf_to_jpg(pdf_path, output_folder):
    # Convert PDF to list of images
    images = convert_from_path(pdf_path)

    # Iterate through the images and save each one as a JPG file
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i + 1}.jpg')
        image.save(image_path, 'JPEG')
        print(f'Saved: {image_path}')

# Example usage
pdf_path = 'Docs_to_review/Find mistakes 1.pdf'
output_folder = 'jpgs_to_review'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

pdf_to_jpg(pdf_path, output_folder)
