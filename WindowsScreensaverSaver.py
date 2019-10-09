import os
import shutil
from PIL import Image as PIL_Image
from tkinter import *
import subprocess
import psutil

# Source and destination directories
source_path = r'C:\Users\first.second\AppData\Local\packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
destination_path = r'C:\

# takes file from current working directory, copies it as jpg to another directory with a new name 
def copy_and_rename_jpg(file, new_file_name, d_path):    
    shutil.copy(file, d_path)
    old_file = os.path.join(d_path, file)
    new_file = os.path.join(d_path, new_file_name + '.jpg')
    os.rename(old_file, new_file)

# GUI app
class App:
    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()
        
        self.label = Label(frame, text="Would you like to save this image?")
        self.label.pack(side=TOP)
        
        self.yes_button = Button(frame, text="Yes", command=lambda:[self.save_img(), frame.quit()])
        self.yes_button.pack(expand=True, fill=BOTH, side=LEFT)
        
        self.no_button = Button(frame, text="No", command=frame.quit)
        self.no_button.pack(side=RIGHT)
        
        self.filename_entry = Entry(frame)
        self.filename_entry.insert(0, "Type filename here")
        self.filename_entry.pack(side=BOTTOM)
        

    def save_img(self):
        copy_and_rename_jpg(file, self.filename_entry.get(), destination_path)


file_size_threshold = 10000 #multiple files are too small to be image files
os.chdir(source_path)

# loop over image files and request user to save file (with name) or skip
for file in os.listdir():
    file_stats = os.stat(file)
    if file_stats.st_size > file_size_threshold:
        with PIL_Image.open(file) as im:
            root = Tk()
            app = App(root)
            im.show()
            root.mainloop()
            # close image once dealt with
            for proc in psutil.process_iter():
                if proc.name() == "Microsoft.Photos.exe":
                    proc.kill()
            root.destroy()
