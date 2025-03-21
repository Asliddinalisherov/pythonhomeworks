import numpy as np
from PIL import Image

# Function to flip the image horizontally and vertically
def flip_image(img_array):
    return np.flip(img_array, axis=(0, 1))

# Function to add random noise to the image
def add_noise(img_array, intensity=25):
    noise = np.random.randint(-intensity, intensity, img_array.shape, dtype=np.int16)
    noisy_img = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    return noisy_img

# Function to brighten the channels by a fixed value
def brighten_channels(img_array, value=40):
    brightened_img = np.clip(img_array + value, 0, 255).astype(np.uint8)
    return brightened_img

# Function to apply a mask to a rectangular region
def apply_mask(img_array, x, y, width, height):
    masked_img = img_array.copy()
    masked_img[y:y+height, x:x+width] = [0, 0, 0]
    return masked_img

# Load the image using PIL
image_path = 'images/birds.jpg'
image = Image.open(image_path)
img_array = np.array(image)

# Perform the manipulations
flipped_img = flip_image(img_array)
noisy_img = add_noise(flipped_img)
brightened_img = brighten_channels(noisy_img)
masked_img = apply_mask(brightened_img, x=100, y=100, width=100, height=100)

# Convert the modified NumPy array back to an image
modified_image = Image.fromarray(masked_img)

# Save the modified image
modified_image.save('modified_birds.jpg')

print("Image manipulations completed and saved as 'modified_birds.jpg'.")