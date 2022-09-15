#1 Write a Python class to convert an integer to a roman numeral
#class number1:
#    def conversion(self,num):


#2 Write a Python program to get all possible unique subsets from a set of distinct integers.
#class number2:
#    def



# 3 Write a Python class to reverse a string word by word
# class creation
class number3:
# defining function
    def Uno_reverse(self, s):
        return ' '.join(reversed(s.split()))

print(number3().Uno_reverse('Was it a rat I saw -> palindrome a is sentence previous the fact Fun'))



#4 Write a Python class which has two methods get_String and print_String.
# get_String accepts a string from the user and print_String prints the string in upper case.

class number4:
# class creation
    string = ' '
    def getString(self):
# defining string to get and then print
        self.string = input("Enter a string : ")

    def printString(self):
        print(self.string.upper())

obj = number4()
obj.getString()
obj.printString()
