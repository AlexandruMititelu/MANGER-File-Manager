import customtkinter as ctk  # Custom tkinter for enhanced GUI elements
import tkinter as tk  # Standard tkinter library for GUI
from tkinter import filedialog  # Provides dialogs for file selection
import threading  # Allows running tasks in separate threads
import logging  # Used for logging messages
from pathlib import Path  # For handling filesystem paths
import os  # Import os to handle file operations

from photo_selector import copy_selected_files  # Import the file copying function
from utils import read_input_text  # I
from data_manager import save_data, load_data  # Import functions for saving and loading user datamport utility function to read input text
from logger import setup_logger  # Import logger setup function

ctk.set_appearance_mode("System")  # Set the appearance mode of the GUI
ctk.set_default_color_theme("blue")  # Set the default color theme

class PhotoSelectorGUI:
    def __init__(self, master):
        self.master = master  # Reference to the main window
        master.title("MANGER - sort your files")  # Set the window title
        master.geometry("800x600")  # Set the window size
        # master.iconbitmap("img/app_icon.ico")
        

        saved_data = load_data()  # Load previously saved user data

        # Create main frame
        self.main_frame = ctk.CTkFrame(master)  # Create a frame for the main content
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Source Folder Path
        self.source_frame = ctk.CTkFrame(self.main_frame)  # Frame for source folder input
        self.source_frame.pack(fill=tk.X, padx=10, pady=10)
        ctk.CTkLabel(self.source_frame, text="Source Folder:").pack(side=tk.LEFT, padx=5)  # Label for source folder
        self.source_path = ctk.CTkEntry(self.source_frame, width=400)  # Entry for source folder path
        self.source_path.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.source_path.insert(0, saved_data['source_path'])  # Pre-fill with saved path
        ctk.CTkButton(self.source_frame, text="Browse", command=self.browse_source, width=100).pack(side=tk.RIGHT, padx=5)  # Button to browse for source folder

        # Target Folder Path
        self.target_frame = ctk.CTkFrame(self.main_frame)  # Frame for target folder input
        self.target_frame.pack(fill=tk.X, padx=10, pady=10)
        ctk.CTkLabel(self.target_frame, text="Target Folder:").pack(side=tk.LEFT, padx=5)  # Label for target folder
        self.target_path = ctk.CTkEntry(self.target_frame, width=400)  # Entry for target folder path
        self.target_path.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.target_path.insert(0, saved_data['target_path'])  # Pre-fill with saved path
        ctk.CTkButton(self.target_frame, text="Browse", command=self.browse_target, width=100).pack(side=tk.RIGHT, padx=5)  # Button to browse for target folder

        # Input Text
        self.input_frame = ctk.CTkFrame(self.main_frame)  # Frame for input text
        self.input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        ctk.CTkLabel(self.input_frame, text="Input:").pack(anchor=tk.W, padx=5, pady=5)  # Label for input text
        self.input_text = ctk.CTkTextbox(self.input_frame, height=150)  # Textbox for user input
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.input_text.insert(tk.END, saved_data['input_text'])  # Pre-fill with saved input text

        # Run Button
        self.run_button = ctk.CTkButton(self.main_frame, text="Run", command=self.run_script, height=40)  # Button to run the script
        self.run_button.pack(pady=20)

        # Log Output
        self.log_frame = ctk.CTkFrame(self.main_frame)  # Frame for log output
        self.log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        ctk.CTkLabel(self.log_frame, text="Log:").pack(anchor=tk.W, padx=5, pady=5)  # Label for log output
        self.log_output = ctk.CTkTextbox(self.log_frame, height=150, state='disabled')  # Textbox for displaying logs
        self.log_output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Configure logging
        setup_logger(self.log_output)  # Set up logging to the log output textbox

        # Add footer with links
        self.footer_frame = ctk.CTkFrame(self.main_frame)  # Frame for footer
        self.footer_frame.pack(side=tk.BOTTOM, pady=10)  # Position at the bottom

        self.footer_label = ctk.CTkLabel(self.footer_frame, text="by ", font=("Arial", 10, "italic"))  # Italic text
        self.footer_label.pack(side=tk.LEFT)

        self.linkedin_label = ctk.CTkLabel(self.footer_frame, text="@AlexSharesTheView", font=("Arial", 10, "italic"), text_color="gray", cursor="hand2")  # LinkedIn link
        self.linkedin_label.pack(side=tk.LEFT)
        self.linkedin_label.bind("<Button-1>", lambda e: os.startfile("https://github.com/AlexandruMititelu"))  # Open LinkedIn

        self.github_label = ctk.CTkLabel(self.footer_frame, text=" | Github", font=("Arial", 10, "italic"), text_color="gray", cursor="hand2")  # GitHub link
        self.github_label.pack(side=tk.LEFT)
        self.github_label.bind("<Button-1>", lambda e: os.startfile("https://www.linkedin.com/in/alexandru-mititelu-984141252/"))  # Open GitHub

        # Change color on hover
        self.linkedin_label.bind("<Enter>", lambda e: self.linkedin_label.configure(text_color="yellow"))  # Hover effect for LinkedIn
        self.linkedin_label.bind("<Leave>", lambda e: self.linkedin_label.configure(text_color="gray"))  # Reset color

        self.github_label.bind("<Enter>", lambda e: self.github_label.configure(text_color="yellow"))  # Hover effect for GitHub
        self.github_label.bind("<Leave>", lambda e: self.github_label.configure(text_color="gray"))  # Reset color

        # Bind the closing event
        master.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event

    def browse_source(self):
        folder_selected = filedialog.askdirectory()  # Open a dialog to select a directory
        self.source_path.delete(0, tk.END)  # Clear the entry
        self.source_path.insert(0, folder_selected)  # Insert the selected folder path

    def browse_target(self):
        folder_selected = filedialog.askdirectory()  # Open a dialog to select a directory
        self.target_path.delete(0, tk.END)  # Clear the entry
        self.target_path.insert(0, folder_selected)  # Insert the selected folder path

    def run_script(self):
        self.run_button.configure(state='disabled')  # Disable the run button to prevent multiple clicks
        threading.Thread(target=self._run_script_thread, daemon=True).start()  # Start the script in a new thread

    def _run_script_thread(self):
        try:
            source_dir = Path(self.source_path.get())  # Get the source directory from the entry
            dest_dir = Path(self.target_path.get())  # Get the target directory from the entry

            if not source_dir.exists():  # Check if the source directory exists
                raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
            
            dest_dir.mkdir(parents=True, exist_ok=True)  # Create the target directory if it doesn't exist
            
            file_names_to_select = read_input_text(self.input_text.get("1.0", tk.END))  # Read and process input text
            files_copied = copy_selected_files(source_dir, dest_dir, file_names_to_select)  # Copy selected files
            
            logging.info(f"Files have been copied successfully! {files_copied} photos have been selected")  # Log success message
        
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")  # Log any unexpected errors
        finally:
            self.master.after(0, lambda: self.run_button.configure(state='normal'))  # Re-enable the run button

    def on_closing(self):
        # Save data before closing
        save_data(
            self.source_path.get(),  # Save the source path
            self.target_path.get(),  # Save the target path
            self.input_text.get("1.0", tk.END)  # Save the input text
        )
        delete_user_data_file()  # Delete the user data file
        self.master.destroy()  # Close the application

def delete_user_data_file():
    if os.path.exists('user_data.json'):  # Check if the file exists
        os.remove('user_data.json')  # Delete the file