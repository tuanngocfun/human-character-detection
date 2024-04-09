import os
from PIL import Image

image_folder = '/home/aivn12gb/yolov8_domain_adaption_evn/data/new-val/images'

widths = []
heights = []
for image_name in os.listdir(image_folder):
    if image_name.endswith('.jpg'):
        image_path = os.path.join(image_folder, image_name)
        with Image.open(image_path) as img:
            width, height = img.size
            widths.append(width)
            heights.append(height)

unique_widths = set(widths)
unique_heights = set(heights)

print("Unique widths:", unique_widths)
print("Unique heights:", unique_heights)
