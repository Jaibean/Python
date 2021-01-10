import shutil
import os



#set where the source of the files are
source = '/Users/jaimiebertoli/Desktop/Folder A'

#set the destination path to folderB
destination = '/Users/jaimiebertoli/Desktop/Folder B'
files = os.listdir(source)

for i in files:
    #We are saying move the files represented by "i" to their new destination
    shutil.move(source+i, destination, copy_function=copy2)
