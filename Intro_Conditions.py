## I, Introduction to Python
# 1. Hello, Tiffany!
#Statement
#Imagine you are creating a mobile application, and you want it to greet the user at startup.
#In this task, capture the users name from the input and use it to greet the human.

name = input()
print("Hello,", name + "!")

# 2.Pizza
#Statement
#In a restaurant, you ordered a pizza with a diameter of d cm. What is its area?
#Your program receives the diameter as an integer number. Calculate and print the area of the pizza in square cm.
#Output the result as an integer, using built-in function round()

from math import pi

diameter = input()
print(round((int(diameter)/2)**2*pi))

# 3. How many seconds?
#Statement
#The athlete has run the distance in m minutes and s seconds. As input, your program receives two numbers m and s, divided with a line break.
#Calculate how many seconds the athlete was running

m = input()
s = input()
print(int(m)*60+int(s))

# 4.The remainder
#Statement
#You are given an integer number. Print its remainder when divided by 10

number = input()
print(int(number)%10)

# 5.Sum of three digits
#Statement
#The input is a three-digit number. Print the sum of its digits.

number = int(input())
print(int(number//100)+int(number//10%10)+int(number%10))

## Conditions
# 1.Odd or even
#Statement
#Given an integer, print odd if it’s odd and print even otherwise.

a = int(input())
if (a % 2) == 0:
  print("even")
else:
  print("odd")

# 2.Minimum of two numbers
#Statement
#Given two integers, print the least of them.

a = int(input())
b = int(input())
if(a<b):
    print(a)
else:
    print(b)
    
# 3.Sign function
#Statement
#In mathematics, the sign function is a function that extracts the sign of a real number (see wiki)
#Sign function y = sgn(x)
#Implement the sign function! Given floating point number x:
#print 1 if x is positive,
#print -1 if x is negative,
#or print 0 if it’s equal to zero.

a = input()
x = float(a)
if (x>0):
  print(1)
elif (x<0):
  print(-1)
else:
  print(0)

# 4.Larger pizza
#Statement
#Your favorite restaurant offers two pizzas of different diameters. Calculate in which case you will get more pizza:
#if you buy two smaller pizzas,
#or a larger one.
#Pizzas
#The program receives two float numbers as input
#the first is always the diameter of smaller pizzas,
#and the second is the diameter of the larger one.
#Print large if larger pizza is bigger than two smaller ones, small if two smaller pizzas are bigger and print same if two options are equal.

from math import pi

d_small = float(input())
d_large = float(input())

a = pi*((d_small/2)**2)
b = pi*((d_large/2)**2)
if b > (a*2):
  print("large")
elif b < (a*2):
  print("small")
else:
  print("same")
  
# 5.Ascending digits
#Statement
#Given a three-digit integer, print True if its digits are going in ascending order from left to right. Print False otherwise.

a = int(input())
if a//100 < a//10%10 < a%10:
  print("True")
else:
  print("False")
  
# 6.Single positive
#Statement
#Given two non-zero integers, print True if exactly one of them is positive and print False otherwise.

a = int(input())
b = int(input())
if (a>0) != (b>0):
  print("True")
else:
  print("False")
  
# 7.Minimum of three numbers
#Statement
#Given three integers, print the least of them.

a = input()
b = input()
c = input()

if a <= b and a <= c :
    print(a)
elif b <= a and b <= c :
    print(b)
elif c <= a and c <= b :
    print(c)
    
# 8. Knight move
#Statement
#Chess knight can move to a square that is two squares away horizontally and one square vertically, or two squares vertically and one square horizontally.
#Given two different squares of the chessboard, determine whether a knight can go from the first square to the second one in a single move.
#The input is four characters: letters from a to h and numbers from 1 to 8, each specifying the column and the row number. First two are for the first square, and the last two for the second square.
#The program should print True if a knight can go from the first square to the second one in one move. Or print False otherwise.

from_x = input()
from_y = int(input())
to_x = input()
to_y = int(input())
dy = abs(from_y - to_y)
dx = abs(ord(from_x) - ord(to_x))
if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
  print("True")
else:
  print("False")
  
# 9.Leap year
#Statement
#Given the year, check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
#The rules in Gregorian calendar are as follows:
#a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100,
#a year is always a leap year if its number is exactly divisible by 400.
#Warning The words LEAP and COMMON should be printed all caps.

a = int(input())

if (a%4 == 0 and a%100 != 0) or (a%400 == 0) :
    print("LEAP")
else :
    print("COMMON")
    
 # 10.Linear equation
#Statement
#Write a program that solves a linear equation ax = b in integers.
#Given two integers a and b (a may be zero), print
#a single integer root if it exists,
#print no solution if there’s no integer roots,
#print many solutions if there are multiple roots.

a = int(input())
b = int(input())

if a == 0:
  if b == 0:
    print('many solutions')
  else:
    print('no solution')
elif b % a == 0:
  print(b // a)
else:
  print('no solution')
