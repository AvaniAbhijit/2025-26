# pytesseract library (a Python wrapper for Google’s Tesseract-OCR engine)
# to extract text from an image file.


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
#add the name of image file (ensure that image and file are saved in same directory)
image_file="image.png"
#extract text from the image using pytesseract
extracted_text = pytesseract.image_to_string(image_file)
#print the extracted text on console
print(extracted_text)
