import os
import xml.etree.ElementTree as ET
from PIL import Image

def convert_yolo_to_xml(yolo_file, xml_file, image_path, class_names):
    with Image.open(image_path) as img:
        width, height = img.size

    root = ET.Element('annotation')
    ET.SubElement(root, 'folder').text = os.path.dirname(image_path)
    ET.SubElement(root, 'filename').text = os.path.basename(image_path)
    ET.SubElement(root, 'path').text = image_path

    source = ET.SubElement(root, 'source')
    ET.SubElement(source, 'database').text = 'Unknown'

    size = ET.SubElement(root, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = '3'

    ET.SubElement(root, 'segmented').text = '0'

    with open(yolo_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            class_index, x_center, y_center, obj_width, obj_height = map(float, parts)

            obj_class = class_names[int(class_index)]
            x_min = (x_center - obj_width / 2) * width
            y_min = (y_center - obj_height / 2) * height
            x_max = (x_center + obj_width / 2) * width
            y_max = (y_center + obj_height / 2) * height

            obj = ET.SubElement(root, 'object')
            ET.SubElement(obj, 'name').text = obj_class
            ET.SubElement(obj, 'pose').text = 'Unspecified'
            ET.SubElement(obj, 'truncated').text = '0'
            ET.SubElement(obj, 'difficult').text = '0'

            bndbox = ET.SubElement(obj, 'bndbox')
            ET.SubElement(bndbox, 'xmin').text = str(int(x_min))
            ET.SubElement(bndbox, 'ymin').text = str(int(y_min))
            ET.SubElement(bndbox, 'xmax').text = str(int(x_max))
            ET.SubElement(bndbox, 'ymax').text = str(int(y_max))

    tree = ET.ElementTree(root)
    tree.write(xml_file)


path_to_labels = '/home/aivn12gb/yolov8_domain_adaption_evn/data/new-val/labels'
class_names = ['Human']

for file_name in os.listdir(path_to_labels):
    if file_name.endswith('.txt'):
        base_name = os.path.splitext(file_name)[0]
        yolo_file = os.path.join(path_to_labels, file_name)
        xml_file = os.path.join(path_to_labels, base_name + '.xml')
        image_path = os.path.join('/home/aivn12gb/yolov8_domain_adaption_evn/data/new-val/images', base_name + '.jpg')

        convert_yolo_to_xml(yolo_file, xml_file, image_path, class_names)
        print(f'Converted {yolo_file} to {xml_file}')
