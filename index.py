import numpy as np
import imageio.v2 as imageio
import os

output_folder = './uploads'
os.makedirs(output_folder, exist_ok=True)

channel_folders = ['red', 'green', 'blue', 'grayscale', 'binary_threshold']
for folder in channel_folders:
    os.makedirs(os.path.join(output_folder, folder), exist_ok=True)

def save_image(image, base_name, suffix, output_folder):
    output_path = os.path.join(output_folder, suffix, f"{base_name}_{suffix}.png")
    imageio.imwrite(output_path, image)
    print(f"Gambar disimpan: {output_path}")

def process_image(image_path):
    img = imageio.imread(image_path)

    if img.ndim == 2:
        print("Gambar harus berwarna (RGB).")
        return
    
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    red_channel = img.copy()
    red_channel[:, :, 1] = 0  
    red_channel[:, :, 2] = 0  
    save_image(red_channel, base_name, 'red', output_folder)

    green_channel = img.copy()
    green_channel[:, :, 0] = 0  
    green_channel[:, :, 2] = 0  
    save_image(green_channel, base_name, 'green', output_folder)

    blue_channel = img.copy()
    blue_channel[:, :, 0] = 0  
    blue_channel[:, :, 1] = 0 
    save_image(blue_channel, base_name, 'blue', output_folder)

    grayscale = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])  
    save_image(grayscale.astype(np.uint8), base_name, 'grayscale', output_folder)

    threshold_value = 128
    binary_threshold = (grayscale > threshold_value) * 255 
    binary_threshold = binary_threshold.astype(np.uint8)
    save_image(binary_threshold, base_name, 'binary_threshold', output_folder)

image_paths = ['./images/Daun-Pepaya.jpg', './images/Daun-Kenikir.jpg', './images/Daun-Singkong.jpg']

for image_path in image_paths:
    process_image(image_path)