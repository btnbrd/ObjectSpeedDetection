# Electric Scooter Detection and Tracking System

---

## Overview
This project provides an end-to-end solution to address the challenge of monitoring electric scooters in urban environments. The system leverages advanced deep learning models for detection, tracking, speed evaluation, and license plate recognition. It aims to automate the process of identifying rule violations and issuing fines efficiently.

---

## Features
1. **Detection**:  
   - Utilizes a YOLO-based object detection model to identify electric scooters in video streams.

2. **Tracking**:  
   - Implements tracking algorithms (e.g., ByteTrack or BoT-SORT) to monitor scooter movement over time.

3. **Speed Evaluation**:  
   - Calculates the speed of each scooter based on tracked positions and timestamps.

4. **License Plate Recognition**:  
   - Extracts and recognizes license plate numbers using OCR (Optical Character Recognition) techniques for fine issuance.

---

## Requirements
### Dependencies:
- Python 3.8+
- Required libraries:
  ```bash
  pip install torch torchvision ultralytics opencv-python-headless numpy
  ```
## Pre-trained Models:
- Detection Model: RT-DETR or YOLOv8 (ensure the .pt weights file is available).
License Plate Recognition Model: EasyOCR or equivalent OCR library.
## Hardware:
- NVIDIA GPU with CUDA support for faster processing (recommended).

## Setup
Clone the repository:

```bash
  git clone https://github.com/your-repo/electric-scooter-detection.git
  cd electric-scooter-detection
```
Prepare the environment:

```bash

python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
```

Add the pre-trained weights:

Place the detection_model.pt and ocr_model files in the models/ directory.
Run the script:

```bash

python scooter_detection.py --input your_video.mp4 --output result.mp4
```

## Pipeline Workflow
### Detection:

The YOLO model processes each frame to detect scooters.
Bounding boxes are generated around detected objects.
Tracking:

### Objects are assigned unique IDs and tracked across frames.
Path coordinates are recorded for speed estimation.
Speed Estimation:

### The distance covered between frames is used to calculate speed, using real-world calibration metrics.
License Plate Recognition:

### When a scooter is detected, its bounding box is cropped and passed to the OCR model for license plate recognition.
Fine Issuance:

- If a speed violation or other infractions are detected, the license plate number is logged for issuing fines.

# Future Improvements
### Increase the Real-Time Processing accuracy:
Better finetune model

### Enhanced License Plate Recognition:
Improve OCR accuracy under low light and motion blur conditions.



# Installation
```
docker build -t tracker_proj .
```
```
docker build -t tracker_proj .
```

```
docker run --rm -it  \
           --gpus all  \
           -p 8888:8888  \
           -v "$(pwd)/src:/app"  \
           tracker_proj
           
```

```
streamlit run main.py --server.port 8888
```
