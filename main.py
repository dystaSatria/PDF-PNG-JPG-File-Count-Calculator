import os
import tkinter as tk
from tkinter import filedialog, messagebox

def count_files_with_extensions(folder_path, extensions):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in extensions:
                count += 1
    return count

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def calculate_file_count():
    folder_path = folder_entry.get()
    extensions = [".pdf", ".png", ".jpg"]
    file_count = count_files_with_extensions(folder_path, extensions)
    messagebox.showinfo("Result", f"Number of PDF, PNG, and JPG files in the folder: {file_count}")

root = tk.Tk()
root.attributes("-toolwindow", True)
root.title("PDF,PNG,JPG File Count Calculator")

background_image = tk.PhotoImage(file="logodysta.png")
background_image = background_image.subsample(2, 2) 
canvas = tk.Canvas(root, width=background_image.width(), height=background_image.height())
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)




folder_label = tk.Label(root, text="Select Folder:", font=("Times New Roman", 12), pady=10)

folder_label.pack()

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack()
folder_entry = tk.Entry(root, width=50)
folder_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_file_count)
calculate_button.pack()


root.mainloop()
