import os

fName = 'Hello.txt'

fPath = 'C:\\Users\\Miles\\Documents\\GitHub\\Basic-Python-Projects\\A'

abPath = os.path.join(fPath, fName)

print(abPath)
