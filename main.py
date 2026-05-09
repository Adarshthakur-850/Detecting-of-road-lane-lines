import cv2
import numpy as np
import pipeline
import time

def main():
    # Attempt to open webcam (0). 
    # If you have a video file, replace 0 with the file path, e.g., "test_video.mp4"
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    print("Press 'q' to quit.")

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            try:
                # Process the frame through the lane detection pipeline
                lane_image = pipeline.process_frame(frame)
                cv2.imshow('Lane Detection', lane_image)
            except Exception as e:
                # If pipeline fails (e.g., no lines detected), just show original frame
                # print(f"Processing error: {e}")
                cv2.imshow('Lane Detection', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
