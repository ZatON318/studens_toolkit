import tkinter as tk
from tkinter import filedialog
import customtkinter

def convert_to_txt():
    pass

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PowerPoint files", "*.pptx")])
    if file_path:
        pathrs.delete(0, tk.END)
        pathrs.insert(0, file_path)

app = customtkinter.CTk()
app.title("Students toolkit")
app.resizable(False, False)
app.geometry("400x150")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure((0, 1), weight=1)

button_browse = customtkinter.CTkButton(app, text="Browse File", command=browse_file)
button_browse.grid(row=0, column=0, padx=10, pady=(15,0), sticky="nw")

pathrs = customtkinter.CTkEntry(app, placeholder_text="C:/...")

button = customtkinter.CTkButton(app, text="convert", command=convert_to_txt)
button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")


app.mainloop()