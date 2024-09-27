File Manager is a simple app that helps me manage the photos that photography clients send me. 
Example: Out of 1000 photos, my clients send 400 photos. Not the RAW files, but their file names. Of course, they might not be ordered, so I would need to sort them. Then I would need to handpick each in Lightroom so I can start editing them. 
File Manager solves this problem. It takes the photos, even if the naming is wrong, as long as they have the photo number, and copies them from the 1k photo folder to another folder, renaming them back to original.


- To just get the last working version of the app:, go to the dist folder, copy it to your machine, and run it.

- TO build the exe:
pyinstaller --onefile --windowed --icon=icon.ico --name "File Manager" main.py

