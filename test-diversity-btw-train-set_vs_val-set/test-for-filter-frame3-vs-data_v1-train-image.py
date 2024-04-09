import glob
import numpy as np
from matplotlib.patches import Circle
from keras.applications import VGG16
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from scipy.spatial import distance

def get_model():
    model = VGG16()
    return Model(inputs=model.inputs, outputs=model.layers[-2].output)

def extract_features(image_path, model):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    feature = model.predict(image)
    return feature.flatten()

def get_features_from_folder(folder_path, model):
    features = [extract_features(file_path, model) for file_path in glob.glob(folder_path + '/*.jpg')]
    return np.array(features)

def calculate_overlap(train_points, valid_points, r):
    overlap_count = 0
    for valid_point in valid_points:
        min_dist = min(distance.euclidean(valid_point, train_point) for train_point in train_points)
        if min_dist <= r:
            overlap_count += 1
            
    return (overlap_count / len(valid_points)) * 100

model = get_model()
train_features = get_features_from_folder('/home/aivn12gb/yolov8_domain_adaption_evn/data_v1/train/images', model)
valid_features = get_features_from_folder('/home/aivn12gb/yolov8_domain_adaption_evn/filter-frame3', model)

# Concatenate the features
all_features = np.concatenate((train_features, valid_features))

# Apply t-SNE
tsne = TSNE(n_components=2, random_state=42)
reduced_features = tsne.fit_transform(all_features)

# Separate the transformed features
train_reduced = reduced_features[:len(train_features)]
valid_reduced = reduced_features[len(train_features):]

# Calculate overlap percentage
r = 0.5 # Example radius
overlap_percentage = calculate_overlap(train_reduced, valid_reduced, r)
print(f"Overlap Percentage: {overlap_percentage}%")

# Plot scatter with circles around training points
plt.scatter(train_reduced[:, 0], train_reduced[:, 1], c='b', label='Training')
plt.scatter(valid_reduced[:, 0], valid_reduced[:, 1], c='r', label='Validation')

for train_point in train_reduced:
    plt.gca().add_patch(Circle(train_point, r, fill=False, edgecolor='b'))

plt.legend(loc='upper right')
plt.show()

# Plot a histogram of distances
all_distances = [distance.euclidean(valid_point, train_point) for valid_point in valid_reduced for train_point in train_reduced]
plt.hist(all_distances, bins=30)
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.show()