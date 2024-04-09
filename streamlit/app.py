import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import tempfile
import numpy as np

model = YOLO('/media/ngoc/mydisk/ngoc/thesis/experiment/Evaluate-Model/manually-label-120-imgs/partially-upscale-best-weight-val-4196_test-on4482/weight-evaluate-on-4482/best.pt')  

st.title("Application to Human Animated Movies")

uploaded_file = st.file_uploader("Upload an image or video...", type=["jpg", "png", "mp4"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    if uploaded_file.type == "video/mp4":
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_file.read())
        vid = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        while vid.isOpened():
            ret, frame = vid.read()
            if not ret:
                break

            results = model.predict(source=frame)

            result_frame = results.render()[0]

            stframe.image(result_frame, caption='Processed Frame', use_column_width=True)
    else:
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        results = model.predict(source=image)

        result_image = results.render()[0]

        st.image(result_image, caption='Processed Image', use_column_width=True)

st.write("Upload an image or video to get started!")
