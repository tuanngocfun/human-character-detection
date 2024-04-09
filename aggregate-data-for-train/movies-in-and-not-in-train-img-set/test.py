import os
import shutil

def main():
    image_dir_path = "/media/ngoc/a normal usb/ngoc/training-set/aggregate4/images"
    anime_video_dir_path = "/media/ngoc/a normal usb/ngoc-data-thesis/videos/train/anime"
    cartoon_video_dir_path = "/media/ngoc/a normal usb/ngoc-data-thesis/videos/train/cartoon"

    target_dir_not_in_train = "/media/ngoc/a normal usb/ngoc-data-thesis/videos/movies-not-in-train-image-set"
    target_dir_in_train = "/media/ngoc/a normal usb/ngoc-data-thesis/videos/movies-in-train-image-set"

    # Create target directories if they don't exist
    if not os.path.exists(target_dir_not_in_train):
        os.makedirs(target_dir_not_in_train)
    if not os.path.exists(target_dir_in_train):
        os.makedirs(target_dir_in_train)

    # Collect names of image files
    image_names = set()
    for file in os.listdir(image_dir_path):
        if file.endswith(".jpg"):
            # Extract name portion between first underscore and '_frame_'
            relevant_name_part = file.split("_")[1:-2]
            relevant_name = "_".join(relevant_name_part)
            image_names.add(relevant_name)

    # Function to process video files
    def process_videos(video_dir_path):
        for file in os.listdir(video_dir_path):
            if file.endswith(".mp4"):
                # Extract name portion without .mp4
                base_name = file.rsplit(".mp4", 1)[0]
                source = os.path.join(video_dir_path, file)

                if base_name in image_names:
                    shutil.copy(source, os.path.join(target_dir_in_train, file))
                else:
                    shutil.copy(source, os.path.join(target_dir_not_in_train, file))

    # Process anime and cartoon directories
    process_videos(anime_video_dir_path)
    process_videos(cartoon_video_dir_path)

if __name__ == "__main__":
    main()
