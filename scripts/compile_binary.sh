#!/bin/bash

# Compile the binary
#alias run_pyinstaller=$(pyinstaller --onefile -w --icon=img/app_icon.ico --name "MANGER - sort your files" main.py)

# NOTE: An icon file is not supported on Linux. 
# Quote from PyInstaller Terminal Output: "242 WARNING: Ignoring icon; supported only on Windows and macOS!""
pyinstaller --onefile -w --icon=img/app_icon.ico --name "MANGER - sort your files" main.py