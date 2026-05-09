import cv2
import numpy as np
import pipeline
import os

def create_dummy_road_image():
    # Create black image
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    
    # Draw "Lane Lines" (White)
    # Left Lane
    cv2.line(img, (100, 480), (300, 300), (255, 255, 255), 10)
    # Right Lane
    cv2.line(img, (540, 480), (340, 300), (255, 255, 255), 10)
    
    cv2.imwrite("dummy_road.jpg", img)
    return img

def test_pipeline():
    print("Generating dummy road image...")
    img = create_dummy_road_image()
    
    print("Running pipeline...")
    try:
        result = pipeline.process_frame(img)
        cv2.imwrite("output_test.jpg", result)
        print("Pipeline executed successfully. Output saved to 'output_test.jpg'.")
        
        # Verify if lines were drawn (check for blue color in output)
        # pipeline draws lines in (255, 0, 0) - Blue
        # But addWeighted might alter it.
        # Blue channel is index 0.
        blue_mask = cv2.inRange(result, (200, 0, 0), (255, 100, 100))
        if cv2.countNonZero(blue_mask) > 0:
            print("SUCCESS: Lane lines detected and drawn.")
        else:
            print("WARNING: Pipeline ran but no lines were drawn on the output.")
            
    except Exception as e:
        print(f"FAILED: Pipeline crashed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_pipeline()
