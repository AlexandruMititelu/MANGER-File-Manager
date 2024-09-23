import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import threading
from photo_selector import copy_selected_files
from utils import read_input_text
from logger import setup_logger
from data_manager import save_data, load_data
import logging
from pathlib import Path

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class PhotoSelectorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Photo Selector")
        master.geometry("800x600")

        # Load saved data
        saved_data = load_data()

        # Create main frame
        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Source Folder Path
        self.source_frame = ctk.CTkFrame(self.main_frame)
        self.source_frame.pack(fill=tk.X, padx=10, pady=10)
        ctk.CTkLabel(self.source_frame, text="Source Folder:").pack(side=tk.LEFT, padx=5)
        self.source_path = ctk.CTkEntry(self.source_frame, width=400)
        self.source_path.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.source_path.insert(0, saved_data['source_path'])
        ctk.CTkButton(self.source_frame, text="Browse", command=self.browse_source, width=100).pack(side=tk.RIGHT, padx=5)

        # Target Folder Path
        self.target_frame = ctk.CTkFrame(self.main_frame)
        self.target_frame.pack(fill=tk.X, padx=10, pady=10)
        ctk.CTkLabel(self.target_frame, text="Target Folder:").pack(side=tk.LEFT, padx=5)
        self.target_path = ctk.CTkEntry(self.target_frame, width=400)
        self.target_path.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.target_path.insert(0, saved_data['target_path'])
        ctk.CTkButton(self.target_frame, text="Browse", command=self.browse_target, width=100).pack(side=tk.RIGHT, padx=5)

        # Input Text
        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        ctk.CTkLabel(self.input_frame, text="Input:").pack(anchor=tk.W, padx=5, pady=5)
        self.input_text = ctk.CTkTextbox(self.input_frame, height=150)
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.input_text.insert(tk.END, saved_data['input_text'])

        # Run Button
        self.run_button = ctk.CTkButton(self.main_frame, text="Run", command=self.run_script, height=40)
        self.run_button.pack(pady=20)

        # Log Output
        self.log_frame = ctk.CTkFrame(self.main_frame)
        self.log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        ctk.CTkLabel(self.log_frame, text="Log:").pack(anchor=tk.W, padx=5, pady=5)
        self.log_output = ctk.CTkTextbox(self.log_frame, height=150, state='disabled')
        self.log_output.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Configure logging
        setup_logger(self.log_output)

        # Bind the closing event
        master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def browse_source(self):
        folder_selected = filedialog.askdirectory()
        self.source_path.delete(0, tk.END)
        self.source_path.insert(0, folder_selected)

    def browse_target(self):
        folder_selected = filedialog.askdirectory()
        self.target_path.delete(0, tk.END)
        self.target_path.insert(0, folder_selected)

    def run_script(self):
        self.run_button.configure(state='disabled')
        threading.Thread(target=self._run_script_thread, daemon=True).start()

    def _run_script_thread(self):
        try:
            source_dir = Path(self.source_path.get())
            dest_dir = Path(self.target_path.get())

            if not source_dir.exists():
                raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
            
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            file_names_to_select = read_input_text(self.input_text.get("1.0", tk.END))
            files_copied = copy_selected_files(source_dir, dest_dir, file_names_to_select)
            
            logging.info(f"Files have been copied successfully! {files_copied} photos have been selected")
        
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
        finally:
            self.master.after(0, lambda: self.run_button.configure(state='normal'))

    def on_closing(self):
        # Save data before closing
        save_data(
            self.source_path.get(),
            self.target_path.get(),
            self.input_text.get("1.0", tk.END)
        )
        self.master.destroy()