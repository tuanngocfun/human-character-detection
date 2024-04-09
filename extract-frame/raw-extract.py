import os
import cv2
from PIL import Image

class FrameExtractor:
    def __init__(self, src_folder, dst_folder):
        self.src_folder = src_folder
        self.dst_folder = dst_folder
        os.makedirs(self.dst_folder, exist_ok=True)

    @staticmethod
    def _save_frame(frame, dst_folder, frame_count, video_file_name):
        frame.save(os.path.join(dst_folder, f"{video_file_name}_frame_{frame_count}.jpg"))

    def _extract_frames(self, video_path, video_file_name):
        if self._frame_exists(video_file_name):
            return

        cap = cv2.VideoCapture(video_path)
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            self._save_frame(pil_image, self.dst_folder, frame_count, video_file_name)
            frame_count += 1

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

# Usage example
src_folder = '../../dataset/preprocessing-train-set/merge-for-train-set/merge-anime-videos'
dst_folder = '../../dataset/preprocessing-train-set/merge-for-train-set/extract-anime/filter-anime-frame'

# Initialize and use the frame extractor
extractor = FrameExtractor(src_folder, dst_folder)
extractor.extract_frames_from_directory()