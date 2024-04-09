import os
import cv2
import numpy as np
from PIL import Image, ImageChops

class FrameExtractor:
    def __init__(self, src_folder, dst_folder, frame_diff_threshold, cos_sim_threshold, interval_ms):
        self.src_folder = src_folder
        self.dst_folder = dst_folder
        self.frame_diff_threshold = frame_diff_threshold
        self.cos_sim_threshold = cos_sim_threshold
        self.interval_ms = interval_ms
        os.makedirs(self.dst_folder, exist_ok=True)

    @staticmethod
    def _feature_vector(image):
        # Convert image to grayscale, resize, and flatten it
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(image_gray, (64, 64)).flatten()
        norm = np.linalg.norm(resized_image)
        if norm == 0:
            return resized_image  # Handle the all-zero vector case
        return resized_image / norm  # Normalize the feature vector

    @staticmethod
    def _cosine_similarity(vec1, vec2):
        # Compute cosine similarity manually using numpy
        dot_product = np.dot(vec1, vec2)
        norm_a = np.linalg.norm(vec1)
        norm_b = np.linalg.norm(vec2)
        if norm_a == 0 or norm_b == 0:
            # If either vector has no magnitude, they are not similar at all.
            return 0.0
        return dot_product / (norm_a * norm_b)

    @staticmethod
    def _process_frame(frame, prev_pil_image, prev_feature_vector, cos_sim_threshold, frame_diff_threshold):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)
        current_feature_vector = FrameExtractor._feature_vector(frame_rgb)

        if prev_feature_vector is None:
            return pil_image, current_feature_vector, True

        diff = ImageChops.difference(pil_image, prev_pil_image) if prev_pil_image else None
        percentage_diff = np.mean(np.array(diff)) / 255 if diff else 0

        cos_sim = FrameExtractor._cosine_similarity(prev_feature_vector, current_feature_vector)
        should_save = cos_sim < cos_sim_threshold or percentage_diff > frame_diff_threshold

        return pil_image, current_feature_vector, should_save

    @staticmethod
    def _save_frame(frame, dst_folder, frame_count, video_file_name):
        frame.save(os.path.join(dst_folder, f"{video_file_name}_frame_{frame_count}.jpg"))

    def _extract_frames(self, video_path, video_file_name):
        if self._frame_exists(video_file_name):
            return

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        skip_frames = int(fps * (self.interval_ms / 1000))

        prev_pil_image = prev_feature_vector = None
        frame_count = total_frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if total_frame_count % skip_frames == 0:
                pil_image, current_feature_vector, should_save = self._process_frame(
                    frame, prev_pil_image, prev_feature_vector, self.cos_sim_threshold, self.frame_diff_threshold
                )
                if should_save:
                    self._save_frame(pil_image, self.dst_folder, frame_count, video_file_name)
                    frame_count += 1
                prev_pil_image, prev_feature_vector = pil_image, current_feature_vector

            total_frame_count += 1

        cap.release()

    def _frame_exists(self, video_file_name):
        frame_files = os.listdir(self.dst_folder)
        return any(video_file_name in frame_file for frame_file in frame_files)

    def extract_frames_from_directory(self):
        video_files = [f for f in os.listdir(self.src_folder) if os.path.isfile(os.path.join(self.src_folder, f)) and f.endswith('.mp4')]

        for video_file in video_files:
            video_path = os.path.join(self.src_folder, video_file)
            video_file_name = os.path.splitext(video_file)[0]
            self._extract_frames(video_path, video_file_name)

src_folder = '../../dataset/preprocessing-train-set/anime/filter-vid15'
dst_folder = '../../dataset/preprocessing-train-set/cosine-similarity-extract/extract-anime/filter-anime-frame15'
frame_diff_threshold = 0.1  
cos_sim_threshold = 0.1  
interval_ms = 200  

extractor = FrameExtractor(src_folder, dst_folder, frame_diff_threshold, cos_sim_threshold, interval_ms)
extractor.extract_frames_from_directory()
