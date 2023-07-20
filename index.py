from zipfile import ZipFile
import os
import re

def cleanFileName(file_name):
    file_name = file_name or ""
    dotSplit = file_name.split(".")
    name = dotSplit[0]
    extension = len(dotSplit) > 1 and "."+dotSplit[1] or ""

    name = re.sub("\(\d*\)", "", name, 999)

    while (name.rfind(" ") == len(name)-1 and len(name) > 0):
        name = name[0:len(name)-1]

    return name+extension




AppName = "React Native Demo"

IPA = ZipFile("./output/"+AppName+".ipa", "w")
for file_name in os.listdir("./input"):   
    IPA.write("./input/"+file_name, "/Payload/"+cleanFileName(file_name))