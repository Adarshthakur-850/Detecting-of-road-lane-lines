# Road Lane Line Detection System

A real-time lane detection system enabling the identification of lane boundaries in a video stream using computer vision techniques.

## Features
- **Region of Interest (ROI)**: Focuses only on the road area to reduce noise.
- **Edge Detection**: Uses Canny Edge Detection to find lane markers.
- **Line Averaging**: Stabilizes detections by averaging line segments into a single Left and Right lane.
- **Real-time Overlay**: Draws detected lanes on the original video feed.

## Project Structure
```
lane_detection/
│
├── main.py        # Entry point (Video processing loop)
├── pipeline.py    # Core processing logic
├── roi.py         # ROI masking
├── utils.py       # Math and drawing helpers
└── requirements.txt
```

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run with Webcam**:
    ```bash
    python main.py
    ```
    *By default, `main.py` uses camera index `0`.*

2.  **Run with Video File**:
    Modify `main.py`:
    ```python
    cap = cv2.VideoCapture("path/to/video.mp4")
    ```

3.  **Controls**:
    - Press `q` to exit the application.

## Troubleshooting
- **No Lines Detected**: Try adjusting the `Canny` thresholds in `pipeline.py` or the `HoughLinesP` parameters.
- **Wrong Lines**: Adjust the `polygons` vertices in `roi.py` to better match your camera's perspective.
