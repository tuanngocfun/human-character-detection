import os
import re
import shutil
import random

image_src_dir = "/media/ngoc/a normal usb/ngoc/training-set/aggregate4-upscale-low-quality/images"
label_src_dir = "/media/ngoc/a normal usb/ngoc/training-set/aggregate4-upscale-low-quality/labels"

dest_dir = "/media/ngoc/a normal usb/ngoc/training-set/120-aggregate4-upscale-low-quality-random"

image_dest_dir = os.path.join(dest_dir, 'images')
label_dest_dir = os.path.join(dest_dir, 'labels')

os.makedirs(image_dest_dir, exist_ok=True)
os.makedirs(label_dest_dir, exist_ok=True)

jpg_files = os.listdir(image_src_dir)
txt_files = os.listdir(label_src_dir)

selected_jpg_files = random.sample(jpg_files, min(120, len(jpg_files)))

selected_txt_files = [f.replace('.jpg', '.txt') for f in selected_jpg_files]

for txt in selected_txt_files:
    if txt not in txt_files:
        print(f"Warning: Label file {txt} not found.")
        
for jpg, txt in zip(selected_jpg_files, selected_txt_files):
    shutil.copy(os.path.join(image_src_dir, jpg), os.path.join(image_dest_dir, jpg))
    if os.path.exists(os.path.join(label_src_dir, txt)):
        shutil.copy(os.path.join(label_src_dir, txt), os.path.join(label_dest_dir, txt))
