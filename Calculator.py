import math
import random


def addition():
    print('Please enter the first number you wish to add:')
    add1 = int(input())
    print('Please enter the second number you wish to add to the first number:')
    add2 = int(input())
    print(add1 + add2)
    again()

def substraction():
    print('Please enter the first number you wish to subtract:')
    neg1 = int(input())
    print('Please enter the second number you wish to subtract:')
    neg2 = int(input())
    print(neg1 - neg2)
    again()

def multiplication():
    print('Please enter the first number you wish to multiply:')
    mult1 = int(input())
    print('Please enter the second number you wish to multiply by:')
    mult2 = int(input())
    print(mult1 * mult2)
    again()

def division():
    print('Please enter the first number you wish to divide:')
    div1 = int(input())
    print('Please enter the second number you wish to divide by:')
    div2 = int(input())
    print(div1 / div2)
    again()

def power():
    print('Please enter the first number you wish to multiply by a power:')
    pow1 = int(input())
    print('Please enter the second number you wish to become the power:')
    pow2 = int(input())
    print(pow(pow1,pow2))
    again()

def square(sqr2 = 2):
    print('Please enter the number you wish to square:')
    sqr1 = int(input())
    print(pow(sqr1,sqr2))
    again()

def squareroot():
    print('Please enter the number that you wish to take the square root of:')
    sqrt = int(input())
    print(math.sqrt(sqrt))
    again()

def again():
    print('Do you wish to use the Calculator again? y/n')
    answer = input().lower()
    if answer != ('y', 'n'):
        print('Enter either \"y\" or \"n\" please.')
        again()
    elif answer == 'y':
        calculator()
    else:
        print('Have a Great Day!')


def uInput():
    global choice
    choice = input().upper()
    return choice


def calculator():
    print('Please select which function you would like to use: A = Addition, S = Subtraction, '
          'M = Multiplication, D = Division, P = Power, Q = Square, R = Square Root:')
    if uInput() == 'A':
        addition()
    elif choice == 'S':
        substraction()
    elif choice == 'M':
        multiplication()
    elif choice == 'D':
        division()
    elif choice == 'P':
         power()
    elif choice == 'Q':
         square()
    elif choice == 'R':
         squareroot()
    else:
        print('You have entered an incorrect letter, please try again.')
        calculator()



print('Hello, this is Calculator 1.0, enjoy the scrub coding.')

calculator()

















