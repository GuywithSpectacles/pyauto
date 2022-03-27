import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO" : ['.m4a', '.m4b', 'mp3'],
    "VIDEOS" : ['.mov', '.avi', '.mp4'],
    "IMAGES" : ['.jpg', 'jpeg', 'png']
}

def pickDirectories(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"
#print(pickDirectories('.pdf'))

def organizeDirectory():
        #to check whats in our current working directory is from OS library function "scandir". it will grab every object in our folder and further our goal of grabbing each file extension

    for item in os.scandir():

        if item.is_dir():  #skip
            continue

            #while i grab the files, i should retrieve their paths as well, to get the path of each item we use library "pathlib" and import path function


        filePath = Path(item)

            #Now isolate the suffix and determine what directory it should be organized into
        
        fileType = filePath.suffix.lower() #".suffix" attribute returns the file extension

            #Use the pickDirectory function and pass in "suffix"
        
        directory = pickDirectories(fileType) #once we pass in the file type, directory should now be = category the file belongs to

            #Cast it to a path to help with file movenment

        directoryPath = Path(directory)

            #Now a conditional statement, if a directory the file maps to does not exist, then our script should make a new directory with that name

        if directoryPath.is_dir() != True:
            directoryPath.mkdir()

            #Moving the file into the map directory is independent of the if statement's outcome, and should happen in both scenarios, so lets put it outside the if statement.

        filePath.rename(directoryPath.joinpath(filePath)) # this script allows us to move our file into the directory by changng the file path to join with the directory's path


            #Precautionary measures
            #1) have a function skip, if the item is a directory
            #2) have our pickDirectory function return MISC category if a file type doesn't exist in our current dictionary

    organizeDirectory()