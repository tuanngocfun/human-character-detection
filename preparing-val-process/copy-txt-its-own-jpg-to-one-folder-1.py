import os
import shutil

# Initialize source and target directories
source_img_dir = '/media/ngoc/a normal usb/ngoc/new-val/labelimage3/transfer-done-val5/images'
source_txt_dir = '/media/ngoc/a normal usb/ngoc/new-val/val5-standard/labels'
target_dir = '/media/ngoc/a normal usb/ngoc/new-val/labelimage3/lbl-img-style-transfer1'

# Create target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Helper function to strip "_out" from .jpg filenames
def strip_out_from_filename(filename):
    return filename.replace("_out", "")

# Gather lists of existing .jpg and .txt files
source_img_files = [f for f in os.listdir(source_img_dir) if f.endswith('.jpg')]
source_txt_files = [f for f in os.listdir(source_txt_dir) if f.endswith('.txt')]

# Curate the .jpg file names to have the same name as .txt files (remove "_out")
curated_img_files = [strip_out_from_filename(f) for f in source_img_files]

# Dictionary to keep track of copied files
copied_files = {'jpg': set(), 'txt': set()}

# Copy matching .jpg files
for f in curated_img_files:
    if f.replace('.jpg', '.txt') in source_txt_files:
        shutil.copy(os.path.join(source_img_dir, f.replace(".jpg", "_out.jpg")), os.path.join(target_dir, f))
        copied_files['jpg'].add(f)

# Copy matching .txt files
for f in source_txt_files:
    if f.replace('.txt', '.jpg') in curated_img_files:
        shutil.copy(os.path.join(source_txt_dir, f), os.path.join(target_dir, f))
        copied_files['txt'].add(f)

# Remove extraneous .jpg and .txt files in the target directory
for f in os.listdir(target_dir):
    ext = f.split('.')[-1]
    if ext == 'jpg' and f not in copied_files['jpg']:
        os.remove(os.path.join(target_dir, f))
    elif ext == 'txt' and f not in copied_files['txt']:
        os.remove(os.path.join(target_dir, f))

# Double-check that each .jpg has a corresponding .txt and vice versa
final_img_files = [f for f in os.listdir(target_dir) if f.endswith('.jpg')]
final_txt_files = [f for f in os.listdir(target_dir) if f.endswith('.txt')]

assert all(f.replace('.jpg', '.txt') in final_txt_files for f in final_img_files)
assert all(f.replace('.txt', '.jpg') in final_img_files for f in final_txt_files)

print("Files successfully copied and curated.")

