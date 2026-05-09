import cv2
import numpy as np

def make_coordinates(image, line_parameters):
    """
    Calculates the coordinates of a line based on slope and intercept.
    """
    try:
        slope, intercept = line_parameters
    except TypeError:
        return None
        
    y1 = image.shape[0]
    y2 = int(y1 * (3/5)) # Draw lines up to 3/5 of the screen height
    
    if slope == 0:
        return None
        
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    """
    Averages the slope and intercept of detected lines to separate Left and Right lanes.
    """
    left_fit = []
    right_fit = []
    
    if lines is None:
        return None
        
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        
        # Slope check: Left lane has negative slope, Right lane has positive slope
        # Removing near-horizontal lines (slope approx 0)
        if slope < -0.5:
            left_fit.append((slope, intercept))
        elif slope > 0.5:
            right_fit.append((slope, intercept))
            
    left_fit_average = np.average(left_fit, axis=0) if left_fit else None
    right_fit_average = np.average(right_fit, axis=0) if right_fit else None
    
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    
    return np.array([line for line in [left_line, right_line] if line is not None])

def display_lines(image, lines):
    """
    Draws lines on a black image.
    """
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image
