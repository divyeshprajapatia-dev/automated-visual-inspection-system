# Automated Visual Inspection & Event Detection System

## Overview
This project is a real-time computer vision–based automated inspection system built using Python and YOLOv8.  
It performs object detection on images, videos, and live webcam feeds, converts continuous frame-level detections into meaningful events, and logs those events in a structured JSON format.

The system is designed to simulate a perception and automation module commonly used in robotics, surveillance, and industrial inspection systems.

---

## Key Features
- Real-time object detection using YOLOv8
- Supports image, video, and live webcam input
- State-based event detection (prevents duplicate logging)
- Structured and fault-tolerant JSON logging
- Modular, production-oriented code architecture
- Clear separation between perception, decision logic, and control flow

---

## System Architecture

Input (Image / Video / Webcam)  
↓  
YOLOv8 Perception Module  
↓  
Detection Filtering (Confidence Threshold)  
↓  
State-Based Event Detection  
↓  
Structured JSON Logging  



This architecture reflects how real-world computer vision systems are designed in robotics and automation pipelines.

---

## Technology Stack
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy

---

## Project Structure

automated-visual-inspection-system/  
├── src/  
│ ├── image_processor.py # Image-based detection pipeline  
│ ├── video_processor.py # Video & webcam detection pipeline  
│ ├── event_manager.py # State-based event detection logic  
│ ├── logger.py # Robust JSON logging module  
│  
├── config/  
│ └── config.yaml # Configuration parameters  
│  
├── outputs/  
│ ├── images/ # Processed image outputs  
│ ├── videos/ # Processed video outputs  
│ └── logs/ # Detection & event logs  
│  
├── main.py # Application entry point (controller)  
├── requirements.txt   
└── README.md  


---

## Event Detection Logic
Raw object detections occur on every frame and can repeat continuously while an object remains visible.  
To avoid duplicate alerts and noisy logs, this system implements **state-based event detection**.

An object is logged as an event only when:
- It appears and persists in the scene for a minimum duration
- It has not already been logged during the same presence
- It disappears and reappears to trigger a new event

This approach converts continuous detections into discrete, meaningful system events and mirrors behavior used in industrial vision and automation systems.

---

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Image Detection
Place an image in the project root (e.g. test.jpg) and run:

```bash
python main.py
(Set MODE = "image" in main.py)
```
3. Webcam Detection

Set MODE = "webcam" in main.py and run:
```bash
python main.py
```
Press Q to exit the live detection window.

---

## Output
  - Annotated images or real-time video frames with bounding boxes
  - Structured JSON logs containing:
    - Timestamp
    - Input source
    - Object class
    - Confidence score
   
---

## Use Cases
  - Robotics perception modules
  - Automated visual inspection systems
  - Surveillance and monitoring
  - Computer vision–based event tracking
  - AI-powered automation pipelines

---

## Future Improvements
  - Configuration-driven rule engine
  - REST API integration
  - Object tracking and re-identification
  - Database-backed logging
  - Alert and notification hooks

---

## Author
Developed as a production-oriented computer vision and automation project, with a focus on clean architecture, system behaviour, and real-world applicability.  
### Made By Divyesh Prajapati
