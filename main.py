import customtkinter as ctk  # Custom tkinter for enhanced GUI elements
from gui import PhotoSelectorGUI  # Import the main GUI class

import sys  # Standard library for system-specific parameters and functions
print(sys.executable)  # Print the path of the Python interpreter
print(sys.path)  # Print the list of paths where Python looks for modules

if __name__ == "__main__":  # Check if the script is run directly
    root = ctk.CTk()  # Create the main application window
    gui = PhotoSelectorGUI(root)  # Initialize the GUI
    root.mainloop()  # Start the GUI event loop