# Line 31 function named extract_text_from_image,
# passing in a variable image_file_path as its argument.
# The function extract_text_from_image() is expected to use
# Optical Character Recognition (OCR) to extract text from that image.
# The resulting text is then stored in the variable extracted_text

# Task: Insert Extracted Text into a Text Widget using insert on line 38.
#        Hint : text_widget.insert(extracted_text)


from tkinter import filedialog
import tkinter as tk
from tkcalendar import DateEntry
import pytesseract
import cv2

def update(*args):
    date_label.config(text="Selected date is "+date_var.get())

def select_file():
    selected_file = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    print("Selected file:", selected_file)

def extract_text_from_image(image_file_path):
        pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
        image = cv2.imread(image_file_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        extracted_text = pytesseract.image_to_string(gray)
        return extracted_text

def mark_attendance():
    image_file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.PNG")])
    if not image_file_path:
        print("No image selected.")
        return
    extracted_text = extract_text_from_image(image_file_path)#pass the image selected by user and fetch the extracted text
    print(extracted_text)#printing the extracted text on console



root = tk.Tk()
root.title("Training Program")
root.geometry("500x500")

root.configure(bg='skyblue')

label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue", fg="white")
label1.pack(padx=10,pady=10)

date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10), bg="skyblue")
date_label.pack(pady=5)

date_var = tk.StringVar()

date_entry = DateEntry(root,relief="sunken",borderwidth=3,justify="center",state="normal",selectbackground="blue",textvariable=date_var)
date_entry.pack(pady=5)

date_var.trace('w', update)

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,bg="#B4A3D8",activebackground="grey",activeforeground="white",command=select_file)
button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",activebackground="grey",activeforeground="white",command=mark_attendance)
button2.config(highlightbackground = "black",highlightthickness=3)
button2.pack(pady=10)

text_widget = tk.Text(root,width=50,height=5,spacing1=5,spacing2=5,spacing3=5,state="disabled")

text_widget.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="#B4A3D8",activebackground="blue",activeforeground="white")
submit.config(highlightbackground = "black",highlightthickness=3)
submit.pack(pady=10)

root.mainloop()
