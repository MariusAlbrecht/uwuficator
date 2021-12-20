import os
import re

def fileUwufy(path = ""):
    with open(os.path.join(path), "r") as file:
        textToConvert = file.read()
        file.close()
        with open(os.path.join(path), "w") as writefile:
            writefile.write(uwufy(textToConvert))
            writefile.close()

def directoryUwufy(path = "", extensions = ['.txt','.md'], avoids = ["README.md"]):
    paths = os.listdir()
    for filepath in paths:
        if(uwufiable(filepath, extensions, avoids)):
            with open(os.path.join(path, filepath), "r") as file:
                textToConvert = file.read()
                file.close()
                with open(os.path.join(path, filepath), "w") as writefile:
                    writefile.write(uwufy(textToConvert))
                    writefile.close()

def uwufy(textToConvert):
    text = str(textToConvert)
    
    if(len(findLink(textToConvert)) == 0):
        text = text.replace("L", "W")
        text = text.replace("R", "W")
        text = text.replace("l", "w")
        text = text.replace("r", "w")
        text = text.replace("th", "d")
        text = text.replace("ove", "uv")
    
    return text

def findLink(string): #taken from https://www.geeksforgeeks.org/python-check-url-string/
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
            
def uwufiable(filepath, extensions, avoids):
    for avoid in avoids:
            if avoid != filepath:
                for extension in extensions:
                    if extension in filepath:
                        return True
    return False