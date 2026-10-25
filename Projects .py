# File Handling Project

from pathlib import Path
from unicodedata import name
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))         # Recursive glob function to get all files and folders in the current directory 
    for i, items in enumerate(items):
        print(f"{i+1} :  {items}")


def createfile():
    try:
       name =input('Enter your file name :')
       p = Path(name)
       if not p.exists():
           with p.open('w') as fs:
            data =input('what you want to write in this file :-')
            fs.write(data)
           print(F"FILE CREATED SUCCESSFULLLY") 
       else:
           print("Your file already exists")   
    except Exception as e:
        print(f"An error occurred: {e}")


def readfile():
    try:
        readfileandfolder()
        name = input('Enter your file name to read :')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("File read successfully.")
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def updatefile():
    try:
        readfileandfolder()
        name = input('Enter your file name to update :')
        p = Path(name)
        if p.exists() and p.is_file():
            print('press 1 for changing the name of file')
            print('press 2 for overwriting the data of your file')
            print(' press 3 for appending some content in your file')

            res = int(input('enter your choice :'))
            if res == 1:
                name = input('enter your new file name :')
                p2 = Path(name)
                p.rename(p2)
            if res ==2:
                with open(p,'w') as fs:
                    data = input('what you want to write in this file :-')
                    fs.write(data)
            if res ==3:
                with open(p,'a') as fs:
                    data = input('what you want to append in this file :-')
                    fs.write(" "+data)            
            
    except Exception as e:
        print(f"An error occurred: {e}")

def deletefile():
    try:
        readfileandfolder()
        name = input('Enter your file name to delete :')
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted successfully.")
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")            
                    


print("Welcome to the File Handling Project")
print("Please select an option:")
print('press 1 for creating a file')
print('press 2 for reading a file')
print('press 3 for updating a file')
print('press 4 for deleting a file')

check = int(input('enter your choices :'))

if check ==1:
    createfile()

if check ==2:
    readfile()

if check ==3:
    updatefile()

if check ==4:
    deletefile()
    