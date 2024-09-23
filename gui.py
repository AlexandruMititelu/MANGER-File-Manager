import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading
from photo_selector import copy_selected_files
from utils import read_input_text
from logger import setup_logger
from data_manager import save_data, load_data
import logging
from pathlib import Path

class PhotoSelectorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Photo Selector")

        # Load saved data
        saved_data = load_data()

        # Source Folder Path
        tk.Label(master, text="Source Folder Path:").grid(row=0, column=0, sticky="w")
        self.source_path = tk.Entry(master, width=50)
        self.source_path.insert(0, saved_data['source_path'])
        self.source_path.grid(row=0, column=1)
        tk.Button(master, text="Browse", command=self.browse_source).grid(row=0, column=2)

        # Target Folder Path
        tk.Label(master, text="Target Folder Path:").grid(row=1, column=0, sticky="w")
        self.target_path = tk.Entry(master, width=50)
        self.target_path.insert(0, saved_data['target_path'])
        self.target_path.grid(row=1, column=1)
        tk.Button(master, text="Browse", command=self.browse_target).grid(row=1, column=2)

        # Input Text
        tk.Label(master, text="Input:").grid(row=2, column=0, sticky="w")
        self.input_text = tk.Text(master, height=10, width=50)
        self.input_text.insert(tk.END, saved_data['input_text'])
        self.input_text.grid(row=2, column=1, columnspan=2)

        # Run Button
        self.run_button = tk.Button(master, text="Run", command=self.run_script)
        self.run_button.grid(row=3, column=1)

        # Log Output
        self.log_output = scrolledtext.ScrolledText(master, height=10, width=70, state='disabled')
        self.log_output.grid(row=4, column=0, columnspan=3)

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
        self.run_button.config(state='disabled')
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
            self.master.after(0, lambda: self.run_button.config(state='normal'))

    def on_closing(self):
        # Save data before closing
        save_data(
            self.source_path.get(),
            self.target_path.get(),
            self.input_text.get("1.0", tk.END)
        )
        self.master.destroy()