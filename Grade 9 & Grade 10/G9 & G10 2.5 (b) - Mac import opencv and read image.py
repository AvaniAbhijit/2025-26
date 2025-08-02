# import cv2 imports the OpenCV library and allows you to use its image processing functions.
# cv2.imread() reads the image file (image.png) and loads it as a NumPy array of pixel values.

import pytesseract
import cv2 #importing opencv
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract.exe'
image_file="image.png"
#This reads the image file using OpenCV, treating it as an array of pixels.
image = cv2.imread(image_file)
extracted_text = pytesseract.image_to_string(image)
print(extracted_text)
