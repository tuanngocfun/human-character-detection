import wandb
from ultralytics import YOLO

# Initialize a new wandb run
wandb_run = wandb.init(project="new-val-detect1", entity='tuanngoc')

# Load the trained model
#model = YOLO('yolov8l.pt')
#model = YOLO('/media/ngoc/mydisk/ngoc/thesis/weight-train/animated-movies/kaggle-training/115-train-25-val-15-test/165-imgs-activ-learning-best.pt')
#model = YOLO('/media/ngoc/mydisk/ngoc/thesis/weight-train/human-real-world/train3/weights/best.pt')
model = YOLO('/media/ngoc/mydisk/ngoc/thesis/weight-train/human-real-world/best.pt')
# model = YOLO('/home/aivn12gb/yolov8_domain_adaption_evn/weight/human-real-world/best.pt') # human-real-world given highest result metrics, but labeling by coco human weight?
# model = YOLO('/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/train29/weights/best.pt')
# model = YOLO('/home/aivn12gb/yolov8_domain_adaption_evn/ultralytics/runs/detect/train46/weights/best.pt') # best human animation weight(note: first train)
# model = YOLO('/media/ngoc/a normal usb/ngoc/weights/train46/weights/best.pt') # best human animation weight(note: first train)
# Human-real-world active labeling weight
# model = YOLO('/home/aivn12gb/yolov8_domain_adaption_evn/weight/human-real-world/train5/weights/best.pt') # mAP50=0.82
# model = YOLO('/media/ngoc/a normal usb/ngoc/weights/voc2007/best-weight-voc2007/kaggle/working/ultralytics/runs/detect/train7/weights/best.pt');

# Define an image or a set of images for prediction
#images = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/not-labeled-by-first-detect/human-real-world-detect-here'
#images = '/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-1-style-transfer'
# images = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4/images' # this time i need to see whether the label is better or not with human-real-world active labeling...?
# images = '/media/ngoc/a normal usb/ngoc/training-set/aggregate4/images'
# images = '/home/aivn12gb/yolov8_domain_adaption_evn/adding-train-data-7-raw'
# images = '/home/aivn12gb/yolov8_domain_adaption_evn/merge-filter-frame-for-train-raw5'
# images = '/home/aivn12gb/yolov8_domain_adaption_evn/standard-data/aggregate4-retrain-subset/images'
# images = '/media/ngoc/a normal usb/ngoc/test-set2/extract-frame-combine'

# train set(redo data)
# images = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/extract-anime/combine-anime'
#images = '/media/ngoc/mydisk/ngoc/thesis/data-qualty-assessment/image-quality-assessment/test/train-set'

images = '/media/ngoc/mydisk/ngoc/thesis/dataset/preprocessing-train-set/dataset-of-hash-difference-first-time-merge-similarity'

# Run prediction
results = model.predict(images, stream=True, imgsz=640, save=True, save_txt=True, conf=0.9, iou=0.95, agnostic_nms=True) # conf=0.8 for human-real-world with active labeling, conf=0.25 for voc2007 weight

# Log results to wandb
for result_index, result in enumerate(results):
    boxes = result.boxes  # Boxes object for bbox outputs
    box_coords = boxes.xyxy  # box with xyxy format, (N, 4)
    
    for i in range(box_coords.shape[0]):
        x1, y1, x2, y2 = box_coords[i]  # Get bounding box coordinates
        class_id = boxes.cls[i]  # Get class id
        objectness_score = boxes.conf[i]  # Get confidence score
        
        # Log bounding box to wandb
        wandb.log({
            "image number": result_index, 
            "bounding box": {
                "position": {
                    "minX": x1.item(),
                    "maxX": x2.item(),
                    "minY": y1.item(),
                    "maxY": y2.item()
                },
                "class_id": class_id.item(),
                "box_caption": "Object",
                "domain": "pixel",
                "scores": {
                    "objectness_score": objectness_score.item(),
                }
            },
        })

# Finish the run
wandb_run.finish()
