import customtkinter as ctk
from gui import PhotoSelectorGUI

import sys
print(sys.executable)
print(sys.path)

if __name__ == "__main__":
    root = ctk.CTk()
    gui = PhotoSelectorGUI(root)
    root.mainloop()