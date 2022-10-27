## VII. Functions

# 1.Multiplication
#Statement
#This is a simple task, we just want to make sure everything works with you:)
#Define simple function named multiply. Function must take two integers as arguments and return their multiplication as a result.

def multiply(a, b):
    return a * b
    
# 2.Reverse
#Statement
#Define function reverse with arbitrary number of positional parameters.
#Function should return taken arguments in the reverse order.

def reverse(*args):
    return args[::-1]

# 3.Luke String
#Statement
#Define function named catchphrase() with three string params:
#name,
#villain_name ,
#place .
#villain_name and place should be predefined with values the Emperor and the galaxy.
#Function should return a string:
#"<name>, you can destroy <villain_name>. He has foreseen this. It is your destiny. Join me, and together we can rule <place> as father and son."

def catchphrase(name, villain_name='the Emperor', place='the galaxy'):
    str = '{}, you can destroy {}.'\
        ' He has foreseen this. It is your destiny.'\
        ' Join me, and together we can rule {} as father'\
        ' and son.'.format(name, villain_name, place)
    return str

# 4.Mean Value
#Statement
#You already know how to calculate the mean value of a sequence.
#Now define a function named mean() which accepts arbitrary number of float values and returns their mean value with two decimal places precision.
#Function being called without arguments should return None.

def mean(*n):
    sums = 0
    for t in n:
        sums = sums + t
    if len(n) > 0:
        a = sums / len(n)
        return round(a, 2)
    return None
  
# 5.Throttler
#Statement
#Imagine you have a web server which accepts requests from users.
#Write a function that accepts
#names of users who want to make a request, as positional arguments,
#names of users, whose requests are processed right now, with estimated times of response, as keyword arguments.
#Write a function throttler() that counts the overall estimated time of your server response.
#If the estimated time for current requests is less than 1 second, return accept so that new requests are accepted.
#If estimated time reaches 1 second or more, return decline so that server will refuse to handle new requests.
#Numbers of both positional and keyword arguments is unknown.

def throttler(*request, **processed):
    for key, value in processed.items():
        if sum(processed.values()) < 1:
            return 'accept'
        return 'decline'

# 6.Subsequence
#Statement
#A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. Thus, [2, 6, 3, 9] is a subsequence of the [1, 0, 2, 1, 6, 3, 9].
#Your function receives a list of integers. Return the length of the longest strictly increasing subsequence.

def subsequence(numbers):
    n = len(numbers)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if numbers[i] > numbers[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return maximum
  
# 7.Tic Tac Toe
#Statement
#You are given a nested list with which represents the tic-tac-toe game:
#[[    1, None,  None ],
#[  None,    0,     1 ],
#[  None,    0, None ]]
#Which stands for:
#Tic-tac-toe input
#It’s your turn!
#Write the function next_move() which will accept the input list and put 1 in any free cell.
#Your function must return nothing, but mutate the input structure instead.

def next_move(field: list):
    move_made = False
    for i in range(len(field)):
        for k in range(len(field[i])):
            if field[i][k] is None and not move_made:
                move_made = True
                field[i][k] = 1

# 8.Closure
#Foreword
#In Python, functions are first class citizens. It means that functions are passed around and manipulated just like other kinds of objects (say, integers or strings).
#So, in Python you can assign a function to a variable, pass it as an argument to another function, etc.
#Let’s try to do so!
#Statement
#Define function closure that takes number as an argument and returns a function.
#The returned function should also take number and return multiplication of taken number and number taken by mother function. This programming technique is called closure.

def closure(n: int):
    def mult(k):
        return n * k
    return mult
  
## VIII. Decorators

# 1.Time it!
#Statement
#In your project, you have a lot of functions, that normally take a long time to run.
#Write a decorator time_logger that measures how much time a function uses to compute its result.
#This decorator should print the time in seconds with 6 decimal places precision and have no return value.
#Our tests will call some CPU intensive function with your decorator and compare the time elapsed.

from time import time
from functools import wraps


def time_logger(func):
    @wraps(func)
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'{(t2-t1):.6f}')
        if result is True:
            return (None)
        else:
            return result

    return wrap_func
  
# 2.Lowercase it!
#Statement
#In your project, you have a lot of functions that always return strings.
#Write a decorator lowercase that converts these functions outputs to lower case.

def lowercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper


@lowercase
def lorem_ipsum():
    return "LOREM IPSUM DOLOR SIT AMET"

