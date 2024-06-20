import cv2
import numpy as np
import sys
import os
def calculate_stroke_lengths(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was read successfully
    if image is None:
        print("Error: Unable to read image.")
        return None, None, None  # Return None for all values

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding to automatically determine the threshold value
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Morphological operations to clean up the image
    kernel = np.ones((3, 3), np.uint8)
    morphed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Find contours in the binary image
    contours, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate the total character length as the sum of stroke lengths
    character_length = 0

    # Iterate through contours to calculate character length
    for contour in contours:
        # Calculate the length of each contour (stroke)
        arc_length = cv2.arcLength(contour, closed=True)
        
        # Exclude contours smaller than a certain threshold (likely noise)
        if arc_length > 10:  # Adjust threshold as needed
            character_length += arc_length

    return character_length, contours, image



# Specify your image path here
image_path = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\ra\ra.png"
character_length,contours, image= calculate_stroke_lengths(image_path)

if character_length is not None and image is not None:
    print("Character Length:", character_length)
    

    # Overlay the character length on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (20, 100)
    fontScale = 4
    color = (255, 0, 0)  # Blue color in BGR
    thickness = 2
    cv2.putText(image, f'Length: {character_length:.0f}', org, font, fontScale, color, thickness, cv2.LINE_AA)

    # Draw contours on the image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Define the path to save the output image
    output_folder = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\A_english\8633.jpg"
    output_image_path = os.path.join(output_folder, "na.png")

    # Save the image
    cv2.imwrite(output_image_path, image)
    print("Output image saved to:", output_image_path)
    cv2.imshow('Output Image', image)
    cv2.waitKey(4000)
    
