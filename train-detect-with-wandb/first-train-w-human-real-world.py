import subprocess
import wandb

wandb_run = wandb.init(project="human-real-world", entity='tuanngoc')

cmd = """
yolo task=detect mode=train \
  model=/home/aivn12gb/yolov8_domain_adaption_evn/set-for-train-human-real-world/Human-real-world/train4/weights/best.pt \
  data=/home/aivn12gb/yolov8_domain_adaption_evn/set-for-train-human-real-world/Human-real-world/human-data/human_detection_dataset/data.yaml \
  epochs=135 imgsz=640 device=0 cache=True workers=24 save_period=30
"""

process = subprocess.Popen(cmd, shell=True)
process.wait()

wandb_run.finish()
