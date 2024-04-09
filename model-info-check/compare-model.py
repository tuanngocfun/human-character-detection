import torch

def load_model(path):
    checkpoint = torch.load(path, map_location=torch.device('cpu'))
    return checkpoint

def compare_models(model1_path, model2_path):
    model1_checkpoint = load_model(model1_path)
    model2_checkpoint = load_model(model2_path)

    if 'model' in model1_checkpoint and 'model' in model2_checkpoint:
        model1_state_dict = model1_checkpoint['model'].state_dict()
        model2_state_dict = model2_checkpoint['model'].state_dict()
    else:
        model1_state_dict = model1_checkpoint
        model2_state_dict = model2_checkpoint

    # Check if the models are identical
    for (key1, param1), (key2, param2) in zip(model1_state_dict.items(), model2_state_dict.items()):
        if isinstance(param1, torch.Tensor) and isinstance(param2, torch.Tensor):
            if torch.equal(param1, param2):
                print(f"Parameter {key1} is the same for both models")
            else:
                print(f"Parameter {key1} is different between the models")
        else:
            if param1 == param2:
                print(f"Non-tensor parameter {key1} is the same for both models")
            else:
                print(f"Non-tensor parameter {key1} is different between the models")

    # Print all keys and their values from the checkpoints
    print("\nKeys and their values in the checkpoint for Model 1:")
    for key, value in model1_checkpoint.items():
        if key not in ['model', 'ema', 'optimizer']:  # Exclude large data structures
            print(f"{key}: {value}")

    print("\nKeys and their values in the checkpoint for Model 2:")
    for key, value in model2_checkpoint.items():
        if key not in ['model', 'ema', 'optimizer']:  # Exclude large data structures
            print(f"{key}: {value}")

#model1_path = '/media/ngoc/a normal usb/ngoc/weights/train20/weights/best.pt'
model1_path = '/media/ngoc/mydisk/ngoc/thesis/weight-train/human-real-world/best.pt'
#model2_path = '/media/ngoc/a normal usb/ngoc/weights/train19/weights/best.pt'
model2_path = '/media/ngoc/mydisk/ngoc/thesis/weight-train/yolov8-model/yolov8x.pt'

compare_models(model1_path, model2_path)
