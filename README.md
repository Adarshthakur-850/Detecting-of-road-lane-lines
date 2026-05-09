# Detecting Road Lane Lines using OpenCV

A computer vision project that detects road lane lines from images and videos using **Python** and **OpenCV**. This project identifies lane boundaries on roads by applying image processing techniques such as edge detection, region masking, and Hough Transform.

## Project Overview

Lane detection is a critical component in:

- Autonomous Vehicles
- Advanced Driver Assistance Systems (ADAS)
- Self-driving car navigation
- Traffic monitoring systems

This project processes road images/videos and highlights detected lane lines in real time.

---

## Features

- Detect lane lines in road images
- Detect lane lines in video streams
- Real-time frame processing
- Edge detection using Canny Algorithm
- Region of Interest masking
- Hough Line Transform
- Lane line visualization overlay

---

## Tech Stack

- Python
- OpenCV
- NumPy
- Matplotlib

---

## Project Workflow

### 1. Image Preprocessing
Convert image to grayscale for easier processing.

```python
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
````

### 2. Gaussian Blur

Reduce noise from the image.

```python
blur = cv2.GaussianBlur(gray, (5,5), 0)
```

### 3. Canny Edge Detection

Detect edges in road lanes.

```python
edges = cv2.Canny(blur, 50, 150)
```

### 4. Region of Interest Selection

Focus only on the road area.

```python
masked = region_of_interest(edges)
```

### 5. Hough Transform

Detect lane lines.

```python
lines = cv2.HoughLinesP(
    masked,
    rho=2,
    theta=np.pi/180,
    threshold=100
)
```

### 6. Overlay Detected Lanes

Draw detected lanes on original frame.

---

## Project Structure

```bash
Detecting-of-road-lane-lines/
│
├── test_images/
├── test_videos/
├── output_images/
├── output_videos/
├── lane_detection.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Adarshthakur-850/Detecting-of-road-lane-lines.git
```

Move into project directory:

```bash
cd Detecting-of-road-lane-lines
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Run on Image

```bash
python lane_detection.py
```

### Run on Video

Modify input path in script and run:

```bash
python lane_detection.py
```

---

## Output

The system detects:

* Left lane lines
* Right lane lines
* Road boundaries

Output examples include processed images/videos with highlighted lanes.

---

## Applications

* Self-driving cars
* Traffic surveillance
* Smart transportation systems
* Accident prevention systems

---

## Future Improvements

* Curved lane detection
* Deep learning-based lane segmentation
* Real-time webcam integration
* Lane departure warning system

---

## Sample Techniques Used

This project uses traditional computer vision techniques similar to widely used lane detection pipelines involving **Canny Edge Detection**, **Hough Transform**, and ROI masking. ([GitHub][1])

For more advanced implementations, perspective transformation and curvature estimation are often used in modern lane detection systems. ([GitHub][2])

---

## Author

**Adarsh Thakur**

GitHub: [Adarshthakur-850 GitHub Profile](https://github.com/Adarshthakur-850?utm_source=chatgpt.com)

---

## License

This project is open-source and available under the MIT License.


[1]: https://github.com/adityagandhamal/road-lane-detection?utm_source=chatgpt.com "adityagandhamal/road-lane-detection"
[2]: https://github.com/abhijitmahalle/lane-detection?utm_source=chatgpt.com "Lane Detection and Turn Prediction"
