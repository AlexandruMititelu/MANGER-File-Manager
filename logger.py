import logging
from PySide6 import QtWidgets

class TextHandler(logging.Handler):
    def __init__(self, text_widget: QtWidgets.QTextEdit):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        self.text_widget.append(msg)  # Use append for QTextEdit

def setup_logger(text_widget: QtWidgets.QTextEdit):
    log_handler = TextHandler(text_widget)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.getLogger().addHandler(log_handler)