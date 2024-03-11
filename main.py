import customtkinter as ctk
from image_widget import *
from PIL import Image, ImageTk

class App(ctk.CTk):
    def __init__(self):

        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('ImagiLab')
        self.minsize(800, 500)


        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight= 2)
        self.columnconfigure(1, weight= 6)

        #widgets for the application
        self.image_import = ImageImporter(self, self.import_image)


        #running the app
        self.mainloop()

    def import_image(self, path):
        self.image = Image.open(path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self)

        self.resize_image()


    def resize_image(self):
        self.image_output.create_image(0, 0, image = self.image_tk)

App()