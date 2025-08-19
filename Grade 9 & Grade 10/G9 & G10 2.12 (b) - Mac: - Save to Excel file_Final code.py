# On line 51 to 53 Open the selected Excel file in append mode, replace the "Attendance"
# sheet if it exists, and write the new data (without headers or index) into that sheet.
# global lets a function access and update a variable that was defined outside the function on line 13.


from tkinter import filedialog
import tkinter as tk
from tkcalendar import DateEntry
import pytesseract
import cv2
import pandas as pd

global selected_file

def update(*args):
    date_label.config(text="Selected date is "+date_var.get())

def select_file():
    global selected_file
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
    extracted_text = extract_text_from_image(image_file_path)
    print(extracted_text)
    text_widget.delete(1.0, tk.END)
    text_widget.config(state="normal")
    text_widget.insert(tk.END, extracted_text + "\n")
    text_widget.config(state="disabled")


def save_to_excel(text, date):  # Save extracted text and date to the selected Excel file
    if not selected_file:  # Check if Excel file is selected
        print("Please select an Excel file first.")  # Show message if no file selected
        return  # Exit the function

    # Create DataFrame with date and text
    df = pd.DataFrame({"Date": [date], "Extracted Text": [text]})
   # Open file in append mode
    with pd.ExcelWriter(selected_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # Write data to 'Attendance' sheet
        df.to_excel(writer, sheet_name='Attendance', index=False, header=False)
    print("Text saved to Excel file.")  # Confirm save success


def submit_to_excel():
    extracted_text = text_widget.get(1.0, tk.END).strip()
    date = date_entry.get()
    save_to_excel(extracted_text, date)


root = tk.Tk()
root.title("Training Program")
root.geometry("500x500")

root.configure(bg='skyblue')

label1 = tk.Label(root, text="Smart Attendance System", font=("Courier New", 24), bg="blue",
fg="white")
label1.pack(padx=10,pady=10)

date_label = tk.Label(root, text="Select Date:",font=("Courier New", 10), bg="skyblue")
date_label.pack(pady=5)

date_var = tk.StringVar()

date_entry = DateEntry(root,relief="sunken",borderwidth=3,justify="center",state="normal",
selectbackground="blue",textvariable=date_var)
date_entry.pack(pady=5)

date_var.trace('w', update)

button1 = tk.Button(root, text="Select Excel File",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white",command=select_file)
button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",
activebackground="grey",activeforeground="white",command=mark_attendance)
button2.config(highlightbackground = "black",highlightthickness=3)
button2.pack(pady=10)

text_widget = tk.Text(root,width=50,height=5,spacing1=5,spacing2=5,spacing3=5,state="disabled")

text_widget.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="#B4A3D8",
activebackground="blue",activeforeground="white",command=submit_to_excel)
submit.config(highlightbackground = "black",highlightthickness=3)
submit.pack(pady=10)

root.mainloop()
