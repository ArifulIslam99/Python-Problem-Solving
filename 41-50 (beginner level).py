#------Question 41 ---------

# With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values in one line and the last half values in one line.

tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)


#------Question 42 ---------

# Write a program to generate and print another tuple
# whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if tp[i]%2==0:
		li.append(tp[i])

tp2=tuple(li)
print(tp2)

#------Question 43 ---------

# Write a program which accepts a string as input to print "Yes"
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

s= input()
if s=="yes" or s=="YES" or s=="Yes":
    print('Yes')
else:
    print('No')


#------Question 44 ---------

# Write a program which can filter even numbers in a list by using filter function.
# The list is: [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)


#------Question 45 ---------

# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(squaredNumbers)

#------Question 46---------

# Write a program which can map() and filter() to make a list
# whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)

#------Question 47 ---------

# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)


#------Question 48 ---------

# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)


#------Question 49 ---------

# Define a class named American which has a static method called printNationality.

class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()


#------Question 50 ---------

# Define a class named American and its subclass NewYorker.


class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)
