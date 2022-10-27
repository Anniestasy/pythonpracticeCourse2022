## IX. Classes

# 1.Cat Breed
#Statement
#Let’s add some genetics stuff!
#You have an abstract class CatBase with methods that allow to get cat’s sound, color and weight.
#There are also two mixin (refer the lecture) classes: DomesticCatMixin and LeopardMixin.
#Your task now is to create your own domestic cat almost the same as usual cat, but with leopard color. For this, use CatBase expanded with mixins in proper order.
#For this, finish defining class DomesticCat with parameters using classes inheritance mechanism only.

from abc import ABC, abstractmethod


class CatBase(ABC):

    @abstractmethod
    def get_sound(self):
        ...

    @abstractmethod
    def get_color(self):
        ...

    @abstractmethod
    def get_weight_kg(self):
        ...


class DomesticCatMixin:

    def get_sound(self):
        return 'meow'

    def get_weight_kg(self):
        return 4


class LeopardMixin:

    def get_color(self):
        return 'leopard'

    def get_weight_kg(self):
        return 40


class DomesticCat(DomesticCatMixin, LeopardMixin, CatBase):

    def __str__(self):
        """Return text description of a cat.

        Returns:
            description
        """
        return (
            f'Color: {self.get_color()}, '
            f'weight: {self.get_weight_kg()}, '
            f'sound: {self.get_sound()}'
        )

# 2.Singleton
#Statement
#Singleton is a design pattern that prohibits instantiating the class more than once.
#It can be useful when you want to get the same instance in different places of code during runtime. Or when there’s only one instance needed at a time, like with your computer’s OS.
#Create your own Singleton class in any way you like, but so that it will work like in example below.

class Singleton:

    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance


a = Singleton()
b = Singleton()
print(a is b)

# 3.Summable instances
#Statement
#Here at Quantori Python School, we solve programming problems:) Each problem gives the student from 1 to 10 points.
#There’s a class Problem that represents a coding task. It has member variables statement, example, points.
#Rewrite the class so that mentors can use sum() built-in function on its instances to calculate the full amount of points in the course.

class Problem:
    title = None
    statement = None
    points = None

    def __init__(self, title, statement, points):
        self.title = title
        self.statement = statement
        self.points = points

    def __radd__(self, other):
        return other + self.points

# 4.Ordered Linked List
#Statement
#In classroom, we worked with a singly linked list, a structure in which every node contains the reference to the next node.
#Now you are given a class OrderedLinkedList representing an ordered doubly linked list of integer values. In a doubly linked list, every node contains a link to a previous node, too.
#In OrderedLinkedList, we want the nodes arranged in ascending order of value.
#Implement insert method that adds a new node at the proper location to maintain the sort.
#Method __init__ is already implemented and instantiates a list with one node.
#The first node of the sequence is stored in variable head.

class Node:

    def __init__(self, value, next_node, prev_node):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class OrderedLinkedList:
    head = None

    def __init__(self, value):
        if value:
            self.head = Node(value, None, None)

    def __str__(self):
        string = ""
        current = self.head
        while (current is not None):
            string += " " + str(current.value)
            current = current.next
        return string

    def insert(self, value):
        newNode = Node(value, None, None)
        current = self.head

        if value <= current.value:
            newNode.next = current
            current.prev = newNode
            self.head = newNode
            return self

        while (current is not None):
            nextNode = current.next
            if nextNode is None:
                current.next = newNode
                newNode.prev = current
                return self

            if value > nextNode.value:
                current = nextNode
            else:
                nextNode.prev = newNode
                newNode.next = nextNode
                newNode.prev = current
                current.next = newNode
                return self

        return self
