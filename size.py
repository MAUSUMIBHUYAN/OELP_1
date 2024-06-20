import cv2
import numpy as np
import os

def find_character_bounding_box(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was read successfully
    if image is None:
        print("Error: Unable to read image.")
        return None, None, None, None, None  # Return None for all values

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Morphological operations to clean up the image
    kernel = np.ones((3, 3), np.uint8)
    morphed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Find contours in the binary image
    contours, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

    # Merge all contours
    merged_contour = np.vstack(contours)

    # Get the bounding box of the merged contour
    x, y, w, h = cv2.boundingRect(merged_contour)

    # Draw bounding box and text on the image if contours are found
    if x is not None:
        # Draw bounding box and text on the image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f'Area: {w * h}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2)

        # Define the output image path
        output_folder = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\KANNADA\Swara\Area"
        output_image_path = os.path.join(output_folder, "na.png")
        cv2.imshow("Annotated Image", image)
        cv2.waitKey(5000)  # Display for 5 seconds
        cv2.destroyAllWindows() 
        # Save the annotated image
        cv2.imwrite(output_image_path, image)
        
        
        # Return bounding box coordinates and area value
        return x, y, w, h, w * h

    else:
        print("No contours found in the image.")
        return None, None, None, None, None

# Example usage
image_path = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\o\img012-023.png" # Path to your input image
result = find_character_bounding_box(image_path)
if result:
    bounding_box, area = result[:4], result[4]
    print("Bounding box coordinates:", bounding_box)
    print("Area:", area)
