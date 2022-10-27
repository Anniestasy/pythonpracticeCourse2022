## V. Dictionaries

# 1.Synonyms
#Statement
#The first line you are given is an integer n, followed by n pairs of words. Every word in each pair is a synonym of the other word in the pair.
#After that there’s one more word. Find a synonym for it.
#It’s guaranteed that all words are different and that the last word is present in pairs.

n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

# 2.Swap keys and values
#Statement
#Your program receives a dictionary. Swap dictionary keys with values
#It’s guaranteed that the nesting level of the input dictionary is 1 and that values are immutable.
#If there are several equal values in the dictionary, choose the key that is the first in the alphanumeric order.
#Sort the output in the alphanumeric order.

import json 

data = json.loads(input())

new_dict = {}

for k in data:
  old_value = data[k]

  new_value = new_dict.get(old_value)
  if new_value == None:
      new_dict.update({old_value: k})
  elif new_value > k:
      new_dict.update({new_value: k})

print(new_dict)

# 3.Min value in a dict
#Statement
#You are given a dictionary. Output the key that has the minimum value.
#It’s guaranteed that the nesting level of the dictionary is 1 and minimum value is only one.

import json

data = json.loads(input())

temp = min(data.values())
res = [key for key in data if data[key] == temp]

print(*res)

# 4.Most frequent word
#Statement
#Input of your program is a text in one line.
#Print the word that occurs most often in the text. If such words are multiple, print the first one in alphabetical order.
#Convert all the words to lowercase and ignore commas, full stops and other punctuation marks.

sequence = input().lower().split()
import string
sequence = [''.join(c for c in s if c not in string.punctuation) for s in sequence]
counter = dict()
for word in sequence:
  split_ = word.split()
  for i in split_:
    counter[i]=counter.get(i, 0) + 1
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
most_frequent.sort()
print((most_frequent)[0])

# 5.Elections
#Statement
#The first line of input contains the number of records.
#After that, each entry contains the name of the candidate and the number of votes they got in some state.
#Count the results of the elections: sum the number of votes for each candidate. Print candidates in the alphabetical order.

num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)
    
# 6.Countries and cities
#Statement
#Your program receives a list of countries and cities of each country, and then several city names.
#For each city print the country in which it is located.
#It is guaranteed that every requested city can be found in one the lists, given before.

num_enties = int(input())
cities = {}
for i in range(num_enties):
    line = input().split()
    for city in line[1:]:
        cities[city] = line[0]

for i in range(int(input())):
    print(cities[input()])
    
## VI. Sets

# 1.Number of Distinct Values
#Statement
#Given a list of integers, count how many distinct numbers it has.

a = input().split()

# 2.All Distinct Values
#Statement
#Given a list of integers, output all unique numbers in ascending order.

numbers = input().split()
list_of_unique = []
unique_numbers = set(numbers)
for number in unique_numbers:
    list_of_unique.append(number)
list_of_unique.sort(key=int)
print(' '.join(list_of_unique))

# 3.Intersection
#Statement
#Given two lists of integers, find all the numbers that occur in both the first and the second list. Print them in ascending order.

a = input().split()
b = input().split()
a_set = set(a)
b_set = set(b)
if (a_set & b_set):
    c = a_set & b_set
else:
    print("No common elements")
    
# 4.Difference
#Statement
#Your program receives three lines with integers, separated with spaces.
#Find all the numbers that occur only in first line, but not in the second and third. Print those numbers in ascending order.
#If there are no such numbers, don’t print anything at all.

a = input().split()
b = input().split()
c = input().split()
set_a = set([int(s) for s in a])
set_b = set([int(s) for s in b])
set_c = set([int(s) for s in c]) 

n = set([item for item in a if item not in b])
m = set([item for item in a if item not in c])
print(' '.join(sorted(n & m, key=int)))

# 5.Cardinality
#Statement
#Given two lists of numbers, count how many numbers of the first one occur in the second one.

list1 = input().split()
list2 = input().split()
a = sum(x in list1 for x in list2)

print(a)

# 6.Seen before
#Statement
#Given a sequence of numbers, scan them from left to right and for each number print YES if this number was already seen in the sequence or 
#NO if it appears for the first time.

a = [int(s) for s in input().split()]
seen = set()
for i in a:
  if i in seen:
    print('YES')
  else:
    print('NO')
  seen.add(i)

# 7.Guess the number
#Statement
#Augustus and Beatrice play the following game.
#Augustus thinks of a secret integer number from 1 to n. Beatrice tries to guess the number by providing a set of integers. Augustus answers YES if his secret number is in the provided set, or NO, if it’s not.
#After a few attempts Beatrice, totally confused, asks you to help her determine Augustus’s secret number.
#In the first line, your program receives a positive integer n.
#Then goes a list of numbers (Beatrice’s guess), and Augustus’ response on a separate line. This sequence (a list and an answer) may appear several times.
#Finally, there’s Beatrice’s plea for HELP.
#When Beatrice calls for help, provide a list of all the remaining possible secret numbers, in ascending order, separated with spaces.
#If the list of possible numbers is empty, print nothing.

n = int(input())

possible = set(range(n+1))
while True:
  line = input()
  if line == 'HELP':
    break
  guess = set([int(s) for s in line.split()])
  if input() == 'YES':
    possible &= guess
  else:
    possible -= guess
print(*sorted(possible))

