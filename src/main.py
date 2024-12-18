import cv2
import tempfile
import streamlit as st
from ultralytics import RTDETR
import os

# Streamlit App Title
st.title("YOLO Video Processing with Streamlit")

# Upload video file
uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

# Load YOLO model
model_path = "rtdetr.pt"
model = RTDETR(model_path)  # Load model

trackers = ['botsort.yaml', 'bytetrack.yaml']

if uploaded_video is not None:
    # Save uploaded video to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_input:
        temp_input.write(uploaded_video.read())
        input_path = temp_input.name

    # Create temporary output path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_output:
        output_path = temp_output.name

    # Process video
    cap = cv2.VideoCapture(input_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('tmp.mp4', fourcc, fps, (frame_width, frame_height))

    # Display progress bar
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    progress_bar = st.progress(0)

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO Detection
        results = model.track(frame, tracker=trackers[1], conf=0.6, iou=0.5, persist=True)

        # Annotate frame
        annotated_frame = results[0].plot()

        # Write annotated frame to output video
        out.write(annotated_frame)

        # Update progress bar
        frame_count += 1
        progress_bar.progress(frame_count / total_frames)

    # Release resources
    cap.release()
    out.release()

    os.system('ffmpeg -i {} -vcodec libx264 {} -y'.format('tmp.mp4', output_path))
    os.remove('tmp.mp4')
    # Display output video
    st.success("Processing complete!")
    st.video(output_path)
else:
    st.warning("Please upload a video file to start processing.")
