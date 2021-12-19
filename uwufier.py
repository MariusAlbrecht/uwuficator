import os

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
    
    text = text.replace("L", "W")
    text = text.replace("R", "W")
    text = text.replace("l", "w")
    text = text.replace("r", "w")
    text = text.replace("th", "d")
    text = text.replace("ove", "uv")

    return text
                    
def uwufiable(filepath, extensions, avoids):
    for avoid in avoids:
            if avoid != filepath:
                for extension in extensions:
                    if extension in filepath:
                        return True
    return False