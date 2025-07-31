# The select_file function on line 15,
# 1. Allows the user to choose a file using a file dialog  and prints the selected file path.
# 2. It uses filedialog.askopenfilename() to open the file explorer.
# 3. This function is called when the "Select Excel File" button is clicked.
# 4. The button is linked to the function through the command=select_file parameter on line 40.

# Task 1 : Run the code and click on select file button, To make it work solve task 2.
# Task 2 : Call the function select_file on line 42 using command=select_file.

from tkinter import filedialog #importing module which helps us to open files
import tkinter as tk
from tkcalendar import DateEntry

def update(*args):
    date_label.config(text="Selected date is "+date_var.get())

def select_file(): #creating function to open file
    selected_file = filedialog.askopenfilename() #using function to allow users to select file and store it in variable
    print("Selected file:", selected_file)#printing the selected file for confirmation

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

#call the function using command
button1 = tk.Button(root, text="Select Excel File",width=20,height=2,
bg="#B4A3D8",activebackground="grey",activeforeground="white",command=)
button1.config(bd = 5,relief="solid")
button1.pack(pady=10)

button2=tk.Button(root,text="Upload Photo",width=20,height=2,bg="#B4A3D8",activebackground="grey",activeforeground="white")
button2.config(bd = 5,relief="solid")
button2.pack(pady=10)

text_widget = tk.Text(root,width=50,height=5,spacing1=5,spacing2=5,spacing3=5,state="disabled")

text_widget.pack(pady=10)

submit=tk.Button(root,text="Submit",width=20,height=2,bg="black",fg="white",activebackground="blue",activeforeground="white")
submit.pack(pady=10)
