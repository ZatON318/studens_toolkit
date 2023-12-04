import customtkinter
#Work in progress
def launch_pptx_to_txt():
    print("button clicked")

app = customtkinter.CTk()
app.title("Students toolkit")
app.resizable(False, False)
app.geometry("400x150")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure((0, 1), weight=1)

button = customtkinter.CTkButton(app, text=".pptx -> .txt", command=launch_pptx_to_txt)
button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

app.mainloop()