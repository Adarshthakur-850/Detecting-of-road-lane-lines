import cv2
import numpy as np

def region_of_interest(image):
    """
    Applies a mask to keep only the region of interest (road area).
    """
    height = image.shape[0]
    width = image.shape[1]
    
    # Define a triangular polygon for the mask
    # Adjust these points based on the camera position/angle
    # (Bottom Left, Bottom Right, Top Mid)
    polygons = np.array([
        [(0, height), (width, height), (int(width * 0.5), int(height * 0.55))]
    ])
    
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image
