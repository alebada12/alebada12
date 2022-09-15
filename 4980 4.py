# I could not get the program to search my directory with user input for part A
# Since I couldn't get it to work and I don't want to error out Part B/C
# I'm leaving what I had as a note
# Part A
#import os
#filename = input("Enter the name of the file you wish to search for:")



# Part B
# Write a Python code that can search a specific file and change the name of the file and
# then move or copy the file in a specific directory. (3 points)

# "Module [that] offers a number of high-level operations on files and collections of files"
# Quoted from python docs
import shutil
# So I can read files on my OS (Linux)
import os
# 2 different files in different directory than PyCharm
f = os.path.join('/home/anthonylebada/Downloads', 'Default.txt')
f2 = os.path.join('/home/anthonylebada/Downloads', 'NewDefault.txt')
# rename(first file, second file)
os.rename(f, f2)
# new location path
newlocation = '/home/anthonylebada/Desktop'
# shutil module that move file location
mover = shutil.move(f2, newlocation)
print("NewDefault.txt moved from /Downloads to:", mover)

# Part C
# Write a simple Python code that can take input from an external file (txt or csv). (3 points)

number = int(72)
f = open('/home/anthonylebada/Downloads/HW4 Input.txt', 'r')
print(f.read())
if number == 72:
        output = int(72+10-3*5)
print("Seventy two now equals", output)