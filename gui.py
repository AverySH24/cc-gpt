# pip install customtkinter
# https://www.youtube.com/watch?v=iM3kjbbKHQU

# https://www.activestate.com/resources/datasheets/tkinter-cheatsheet-tips-and-tricks-to-create-your-user-interface/
# import tkinter
# import customtkinter
# from tkinter import *

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

# root = customtkinter.CTk()
# root.geometry("500x350")


# frame = customtkinter.CtkFrame(master = root)

# root.mainloop()

import tkinter
import customtkinter as customtkinter

# print("Hello")

class App(customtkinter.CTk):
   def __init__(self):
    super().__init__()

    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("700x540")

    def button_function():
        print("button pressed")

    # Use CTkButton instead of tkinter Button
    button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# if __name__ == "__main__":
app = App()
app.mainloop()
print("Goodbye")