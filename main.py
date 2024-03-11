import customtkinter as ctk
from image_widget import *

class App(ctk.CTk):
    def __init__(self):

        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('ImagiLab')
        self.minsize(800, 500)


        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight= 2)
        self.columnconfigure(0, weight= 6)

        #widgets for the application
        ImageImporter(self, self.import_image)


        #running the app
        self.mainloop()

    def import_image(self, path):
        print(path)

App()