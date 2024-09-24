import logging  # Standard library for logging messages
import tkinter as tk  # Standard tkinter library for GUI

class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()  # Initialize the base class
        self.text_widget = text_widget  # Reference to the text widget for logging output

    def emit(self, record):
        msg = self.format(record)  # Format the log message
        self.text_widget.configure(state='normal')  # Enable editing of the text widget
        self.text_widget.insert(tk.END, msg + '\n')  # Insert the log message at the end
        self.text_widget.configure(state='disabled')  # Disable editing to prevent user changes
        self.text_widget.see(tk.END)  # Scroll to the end of the text widget

def setup_logger(text_widget):
    log_handler = TextHandler(text_widget)  # Create a custom log handler
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')  # Configure logging format and level
    logging.getLogger().addHandler(log_handler)  # Add the custom handler to the logger