import customtkinter as ctk  
from gui import PhotoSelectorGUI  

import sys  
print(sys.executable)  # path of the Python interpreter
print(sys.path)  # paths where Python looks for modules

if __name__ == "__main__":  
    root = ctk.CTk()  # main application window
    #root.iconbitmap('img/app_icon.ico')

    ctk.set_appearance_mode("System")  # Set the appearance mode of the GUI
    ctk.set_default_color_theme("blue")  # Set the default color theme
    gui = PhotoSelectorGUI(root)  # Initialize the GUI
    root.mainloop()  # Start the GUI event loop