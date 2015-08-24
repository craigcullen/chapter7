import os

def run(**args):

    print"[*] In dirlister module."
    files=os.listdir(".")

    return str(files)

# Exposes a run function that lists all files in the current directory and returns the list as a string. 
# Each module you develop should expose a run function that takes a variable number of arguments.
