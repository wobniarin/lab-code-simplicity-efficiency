"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
#importing libraries
import random
import sys
import string


#defining functions
def AskUser():

    min_len = int(input('Enter minimum string length: '))
    max_len = int(input('Enter maximum string length: '))
    num_rand_str = int(input('How many random strings to generate? '))

    if min_len > max_len or min_len<0 or max_len <0:
        sys.exit('Incorrect min and max string lengths. Try again.')

    return min_len,max_len,num_rand_str

def RandomStringGenerator(l=12):
    s = ''
    ascii_char = string.ascii_lowercase + string.digits
    for i in range(l):
        s += random.choice(ascii_char)
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        if a < b:
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        r.append(RandomStringGenerator(c))
    print(r)


#playing the game

min_len,max_len,num_rand_str = AskUser()

BatchStringGenerator(num_rand_str, min_len, max_len)
