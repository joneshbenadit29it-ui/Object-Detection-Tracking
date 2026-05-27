import cv2
import os
import urllib.request
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

def ensure_video_source(filename="sample.mp4"):
    """Ensures a valid video file exists or falls back safely."""
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        return filename

    print(f"'{filename}' not found locally. Attempting fallback stream...")
    
    # Direct reliable archival source URL
    url = "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
    try:
        print("Downloading a fresh sample tracking video clip...")
        urllib.request.urlretrieve(url, filename)
        print("Download complete!\n")
        return filename
    except Exception as e:
        print(f"\n[Warning] Automated download encountered a network block: {e}")
        print("Switching engine to a public live network stream directly...")
        # Direct stream backup link that bypasses local file writing constraints
        return "https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"

def main():
    # Automatically manages and falls back on standard network streams if local storage fails
    video_source = ensure_video_source("sample.mp4")

    # 1. Initialize Video Input
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print(f"Error: OpenCv engine failed to initialize data stream from: '{video_source}'.")
        return

    # 2. Load Pre-trained YOLOv8 Model
    try:
        model = YOLO("yolov8n.pt")  
    except Exception as e:
        print(f"Model initialization error: {e}. Check internet connection for initial download.")
        return

    # 3. Initialize Deep SORT Tracker
    tracker = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0, max_cosine_distance=0.2)

    print("\n" + "="*50)
    print("SUCCESS: Engine Active.")
    print("-> Press 'q' inside the video display window to stop processing.")
    print("="*50 + "\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video source stream ended or frame structure dropped.")
            break

        # 4. Run YOLOv8 Object Detection on the current frame
        results = model(frame, verbose=False)[0]
        
        detections = []
        # Parse detections into the format Deep SORT expects: ([x, y, w, h], confidence, class_id)
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            
            # Filter detections with > 40% confidence
            if conf > 0.4:
                detections.append(([x1, y1, w, h], conf, cls))

        # 5. Update Tracker with current frame detections
        tracks = tracker.update_tracks(detections, frame=frame)

        # 6. Draw Bounding Boxes and Tracking IDs
        for track in tracks:
            if not track.is_confirmed():
                continue
            
            track_id = track.track_id
            ltrb = track.to_ltrb() # Left, Top, Right, Bottom format
            x1, y1, x2, y2 = map(int, ltrb)

            # Draw bounding box (Green)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Display Tracking ID
            label = f"ID {track_id}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # 7. Display the output window
        cv2.imshow("Object Detection & Tracking", frame)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up resources
    cap.release()
    cv2.destroyAllWindows()
    print("System resources safely unlinked. Process terminated.")

if __name__ == "__main__":
    main()