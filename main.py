from PySide6 import QtWidgets
from gui import PhotoSelectorGUI
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    gui = PhotoSelectorGUI(main_window)
    main_window.show()
    sys.exit(app.exec())