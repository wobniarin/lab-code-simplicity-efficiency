"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

import sys

######## Function definition

def WelcomeMessage():

    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers from zero to five')

def Validation(a,b,c):

    num_dict = {'zero':0, 'one':1, 'two':2, 'three': 3, 'four': 4, 'five': 5}

    if a not in num_dict and b!= 'plus' or b!='minus' and c not in num_dict:
       sys.exit("I am not able to answer this question. Check your input. Terminating Program.")
    return num_dict[a],b,num_dict[c]

def AskUser():

    a = input('Please choose your first number (zero to five): ')
    b = input('What do you want to do? plus or minus: ')
    c = input('Please choose your second number (zero to five): ')

    num_a, op_b, num_c = Validation(a,b,c)

    return num_a, op_b, num_c

def Game(num_a,op_b,num_c):

    if op_b == 'plus':
        result = num_a + num_c
    else:
        result = num_a - num_c

    res_dict = {-5: 'negative five', -4: 'negative four', -3: 'negative three', -2:'negative two', -1: 'negative one',
                0: 'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
                10: 'ten'}

    print(f"{res_dict[num_a].capitalize()} {op_b} {res_dict[num_c]} equals {res_dict[result]}")
    print("Thanks for using this calculator, goodbye :)")




####### Game


WelcomeMessage()  #print welcome message

a,b,c = AskUser() #ask user the inputs and validates them

Game(a,b,c)  #play the game


