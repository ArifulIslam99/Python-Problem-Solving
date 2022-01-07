
#------Question 01 ----------

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers = []

for i in range(2000, 3201):
    if(i%7 == 0) and (i%5!=0):
        numbers.append(str(i))

print(','.join(numbers))
print('\n')


#------Question 02 ---------

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:

def factorial(x):
    if x == 0:
        return 1
    return  x*factorial(x-1)

user_input = int(input("Enter Number to check factorial value: "))
print(factorial(user_input))
print('\n')


#------Question 03 -------

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:

n = int(input("Enter Number Range for create square dictionary: "))
dictionary = dict()

for i in range(1, (n+1)):
    dictionary[i] = (i * i)

print(dictionary)
print('\n')


#------Question 04 --------
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:

values = input('Enter Values: ')
list_converted = values.split(",")
tuple_converted =tuple(list_converted)


print(list_converted)
print(tuple_converted)
print('\n')


#------Question 05 --------

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.



class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input('Enter String Value: ')

    def printString(self):
        print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()






