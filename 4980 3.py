# Part A
# A text file HW3_DataFile_ChangeVariable is provided.
# Change "Thick" value from 1.4 to 5
with open('HW3_DataFile_ChangeVariable.txt','r') as file:
    text = file.read()
    text = text.replace('1.4','5')
with open('HW3_DataFile_ChangeVariable.txt','w') as file:
    print(text)

#Part C
import(pandas) as pd

