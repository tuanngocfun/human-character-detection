import subprocess
import wandb

wandb_run = wandb.init(project="start-with-human-animation-standard-data", entity='tuanngoc')

cmd = """
yolo task=detect mode=train \
  model="/media/ngoc/a normal usb/ngoc/weights/train46/weights/best.pt" \
  data="/media/ngoc/a normal usb/ngoc/training-set/data.yaml" \
  epochs=135 imgsz=640 batch=18 device=0 cache=True workers=16 save_period=30
"""

process = subprocess.Popen(cmd, shell=True)
process.wait()

wandb_run.finish()
