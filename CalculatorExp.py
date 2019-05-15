import math
import sys

class Error(Exception):
    """Base class for custom exceptions"""
    pass

class InvalidError(Error):
    """Raised when an incorrect value is given"""
    pass

def addition():
    print('Please enter the first number you wish to add:')
    add1 = int(input())
    print('Please enter the second number you wish to add to the first number:')
    add2 = int(input())
    print(add1 + add2)

def substraction():
    print('Please enter the first number you wish to subtract:')
    neg1 = int(input())
    print('Please enter the second number you wish to subtract:')
    neg2 = int(input())
    print(neg1 - neg2)

def multiplication():
    print('Please enter the first number you wish to multiply:')
    mult1 = int(input())
    print('Please enter the second number you wish to multiply by:')
    mult2 = int(input())
    print(mult1 * mult2)

def division():
    print('Please enter the first number you wish to divide:')
    div1 = int(input())
    print('Please enter the second number you wish to divide by:')
    div2 = int(input())
    print(div1 / div2)

def power():
    print('Please enter the first number you wish to multiply by a power:')
    pow1 = int(input())
    print('Please enter the second number you wish to become the power:')
    pow2 = int(input())
    print(pow(pow1,pow2))

def square(sqr2 = 2):
    print('Please enter the number you wish to square:')
    sqr1 = int(input())
    print(pow(sqr1,sqr2))

def squareroot():
    print('Please enter the number that you wish to take the square root of:')
    sqrt = int(input())
    print(math.sqrt(sqrt))


def uInput():
    global choice
    choice = input().upper()
    return choice

print('Hello, this is Calculator 1.0, enjoy the scrub coding.')


while True:
    try:
        print('Please select which function you would like to use: A = Addition, S = Subtraction,\nM = Multiplication, D = Division, P = Power, Q = Square, R = Square Root:')
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
             square(sqr2= 2)
        elif choice == 'R':
             squareroot()
        elif choice != ('A', 'S', 'M', 'D', 'P', 'Q', 'R'):
            raise InvalidError
    except InvalidError:
        print('Please enter a valid key')
        print()
    else:
        while True:
            ans = input('Would you like to continue using CalculatorExp? y/n ').lower()
            try:
                if ans == 'y':
                    break
                elif ans == 'n':
                    print('Have a great day!')
                    sys.exit()
                elif ans != ('y', 'n'):
                    raise InvalidError
            except InvalidError:
                print('Please enter either y or n.')
                print()






























