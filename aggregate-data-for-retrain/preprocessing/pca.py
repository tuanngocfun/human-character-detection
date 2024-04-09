import cv2
import os
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Function to load images from a specified directory
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

# Directory path
folder_path = '/home/aivn12s2/data/cosine-similarity-used-in-frame-extraction/pca/merge-cartoon'

# Load images
images = load_images_from_folder(folder_path)

# Ensure all images have the same dimensions (resize if necessary)
width, height = images[0].shape[1], images[0].shape[0]
images_resized = [cv2.resize(img, (width, height)) for img in images]

# Flatten the images
n_samples = len(images_resized)
data_flat = np.array([img.flatten() for img in images_resized])

# Set up PCA and the X vector for dimensionality reduction
n_components = 150
pca = PCA(n_components=n_components, whiten=True).fit(data_flat)

# Apply PCA transformation
data_pca = pca.transform(data_flat)

# Optionally inverse transform to visualize the dimensionality reduction
data_inv_transform = pca.inverse_transform(data_pca)
data_restored = data_inv_transform.reshape((n_samples, height, width, 3))

# Display some of the original images and the reconstructed images
fig, ax = plt.subplots(2, 10, figsize=(10, 2.5),
                        subplot_kw={'xticks':[], 'yticks':[]},
                        gridspec_kw=dict(hspace=0.1, wspace=0.1))

for i in range(10):  # Displaying only the first 10 images for brevity
    ax[0, i].imshow(cv2.cvtColor(images_resized[i], cv2.COLOR_BGR2RGB))
    ax[1, i].imshow(cv2.cvtColor(data_restored[i].astype(np.uint8), cv2.COLOR_BGR2RGB))

ax[0, 0].set_ylabel('full-dim\ninput')
ax[1, 0].set_ylabel(f'{n_components}-dim\nreconstruction');

plt.show()
