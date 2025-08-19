# pytesseract library (a Python wrapper for Google’s Tesseract-OCR engine)
# to extract text from an image file.
# Download any png file with text and save it as image.png in the same folder as your Python code.

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
#add the name of the image file (ensure that the image and file are saved in the same directory)
image_file="image.png"
#extract text from the image using pytesseract
extracted_text = pytesseract.image_to_string(image_file)
#print the extracted text on console
print(extracted_text)
