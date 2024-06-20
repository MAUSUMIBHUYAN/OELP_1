import cv2
import length
import size
import os

# Read character length and area from the imported modules
l = length.character_length
s = size.result[4]

# Calculate compactness
comp = l / s

# Load the image
image_path = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\o\o.png"
image = cv2.imread(image_path)

# Overlay the character length on the image
font = cv2.FONT_HERSHEY_SIMPLEX
org = (20, 100)
fontScale = 3.5
color = (255, 0, 0)  # Blue color in BGR
thickness = 2
cv2.putText(image, f'Compactness: {comp:.3f}', org, font, fontScale, color, thickness, cv2.LINE_AA)

# Define the output directory
output_folder = r"C:\Users\mausu\Downloads\Electrical\Sem4\OELP\KANNADA\Swara\Compactness"

# Save the annotated image with compactness value included
output_image_path = os.path.join(output_folder, "na.png")
cv2.imwrite(output_image_path, image)

# Display the image
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the compactness value
print("Compactness:", comp)
