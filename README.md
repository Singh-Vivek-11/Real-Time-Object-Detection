# 🧠 Real-Time Object Detection System using YOLOv5, Flask & OpenCV

This project is a real-time object detection system built with **YOLOv5**, **Flask**, and **OpenCV**. It captures video from a webcam, performs object detection using a pre-trained YOLOv5 model, and streams the output to a web interface.

## 🔧 Features

- 🎥 Real-time video streaming via Flask web server.
- 🕵️‍♂️ Object detection using YOLOv5 (`yolov5s.pt` model).
- 💻 Compatible with both Linux and Windows platforms.
- 🌐 Lightweight HTML frontend with auto-retry on stream failure.
- 📦 Deployable on local machines, VMs, or cloud instances.

## 📁 Project Structure

├── app.py             # Flask app for web streaming
├── detect.py          # Standalone YOLOv5 detection script using OpenCV
├── index.html         # Frontend for live stream display
├── yolov5s.pt         # Pretrained YOLOv5 model (Ultralytics)
```

### Prerequisites

- Python 3.7+
- pip
- OpenCV (`cv2`)
- Flask
- PyTorch
- YOLOv5 dependencies

```bash
pip install flask torch torchvision opencv-python
```

### Run the Flask Server

```bash
python app.py
```

Open your browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### OR Run the Detection Script (Standalone)

```bash
python detect.py
```

## 🌩 Deployment Options

This system can be deployed on:

- Virtual machines (Ubuntu/Windows)
- Cloud platforms (Azure, AWS EC2, GCP)
- Containers (Docker - future enhancement)

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Flask**
- **OpenCV**
- **YOLOv5 (Ultralytics)**
- **Torch (PyTorch)**
- **HTML/CSS (for frontend)**

---

## 💡 Use Cases

- Surveillance systems
- Smart cameras
- Industrial safety detection
- Object counting and analytics
