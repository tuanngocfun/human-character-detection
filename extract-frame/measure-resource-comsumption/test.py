import os
import cv2
import imagehash
import numpy as np
import psutil
import time
from PIL import Image, ImageChops

class FrameExtractor:
    def __init__(self, src_folder, dst_folder, frame_diff_threshold, hash_diff_threshold, interval_ms):
        self.src_folder = src_folder
        self.dst_folder = dst_folder
        self.frame_diff_threshold = frame_diff_threshold
        self.hash_diff_threshold = hash_diff_threshold
        self.interval_ms = interval_ms
        os.makedirs(self.dst_folder, exist_ok=True)

    @staticmethod
    def _image_hash(image):
        return imagehash.average_hash(image)

    @staticmethod
    def _hash_diff(hash1, hash2):
        return hash1 - hash2

    @staticmethod
    def _process_frame(frame, prev_pil_image, prev_hash, hash_diff_threshold, frame_diff_threshold):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)
        current_hash = FrameExtractor._image_hash(pil_image)

        if prev_hash is None:
            return pil_image, current_hash, True

        diff = ImageChops.difference(pil_image, prev_pil_image) if prev_pil_image else None
        percentage_diff = np.mean(np.array(diff)) / 255 if diff else 0

        should_save = FrameExtractor._hash_diff(prev_hash, current_hash) > hash_diff_threshold or \
                      percentage_diff > frame_diff_threshold

        return pil_image, current_hash, should_save

    @staticmethod
    def _save_frame(frame, dst_folder, frame_count, video_file_name):
        frame.save(os.path.join(dst_folder, f"{video_file_name}_frame_{frame_count}.jpg"))

    def _extract_frames(self, video_path, video_file_name):
        if self._frame_exists(video_file_name):
            return

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        skip_frames = int(fps * (self.interval_ms / 1000))

        prev_pil_image = prev_hash = None
        frame_count = total_frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if total_frame_count % skip_frames == 0:
                pil_image, current_hash, should_save = self._process_frame(
                    frame, prev_pil_image, prev_hash, self.hash_diff_threshold, self.frame_diff_threshold)
                if should_save:
                    self._save_frame(pil_image, self.dst_folder, frame_count, video_file_name)
                    frame_count += 1
                prev_pil_image, prev_hash = pil_image, current_hash

            total_frame_count += 1

        cap.release()

    def _frame_exists(self, video_file_name):
        frame_files = os.listdir(self.dst_folder)
        return any(video_file_name in frame_file for frame_file in frame_files)

    def extract_frames_from_directory(self):
        video_files = [f for f in os.listdir(self.src_folder) if os.path.isfile(os.path.join(self.src_folder, f)) and f.endswith('.mp4')]

        # Start measuring resources
        start_time = time.time()
        start_cpu = psutil.cpu_percent(interval=None)
        process = psutil.Process(os.getpid())
        start_ram = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB

        for video_file in video_files:
            video_path = os.path.join(self.src_folder, video_file)
            video_file_name = os.path.splitext(video_file)[0]
            self._extract_frames(video_path, video_file_name)

        # End measuring resources
        end_cpu = psutil.cpu_percent(interval=None)
        end_ram = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB
        end_time = time.time()

        # Calculate the resources used
        elapsed_time = end_time - start_time
        cpu_usage = end_cpu - start_cpu
        ram_usage = end_ram - start_ram

        print(f"Time taken: {elapsed_time} seconds")
        print(f"CPU usage: {cpu_usage} percent")
        print(f"RAM usage increase: {ram_usage} MB")


# Example usage
src_folder = "../../../dataset/preprocessing-train-set/cartoon/filter-vid5"
dst_folder = "../../../dataset/preprocessing-train-set/measure-resources/extract-cartoon/filter-cartoon-frame5"
frame_diff_threshold = 0.1
hash_diff_threshold = 5
interval_ms = 200

# Instantiate and use the FrameExtractor
extractor = FrameExtractor(src_folder, dst_folder, frame_diff_threshold, hash_diff_threshold, interval_ms)
extractor.extract_frames_from_directory()
