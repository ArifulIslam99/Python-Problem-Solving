

#------Question 01 ----------- Difficulity (beginner)

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers = []

for i in range(2000, 3201):
    if(i%7 == 0) and (i%5!=0):
        numbers.append(str(i))

print(','.join(numbers))
print('\n')


#------Question 02 ----------- Difficulity (beginner)

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


#------Question 03 ----------- Difficulity (beginner)

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:

n = int(input("Enter Number Range for create square dictionary: "))
dictionary = dict()

for i in range(1, (n+1)):
    dictionary[i] = (i * i)

print(dictionary)