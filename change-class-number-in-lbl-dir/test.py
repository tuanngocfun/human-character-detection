import os

def process_file(filepath):
    lines = []
    with open(filepath, 'r') as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 0:
            continue
        class_id = parts[0]
        if class_id == "14":
            parts[0] = "0"
        updated_lines.append(" ".join(parts))

    with open(filepath, 'w') as f:
        f.write("\n".join(updated_lines))

def process_directory(directory_path):
    for subdir, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                process_file(os.path.join(subdir, file))

if __name__ == "__main__":
    directory_path = '/media/ngoc/a normal usb/ngoc/training-set/voc2007-label/labels'
    process_directory(directory_path)
