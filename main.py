import customtkinter as ctk  
from gui import PhotoSelectorGUI  

import sys  
print(sys.executable)  # path of the Python interpreter
print(sys.path)  # paths where Python looks for modules

if __name__ == "__main__":  
    root = ctk.CTk()  # main application window
    #root.iconbitmap('img/app_icon.ico')
    gui = PhotoSelectorGUI(root)  # Initialize the GUI
    root.mainloop()  # Start the GUI event loop