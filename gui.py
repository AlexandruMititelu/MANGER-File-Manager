from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QFileDialog
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
        master.setWindowTitle("Photo Selector")
        master.setGeometry(100, 100, 800, 600)

        # Load saved data
        saved_data = load_data()

        # Create main layout
        self.main_layout = QtWidgets.QVBoxLayout(master)

        # Source Folder Path
        self.source_frame = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.source_frame)
        self.source_label = QtWidgets.QLabel("Source Folder:")
        self.source_frame.addWidget(self.source_label)
        self.source_path = QtWidgets.QLineEdit()
        self.source_frame.addWidget(self.source_path)
        self.source_path.setText(saved_data['source_path'])
        self.browse_source_button = QtWidgets.QPushButton("Browse")
        self.browse_source_button.clicked.connect(self.browse_source)
        self.source_frame.addWidget(self.browse_source_button)

        # Target Folder Path
        self.target_frame = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.target_frame)
        self.target_label = QtWidgets.QLabel("Target Folder:")
        self.target_frame.addWidget(self.target_label)
        self.target_path = QtWidgets.QLineEdit()
        self.target_frame.addWidget(self.target_path)
        self.target_path.setText(saved_data['target_path'])
        self.browse_target_button = QtWidgets.QPushButton("Browse")
        self.browse_target_button.clicked.connect(self.browse_target)
        self.target_frame.addWidget(self.browse_target_button)

        # Input Text
        self.input_frame = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.input_frame)
        self.input_label = QtWidgets.QLabel("Input:")
        self.input_frame.addWidget(self.input_label)
        self.input_text = QtWidgets.QTextEdit()
        self.input_frame.addWidget(self.input_text)
        self.input_text.setPlainText(saved_data['input_text'])

        # Run Button
        self.run_button = QtWidgets.QPushButton("Run")
        self.run_button.clicked.connect(self.run_script)
        self.main_layout.addWidget(self.run_button)

        # Log Output
        self.log_frame = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.log_frame)
        self.log_label = QtWidgets.QLabel("Log:")
        self.log_frame.addWidget(self.log_label)
        self.log_output = QtWidgets.QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_frame.addWidget(self.log_output)

        # Configure logging
        setup_logger(self.log_output)

        # Bind the closing event
        master.closeEvent = self.on_closing

    def browse_source(self):
        folder_selected = QFileDialog.getExistingDirectory(self.master)
        self.source_path.setText(folder_selected)

    def browse_target(self):
        folder_selected = QFileDialog.getExistingDirectory(self.master)
        self.target_path.setText(folder_selected)

    def run_script(self):
        self.run_button.setEnabled(False)
        threading.Thread(target=self._run_script_thread, daemon=True).start()

    def _run_script_thread(self):
        try:
            source_dir = Path(self.source_path.text())
            dest_dir = Path(self.target_path.text())

            if not source_dir.exists():
                raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
            
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            file_names_to_select = read_input_text(self.input_text.toPlainText())
            files_copied = copy_selected_files(source_dir, dest_dir, file_names_to_select)
            
            logging.info(f"Files have been copied successfully! {files_copied} photos have been selected")
        
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
        finally:
            self.master.after(0, lambda: self.run_button.setEnabled(True))

    def on_closing(self, event):
        # Save data before closing
        save_data(
            self.source_path.text(),
            self.target_path.text(),
            self.input_text.toPlainText()
        )
        self.master.close()