# 3.Security check
#Statement
#Function get_money uses parameters owner_id and amount to withdraw money from user’s online wallet. It’s not checking anything, just performs the transaction.
#Now we want to protect users wallets from unauthorised access without modifying get_money() itself.
#Write a decorator security_check that accepts parameter current_user_id. This parameter identifies someone who wants to access the money.
#If it was the owner who tried to get the money, function should return string:
#Succesful transaction. Sum: {amount}
#And decorated function should return string Access denied if current_user_id is not the same as owner_id.
#Our tests will just call the decorated get_money() function with different parameters. Please, only change the decorator
#security_check in this task, because our tests use the code in the template:)

from uuid import uuid4

user_id = uuid4().hex


def security_check(current_user_id):
    def inner_decorator(f):
        def wrapped(owner_id, *args, **kwargs):
            if owner_id not in user_id:
                return ('Access denied')
            else:
                return f(owner_id, *args, **kwargs)
        return wrapped
    return inner_decorator


@security_check(user_id)
def get_money(owner_id, amount):
    ...  # performing the transaction
    return f'Successful transaction. Sum: {amount}'

# 4.Transpose the note
#Statement
#There are seven notes of music and seven letters below are often used to represent them:
#Note	Symbol
#Do	c
#Re	d
#Mi	e
#Fa	f
#Sol	g
#La	a
#Si	h
#Let there be notes in the “note-octave” string format with 7 possible octaves in total:
#"c1": Do of the 1st octave,
#"d1": Re of the 1st octave,
#"g1": Sol of the 1st octave,
#"c2": Do of the 2nd octave,
#"a5": Mi of the 5th octave.
#You have a predefined function get_note() that returns a note in the specified format.
#Write a decorator with parameter that changes the octave and returns a note.
#We call the decorator with an integer parameter that denotes how to change the input note:
#0: do not change at all,
#1: one octave up,
#-3: three octaves down,
#etc.
#This is how this call might look:
#from random import choice
#@transpose(2)  # parameter 
#def get_note():
#    note = choice(['c', 'd', 'e', 'f', 'g', 'a', 'h'])
#    octave = choice(range(1, 8))
#    print(f"Initial: {note}{octave}")
#    return f"{note}{octave}"
#returned = get_note()
#print(f"result: {returned}")
#You cannot move the note below the 1st octave and above the 7th octave.
#Define the transpose decorator.

def transpose(param):
    def inner(func):
        def wrapper(*args, **kwargs):
            note = func(*args, **kwargs)
            octave = int(note[1])
            result_octave = octave + param
            if result_octave > 7:
                result_octave = 7
            if result_octave < 1:
                result_octave = 1
            return note[0] + str(result_octave)
        return wrapper
    return inner

# 5.Chaining decorators
#Statement
#In your NLP project, you have two functions that produce texts: one of them produces random poetry, and the other produces funny titles for it.
#Suppose you want to print these texts in bold, italic or both without changing the generating code.
#If we want to print Lorem ipsum in italic, we add html-tags:
#<i> in the beginning of the italicized text,
#and </i> in the end:
#'<i>Lorem ipsum</i>'
#For bold we use:
#'<b>Lorem ipsum</b>'
#Write a decorator @bold that makes your text bold and @italic that makes it italic.
#Use these decorators to return verses in italic, and titles in both italic and bold.

def bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper


def italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper


@italic
def verse():
    """ Returns example verse """
    text = "It's no baloney, " \
           "It ain't a phoney " \
           "My cellular " \
           "Bananular phone!"
    return text


@bold
@italic
def title():
    """ Returns example title """
    text = "Bananaphone"
    return text

# 6.Caching deco
#Statement
#Suppose you have a computation-heavy function, which you may call with the same arguments many times.
#It would be useful to cache the function parameters with the results so that you can get result without calling the function if you already have calculated it before.
#Write a decorator cache that returns the result immediately if the decorated function is called with values it was already called before. And runs the function otherwise.
#PyCharm or other IDE that you like will help you with debugging.

from random import randint
from time import sleep


def cache(func):
    cache_ = dict()

    def cache_func(*args):
        if args in cache_:
            return cache_[args]
        result = func(*args)
        cache_[args] = result
        return result

    return cache_func


@cache
def cpu_intensive_func(*args):
    """ Does something with args for a long time """
    sleep(randint(1, 3))
    # return some result just for the demo
    return sum(args)

