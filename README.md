
<b>MANGER</b> is a simple and modern file manager that helps me <b>manage the photos </b>that photography clients send me. 


<b>USE CASES</b>: Out of 1000 photos, my clients select 400 photos. They send the file-names. 
Of course, they will have to be: 
-> ordered
-> individually handpicked in Lightroom
-> made sure they are the correct photos
-> made sure there are no missing photos

MANGER solves this problem. It takes the photos, even if the naming is wrong, as long as they have the photo number, and copies them from the 1k photo folder to another folder, renaming them back to original.


Influenced by 37Signals and their product line ONCE. I like their minimalistic approach. And "single use" apps that make you do less, not more. 
This is my first personal project that I use on a regular basis. 


- To just get the last working version of the app:, go to DOWNLOAD_HERE folder, copy it to your machine, and run it. - WINDOWS ONLY FOR NOW. 

- TO build the exe:
pyinstaller --onefile -w --icon=img/app_icon.ico --name "MANGER - sort your files" main.py


<b>TODO</b>:
- Add icons, add name, create a installer + .app for mac
