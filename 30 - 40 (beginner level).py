#------Question 31 ---------

# Define a function that can accept an integer number as input and print the "It is an even number"
# if the number is even, otherwise print "It is an odd number".

def checkValue(n):
    if n % 2 == 0:
        print("It is an even number")

    else:
        print("It is an odd number")



checkValue(7)


#------Question 32 ---------
#
# Define a function which can print a dictionary
# where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

def printDict():
    d = dict()
    d[1] = 1
    d[2] = 2 ** 2
    d[3] = 3 ** 2
    print(d)


printDict()


#------Question 33 ---------

# Define a function which can print a dictionary
# where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def printDict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    print(d)


printDict()


#------Question 34 ---------

# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the values only.

def printDict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for (k, v) in d.items():
        print(v)


printDict()

#------Question 35 ---------

# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the keys only.


def printDict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for k in d.keys():
        print(k)

printDict()

#------Question 36 ---------

# Define a function which can generate and print a list
# where the values are square of numbers between 1 and 20 (both included).

def printList():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(li)


printList()


#------Question 37 ---------

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

def printList():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(li[:5])

printList()


#------Question 38 ---------

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.

def printList():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(li[-5:])



printList()


#------Question 39 ---------

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list

def printList():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(li[5:])



printList()


#------Question 40 ---------


# Define a function which can generate and print a tuple
# where the value are square of numbers between 1 and 20 (both included).

def printTuple():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print( tuple(li))



printTuple()