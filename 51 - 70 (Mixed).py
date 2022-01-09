#------Question 51 ---------

# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print(aCircle.area())

#------Question 52 ---------


# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())


#------Question 53 ---------

# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())

#------Question 54 ---------

# Please raise a RuntimeError exception.

raise RuntimeError('something wrong')


#------Question 55 ---------

# Write a function to compute 5/0 and use try/except to catch the exceptions.

def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")

except Exceptionerr:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')


#------Question 56 ---------

# Define a custom exception class which takes a string message as attribute.


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
print(error)

#------Question 57 ---------

# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))

#------Question 58 ---------

# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address.
# Both user names and company names are composed of letters only.


import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))

#------Question 59 ---------

# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

import re
s = input()
print(re.findall("\d+",s))


#------Question 60 ---------


# Print a unicode string "hello world".

s = input()
u = unicode( s ,"utf-8")
print(u)

#------Question 61 ---------

# Write a special comment to indicate a Python source code file is in unicode.

#------------

# -*- coding: utf-8 -*-

#--------------



#------Question 62 ---------

# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)


#------Question 63 ---------

# Write a program to compute:
#
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
#
# with a given n input by console (n>0).


def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))



#------Question 64 ---------

# The Fibonacci Sequence is computed based on the following formula


# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
#
# Please write a program to compute the value of f(n) with a given n input by console.

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))


#------Question 65 ---------

# The Fibonacci Sequence is computed based on the following formula:
#
#
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
#
# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.


def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))




#------Question 66 ---------


# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))

#------Question 67 ---------


# Please write a program using generator to print the numbers
# which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))

#------Question 68 ---------

# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

li = [2,4,6,8]
for i in li:
    assert i%2==0


#------Question 69 ---------


# Please write a program which accepts basic mathematic expression from console and print the evaluation result.

expression = input()
print(eval(expression))


#------Question 70 ---------


# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))









