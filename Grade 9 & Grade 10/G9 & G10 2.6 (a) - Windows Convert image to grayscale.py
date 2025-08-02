# cv2.cvtColor() is an OpenCV function used to convert images from one color space to another.
# image is originally in BGR format (Blue-Green-Red), as read by cv2.imread().
# cv2.COLOR_BGR2GRAY tells OpenCV to convert the image from BGR to grayscale.

import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_file="image.png"
image = cv2.imread(image_file)
#Converts color image to grayscale for simplicity.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
extracted_text = pytesseract.image_to_string(gray)
print(extracted_text)
