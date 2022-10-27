## III. Strings

# 1.Palindromes
#Statement
#A palindrome is a sequence that reads the same backwards and forwards.
#You are given a string. Print True if the string is a palindrome and False if it’s not.
#The case of the input string must be ignored.

s = input()
s = s.lower()

if s == s[::-1]:
  print("True")
else:
  print("False")
  
# 2.Number of words
#Statement
#Given a string that consists of words separated by spaces, determine, how many words it has. Word is a group of any non-space symbols.
#https://docs.python.org/3/library/stdtypes.html#string-methods

s = input()

word_list = s.split()
number = len(word_list)
print(number)

# 3.Two Halves
#Statement
#You are given a string. Cut it into two equal parts and print it with the first and second halves swapped.
#If the length of the string is odd, leave the middle character within the first chunk.


s = input()
s = s
# WRITE YOUR CODE HERE
a,b = s[:len(s)//2 if len(s)%2 == 0 else ((len(s)//2)+1):],s[len(s)//2 if len(s)%2 == 0 else ((len(s)//2)+1):]
print(b+a)

# 4.Swap Two Words
#Statement
#Your program receives a string that consists of exactly two words, separated with a space.
#Print a new string with the first and the second words swapped, so that the second word is printed first.
#Consider all adjacent non-space characters a single word.

s = input()
a,b = s.split()
print(b,a)

# 5.First and Second Occurrence
#Statement
#You are given a string that may contain a letter f.
#If the word contains no fs, print -1;
#if there’s only one f in the word, print its index;
#if it occurs twice or more times, print the indexes of two first occurrences.
#In Python, we index from 0:)

s = input()

if s.find('f') >= 0:
  res = []
  for i in range(len(s)):
     if s[i] == 'f':
         res.append(i)
  print(*res[:2], sep = ' ')
else:
  print(-1)
  
# 6.Replace
#Statement
#Your program receives a string with semicolon separated data. Replace all the semicolons with commas.

s = input()
a = s.replace(";", ",")
print(a)

# 7.Delete special character
#Statement
#Given a string, delete all the sequences \n from this string.

s = input()
s = s.replace('\\n', '')
print(s)

# 8.Remove Fragment
#Statement
#You are given a DNA fragment as a string. This string consists of characters A, C, G, T that stand for four types of bases. Spaces may also be included.
#Process the string as described below:
#delete the sequence, enclosed between the first and the last occurrence of A base, including borders.
#It’s guaranteed that A occurs in the input string at least twice and is written as capital letter.

s = input()
ch = "A"
if s.find(ch)>=0:
  f = s.index(ch)
  reversed = s[::-1]
  first_index_in_reversed = reversed.index(ch)
  l = len(s) - first_index_in_reversed
  a = s[:f] + s[l:]
  print(a)
  
# 9.Reverse Fragment
#Statement
#You are given a DNA fragment as a string. This string consists of characters A, C, G, T that stand for four types of bases. Spaces may also be included.
#Process the string as described below:
#reverse the sequence, enclosed between the first and the last occurrence of A.
#It’s guaranteed that A occurs in the input string at least twice and is written as capital letter.

s = input()
ch = "A"
if s.find(ch)>=0:
  f = s.index(ch)
  reversed = s[::-1]
  first_index_in_reversed = reversed.index(ch)
  l = len(s) - first_index_in_reversed
  a = s[f:l]
  b = s[:f]+a[::-1]+s[l:]
  print(b)
  
# 10.Replace in fragment
#Statement
#You are given a DNA fragment as a string, and also a start and an end indexes of it’s subsequence.
#This string consists of characters A, C, G, T that stand for four types of bases. Spaces may also be included.
#Process the string as described below:
#replace all the C characters with T in a subsequence between start and end.
#It’s guaranteed that 0 <= start < end , and both values are within the length of the input string.

s, start, stop = input().split(',')
f = int(start)
l = int(stop)
a = s[(f):(l+1)]
b = s[:f]+a.replace('C','T')+s[(l+1):]
print(b)

# 11.Delete every third character
#Statement
#Given a string, delete every 3-rd character in it.

s = input()
new_s = "" 
for i in range(len(s)):
    if i % 3 != 0:
        new_s = new_s + s[i]
print (new_s)

## IV. Loops

# 1.Mean Value
#Statement
#Your program receives non-empty list of numeric values separated with spaces.
#Calculate and print the mean value, rounding it to two decimal points.

numbers = input().split()
res = list(map(float,numbers))  
print('%.2f' % (sum(res)/len(res)))

# 2.N-th Largest
#Statement
#Your program first receives an integer n and then a list of float values. Print the n-th largest element in the list with one decimal point precision.
#Note: n-th largest, not just n-th element
#Can you come up with an O(n) solution?

numbers = input()
y = numbers.split(' ')
print("%.1f" % (sorted(list(map(float,y[1:])),reverse = True))[(int(y[0])-1)])

# 3.Duplicate Number
#Statement
#Your program receives a list of n + 1 integers, where each integer is in the range from 1 to n inclusive.
#Only one number in this list is repeated twice. Print this number!
#Could you solve it using only O(1) extra space complexity and O(n) time complexity?

numbers = input()
n = len(list(map(int,numbers.split(' '))))-1
a = sum(list(map(int,numbers.split(' ')))) - (((n+1) * n) //2)
print(a)

# 4.First and Last
#Statement
#Your program receives an integer value and a sorted list of integers as input.
#Find indexes of the first and the last occurrence of the given value in the list.
#If the value is not found in the array, print -1 -1.
#Try writing an algorithm with O(log n) complexity.

target, *numbers = map(int, input().split())

x = (target)
n = len(numbers)
def first(numbers, x, n):
    low = 0
    high = n - 1
    res = -1
    while (low <= high):
      mid = (low + high) // 2 
      if numbers[mid] > x:
        high = mid - 1
      elif numbers[mid] < x:
        low = mid + 1
      else:
        res = mid
        high = mid - 1
    return(res)

def last(numbers, x, n):
    low = 0
    high = n - 1
    res = -1
    while(low <= high):
      mid = (low + high) // 2
      if numbers[mid] > x:
        high = mid - 1
      elif numbers[mid] < x:
        low = mid + 1
      else:
        res = mid
        low = mid + 1
    return(res)
print(first(numbers, x, n),last(numbers, x, n))

# 5.Braces
#Statement
#Sometimes you need to check, if data complies with a set of rules. Let’s model such a situation with a sequence of braces.
#A correct sequence of braces follows two rules:
#each brace has a pair,
#each brace is opened and closed in the direction of its pair.
#Print True if the sequence is correct and False if it’s not.

sequence = input()  # a string with any mix of "(" or ")" inside

def check(sequence): 
    open = tuple('({[')
    close = tuple(')}]')
    map = dict(zip(open, close))
    queue = []
    for i in sequence:
        if i in open:
            queue.append(map[i])
        elif i in close:
            if not queue or i != queue.pop():
                return "False"
    if not queue:
        return "True"
    else:
        return "False"
print(check(sequence))

# 6.Flatten a List
#Statement
#Time for a real challenge for your looping skills!
#Your input is a list of lists with unknown nesting level. Could be like:
#[
#    [1, 2],
#    [
#        3,
#        [4, 5],
#    ],
#    6,
#    7,
#]
#Your challenge is to reshape it into a single list like that:
#[1, 2, 3, 4, 5, 6, 7]
#Be careful to preserve the order of the values.
#Input will consist of lists and integers only.
#Try to avoid using library functions, use loops and built-in functions instead.

import json

data = json.loads(input())

def flat(data):
    flatlist = []
    for x in data:
        if type(x) is list:
            flatten = flat(x)
            for x in flatten:
                flatlist.append(x)
        else:
            flatlist.append(x)
    return flatlist
print(flat(data))

