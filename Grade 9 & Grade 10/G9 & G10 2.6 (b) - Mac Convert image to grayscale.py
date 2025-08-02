


import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_file="image.png"
image = cv2.imread(image_file)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converts color image to grayscale for simplicity.
extracted_text = pytesseract.image_to_string(gray)
print(extracted_text)
