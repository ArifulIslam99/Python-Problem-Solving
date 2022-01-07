#------Question 23 ---------

# Write a method which can calculate  square value of number

def square(num):
    return num ** 2

print(square(2))


#------Question 24 ---------

# Python
# has
# many
# built - in functions, and if you do not know how to use it, you can read document online or find some books.But Python has a built- in document function for every built- in functions.
# Please
# write
# a
# program
# to
# print
# some
# Python
# built - in functions
# documents, such as abs(), int(), raw_input()
# And
# add
# document
# for your own function


print(abs.__doc__)

print(int.__doc__)

print(input.__doc__)



def square(num):
    '''Return the square value of the input number.

    The input number must be integer.
    '''
    return num ** 2

print(square(2))
print(square.__doc__)



#------Question 25 ---------

# Define a class, which have a class parameter and have a same instance parameter.


class Person:
    name = "Person"

    def __init__(self, name=None):

        self.name = name


jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))


nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))


#------Question 26---------

# Define a function which can compute the sum of two numbers.

def SumFunction(number1, number2):
	return number1+number2

print(SumFunction(1,2))


#------Question 27---------


# Define a function that can convert a integer into a string and print it in console.

def printValue(n):
    print(str(n))

printValue(3)

#------Question 28---------


# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.


def printValue(s1,s2):
	print(int(s1)+int(s2))

printValue("3","4")


#------Question 29---------


# Define a function that can accept two strings as input and concatenate them and then print it in console.

def printValue(s1,s2):
	print(s1+s2)

printValue("3","4")


#------Question 30---------

# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print al l strings line by line.

def printValue(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)

    elif len2 > len1:
        print( s2)

    else:
        print(s1)

        print(s2)



printValue("one", "three")