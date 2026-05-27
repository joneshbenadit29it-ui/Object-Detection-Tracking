# 👁️‍🗨️ Real-Time Object Detection & Tracking 🎯

<p align="center">
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-blueviolet?style=for-the-badge&logo=python&logoColor=white" alt="YOLOv8">
  <img src="https://img.shields.io/badge/Object--Tracking-Deep%20SORT-🚀-orange?style=for-the-badge" alt="Deep SORT">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-blue?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
</p>

---

An advanced computer vision system engineered to detect and track multiple objects concurrently in real time. This project seamlessly integrates the blazing-fast inference speeds of **YOLOv8** for localized object detection with the deep-feature precision of **Deep SORT** to maintain strict, identity-consistent tracking IDs across dynamic video frames.
---

## 🚀 Features

* **Real-Time Detection:** Utilizes a pre-trained YOLOv8 nano (`yolov8n.pt`) model for high-speed frame processing.
* **Continuous Multi-Object Tracking:** Implements Deep SORT to maintain distinct ID assignments across consecutive frames even during occlusions.
* **Fail-Safe Video Engine:** Automatically detects hardware webcam blocks or missing local media, instantly deploying a stable multi-fallback remote network stream to ensure continuous execution.
* **Confidence Filtering:** Processes detections with a strict confidence threshold (> 40%) to eliminate background noise and false positives.

---

## 🛠️ System Requirements & Architecture

The system operates inside an isolated, lightweight python sandbox to avoid dependency conflicts:

* **Python:** 3.11+
* **Core Libraries:** OpenCV (`cv2`), Ultralytics (YOLOv8), Deep-Sort-Realtime, PyTorch
* **Environment:** Windows PowerShell Execution-Policy optimized

---

## 📁 Repository Structure

```text
Object-Detection-Tracking/
│
├── venv/                       # Isolated Virtual Environment (Hidden via .gitignore)
├── main.py                     # Main application entry point script
├── yolov8n.pt                  # Pre-trained YOLOv8 nano weights file
├── sample.mp4                  # Local video source file (Auto-generated fallback)
├── .gitignore                  # Keeps tracking metadata and heavy assets local
└── README.md                   # Project documentation
⚙️ Setup and Installation
1. Clone the Repository
Bash
git clone [https://github.com/joneshbenadit29it-ui/Object-Detection-Tracking.git](https://github.com/joneshbenadit29it-ui/Object-Detection-Tracking.git)
cd Object-Detection-Tracking
2. Activate the Virtual Environment
On Windows (PowerShell):

PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1
3. Install Dependencies
PowerShell
pip install opencv-python ultralytics deep-sort-realtime
💻 Usage
To launch the object tracking interface, run the core script:

PowerShell
python main.py
Stream Pipeline Architecture:
Primary Feed: Looks for a local sample.mp4 file or a live camera stream index.

Secondary Fallback: If local files are absent or hardware permissions lock out the webcam sensor, the engine automatically attempts to pull an optimized public domain tracking clip.

Tertiary Live Stream: If file writing is restricted by administrative policies, it defaults directly to a cloud network video stream to guarantee output visibility.

To Exit: Click inside the visualization window and tap the 'q' key on your keyboard.

📊 Sample Output Visualization
The output window displays live bounding boxes annotated with persistent Tracking IDs tracking distinct target features:

Plaintext
+-----------------------------------------------------------+
|  [ID 1] Class: Person                                     |
|  +-------------------+                                    |
|  |                   |                                    |
|  |     (Object)      |                                    |
|  |                   |                                    |
|  +-------------------+                                    |
|                                     [ID 2] Class: Car     |
|                                     +------------------+  |
|                                     |     (Object)     |  |
|                                     +------------------+  |
+-----------------------------------------------------------+
📜 Task Requirements Met
[x] Set up video input stream pipeline using OpenCV.

[x] Integrate pre-trained deep learning localization network (YOLOv8).

[x] Render real-time bounding boxes over localized array positions.

[x] Map unique tracking tracking identities across frames using Deep SORT.

[x] UI/UX display output showing ID labels in real time.


---

### Step 5: Push this README to GitHub too!

Once you save the file, run these 3 quick commands in your terminal to update your GitHub repository with this beautiful profile layout:

```powershell
git add README.md
git commit -m "Docs: Add beautiful and comprehensive project README documentation"
git push origin main
