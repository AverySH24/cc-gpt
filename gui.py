# pip install customtkinter
# https://www.youtube.com/watch?v=iM3kjbbKHQU

# https://www.activestate.com/resources/datasheets/tkinter-cheatsheet-tips-and-tricks-to-create-your-user-interface/

import tkinter
import customtkinter as customtkinter

# print("Hello")

class App(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ChatPage):
            page_name = F.__name__
            if F is ChatPage:
                for name in ("Beethoven", "Mozart", "Brahms", "Bach", "Tchaikovsky", "Chopin"):
                    frame = F(parent=container, controller=self, page = name)
                    self.frames[page_name + name] = frame
            else:
                frame = F(parent=container, controller=self, page = "start")
                self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        
        def button_function(composer):
            print(composer)
            controller.show_frame("ChatPage" + composer)


        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

            # Use CTkButton instead of tkinter Button
        buttonBeethoven = customtkinter.CTkButton(self, text="Beethoven", command= lambda: button_function("Beethoven"))
        buttonBeethoven.place(relx=0.25, rely=0.25, anchor=tkinter.CENTER)

        buttonMozart = customtkinter.CTkButton(self, text="Mozart", command=lambda: button_function("Mozart"))
        buttonMozart.place(relx=0.75, rely=0.25, anchor=tkinter.CENTER)

        buttonBach = customtkinter.CTkButton(self, text="Bach", command=lambda: button_function("Bach"))
        buttonBach.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

        buttonBrahms = customtkinter.CTkButton(self, text="Brahms", command=lambda: button_function("Brahms"))
        buttonBrahms.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

        buttonTchaikovsky = customtkinter.CTkButton(self, text="Tchaikovsky", command=lambda: button_function("Tchaikovsky"))
        buttonTchaikovsky.place(relx=0.25, rely=0.75, anchor=tkinter.CENTER)

        buttonChopin = customtkinter.CTkButton(self, text="Chopin", command=lambda: button_function("Chopin"))
        buttonChopin.place(relx=0.75, rely=0.75, anchor=tkinter.CENTER)


    

# CHANGE TO FRAME LATER
class ChatPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller, name):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        convo = 0
        if (not convo):
            # there is a new page, you need to create a new conversation with a new prompt.
            convo += 1

        def new_entry():
            textbox.insert("end", "You: " + entry.get() + "\n")
            textbox.insert("end", name + ":" + entry.get() + "\n")

        entry = customtkinter.CTkEntry(self, fg_color = "transparent", border_width = 2, text_color = ("gray10", "#DCE4EE"))
        entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        main_button_1 = customtkinter.CTkButton(self, fg_color="transparent", border_width=2, text = "Send", text_color=("gray10", "#DCE4EE"), command = new_entry)
        main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        textbox = customtkinter.CTkTextbox(self, width=250)
        textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        home_button = customtkinter.CTkButton(self, fg_color="transparent", border_width=2, text = "Back", text_color=("gray10", "#DCE4EE"), command = lambda: controller.show_frame("StartPage"))
        home_button.grid(row=2, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


app = App()
app.mainloop()
