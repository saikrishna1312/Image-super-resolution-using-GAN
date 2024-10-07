import os
from PIL import Image

# Function to downscale images and save the LR version
def downscale_image(input_folder, output_folder, scale_factor=4):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the folder if it doesn't exist
    
    # Loop through all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Ensure it's an image file
            img_path = os.path.join(input_folder, filename)
            
            # Open the high-resolution image
            hr_image = Image.open(img_path)
            
            # Get original dimensions
            width, height = hr_image.size
            
            # Calculate new dimensions (downscaled size)
            new_width = width // scale_factor
            new_height = height // scale_factor
            
            # Downscale the image using Bicubic interpolation
            lr_image = hr_image.resize((new_width, new_height), Image.BICUBIC)
            
            # Save the low-resolution image to the output folder
            output_path = os.path.join(output_folder, filename)
            lr_image.save(output_path)
            print(f"Saved downscaled image: {output_path}")

# Paths to the folders
hr_test_folder = 'train_HR'   # Folder containing 800 HR test images
lr_test_output_folder = 'train_LR'  # Folder to save downscaled LR images
hr_val_folder = 'val_HR'     # Folder containing 100 HR validation images
lr_val_output_folder = 'val_LR'    # Folder to save downscaled LR images

# Downscale the test and validation images
downscale_image(hr_test_folder, lr_test_output_folder, scale_factor=4)
downscale_image(hr_val_folder, lr_val_output_folder, scale_factor=4)