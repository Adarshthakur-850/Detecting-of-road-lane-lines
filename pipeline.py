import cv2
import numpy as np
import roi
import utils

def process_frame(image):
    """
    Takes an image and returns the image with lane lines overlaid.
    """
    height, width = image.shape[:2]
    
    # 1. Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 2. Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 3. Canny Edge Detection
    canny = cv2.Canny(blur, 50, 150)
    
    # 4. Region of Interest Masking
    cropped_image = roi.region_of_interest(canny)
    
    # 5. Hough Transform
    # rho=2, theta=np.pi/180, threshold=100, minLineLength=40, maxLineGap=5
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    
    # 6. Average Slope Intercept (Left/Right Lanes)
    # This returns averaged line coordinates for left and right lane
    averaged_lines = utils.average_slope_intercept(image, lines)
    
    # 7. Draw Lines
    line_image = utils.display_lines(image, averaged_lines)
    
    # 8. Overlay
    combo_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)
    
    return combo_image
