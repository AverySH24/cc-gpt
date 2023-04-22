# pip install customtkinter
# https://www.youtube.com/watch?v=iM3kjbbKHQU

# https://www.activestate.com/resources/datasheets/tkinter-cheatsheet-tips-and-tricks-to-create-your-user-interface/

import tkinter
import customtkinter as customtkinter
import gpt

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
            if (page_name == "ChatPage"):
                for name in ("Beethoven", "Mozart", "Brahms", "Bach", "Tchaikovsky", "Chopin"):
                    frame = F(parent=container, controller=self, page = name)
                    self.frames[name] = frame
                    frame.grid(row=0, column=0, sticky="nsew")
            else:
                frame = F(parent=container, controller=self, page = "start")
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")


            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.

        

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller, page):
        
        def button_function(composer):
            # print(composer)
            controller.show_frame(composer)


        customtkinter.CTkFrame.__init__(self, parent)
        
        # self.label = customtkinter.CTkLabel("Start Page")
        # self.label.grid(row=0, column=0, padx=20)
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
    def __init__(self, parent, controller, page):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        label = customtkinter.CTkLabel(master=self, text=page)
        label.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)
        # print("CHAT" + page)
        convo = 0
        # if (convo == 0):
        #     data_first = gpt.start_convo(page)
        #     convo = data_first["conversationId"]
        # if (convo_num == 0):
        #     data = gpt.start_convo(page)
        #     convo_num = data["conversationId"]
        #     textbox.insert("end", page + ":" + data["response"] + "\n\n")

        def new_entry(convo_num):
            data = gpt.make_query(page, entry.get(), convo_num)
            textbox.insert("end", "You: " + entry.get() + "\n\n")
            textbox.insert("end", page + ":" + data["response"] + "\n\n")

        entry = customtkinter.CTkEntry(self, fg_color = "transparent", border_width = 2, text_color = ("gray10", "#DCE4EE"))
        entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        main_button_1 = customtkinter.CTkButton(self, fg_color="transparent", border_width=2, text = "Send", text_color=("gray10", "#DCE4EE"), command = lambda: new_entry(convo))
        main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        textbox = customtkinter.CTkTextbox(self, width=250)
        textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        home_button = customtkinter.CTkButton(self, fg_color="transparent", border_width=2, text = "Back", text_color=("gray10", "#DCE4EE"), command = lambda: controller.show_frame("StartPage"))
        home_button.grid(row=2, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


app = App()
app.mainloop()
