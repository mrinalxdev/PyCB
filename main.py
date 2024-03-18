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
        self.image_ratio = self.image.size[0] / self.image.size[1]

        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self)

        self.resize_image()


    def resize_image(self, event):

        #current canvas ratio
        canvas_ratio = event.widht / event.hieght

        if canvas_ratio > self.image_ratio:
            image_hieght = int(event.hieght)
            image_width = int(event.hieght * self.image_ratio )
        else: 
            image_width = int(event.width)
            image_hieght = int(image_width / self.image_ratio)

        self.image_output.delete('all')
        resized_image = self.image.resize((image_width, image_hieght))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width / 2, event.width / 2, image = self.image_tk)

App()