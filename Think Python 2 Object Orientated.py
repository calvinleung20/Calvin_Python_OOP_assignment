# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:35:46 2019
Think Python Object Oriented Features
@author: caleung
"""

# python is an object oritented progarmming language

#programs include class and method definitions
#computation is expressed in terms of operations on objects
#obecjts reprsent things inthe real world , and methods correspond to the ways things in the real world interact
import datetime


def int_to_time(second):
    minutes, seconds = divmod(second, 60)
    hour, minute = divmod(minutes, 60)
    time = Time1(hour, minute, seconds)
    return time
    


class Time:
    """ Represets the time of day."""
    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

        
        
class Time1:
    def __init__(self, hour = 0, minute = 0 , second = 0):
        """
        Initializes a time object.
        hour: int
        minute: int
        second: int or float 
        
        
        the initialization method is a special method that gets invoked when an object is instantiated
        2 underscore, init, 2 underscore 
        it is common for the parameters of init to have the same names as the attricutes
        
        parameters are optional
        """
        
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    def __add__(self, other):
        """
        by defining special methods, you can specify the behavior on operators on progarmmer defined types
        for example, you can define a method named __add__ for the Time class, and you can use the + operator on tiem objects
        changing the behavior of an operator so that it works with programmer defined types is called operator overloading
        for every operator in python there is a corresponding special method
        
        
        """
        if isinstance(other, Time1):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    #type based dispatch
    """
    This operation is called a type-based dispatch
    because it dispatches the computation to different methods based on the type of the arguments.
    """
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print('%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second))
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other):
        #two time objects, first parmeter is self, second is other
        #to use this method, you have to invoke it on one object and pass the other as an argument
        #reads like end.is after(start) to invoke
        return self.time_to_int() > other.time_to_int()
    def __radd__(self, other):
        return self.__add__(other)
    
start = Time1()
start.hour = 9
start.minute = 45
start.second = 00


#in this use of the dot notation, time is the name of the class and print_time is the name of the method. start 
# is passed as a parameter
Time.print_time(start)
    

#method syntax

start.print_time()

starter = Time1(9, 45)
duration = Time1(1, 15)
print(start + duration)
print(start + 1337)

#int his use of dot notation, print_time is the name of the method again
#start is the object the method is invoked on - called the subject
#just as the subject of a sentence is what the sentence is about, the subject of a method invocation is what the method is about


#by convention, the first parameter of a method is called self, so it would be more common to write print_time liek this

        
        
#the reason for this convention is an implicit metaphor

# the syntax for a function call, print_time(start) suggests that the function is an active agent
#it says something like "hey print time! Heres an object for you to print"

#in object oriented programming- the objets are the active agents. 
# a method invocation like start.print_time() says " hey start, print yourself"

#but by shifting responsibility from the functions onto the objects makes it possible to write more versitable functions or methods
#easier to maintin and reuse code
#def time_to_int(time):
#minutes = time.hour * 60 + time.minute
#seconds = minutes * 60 + time.second
#return seconds

#positional argument is an argument that doesnt have a parameter name, it is not a keyword argument

class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x = 0, y = 0 ,):
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g,%g)' % (self.x, self.y)
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)
    def add_tuple(self, tup):
        return Point(self.x + tup[0], self.y + tup[1])

        
    def add_point(self, other):
        
        return Point(self.x + other.x , self.y + other.y )
    def print_point(self):
        print('(%g,%g)' %(self.x,self.y))
    
    
    
#to instantiate an  object - instance of the class

point1 = Point()
point1.print_point()
print(point1)
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)
print(p2)
print(p1 + p2)
print(p1 + (3, 4))

#the str method is a special method, like __init__, it is supposed to return a string reprsentation of an object


"""
def histogram(s):
d = dict()
for c in s:
if c not in d:
d[c] = 1
168 Chapter 17. Classes and methods
else:
d[c] = d[c]+1
return d
This function also works for lists, tuples, and even dictionaries, as long as the elements of
s are hashable, so they can be used as keys in d.
>>> t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
>>> histogram(t)
{'bacon': 1, 'egg': 1, 'spam': 4}
Functions that work with several types are called polymorphic. Polymorphism can facilitate
code reuse. For example, the built-in function sum, which adds the elements of a
sequence, works as long as the elements of the sequence support additi

If you are not sure whether an object has a particular attribute, you can use the built-in
function hasattr

Another way to access attributes is the built-in function vars, which takes an object and
returns a dictionary that maps from attribute names (as strings) to their values:
>>> p = Point(3, 4)
>>> vars(p)
{'y': 4, 'x': 3}
For purposes of debugging, you might find it useful to keep this function handy:
def print_attributes(obj):
for attr in vars(obj):
print(attr, getattr(obj, attr))
print_attributes traverses the dictionary and prints each attribute name and its corresponding
value.
The built-in function getattr takes an object and an attribute name (as a string) and returns
the attribute’s value.
"""


#exercise 17.2

class Kangaroo:
    def __init__(self, name, contents = None ):
        self.name = name
        # you must set the contents = None 
        # this way you can add a check to see if the contents is None
        #if it is not none, then it will be the intialized content
        #problem here is that the default value for contents, if you set it as a emptly list
        #it will always be referencing back to the empty list
        #default values get evaulated once, when the function is defined
        #they dont get evaulated when the function is called
        if contents == None:
            contents = []
        self.pouch_contents = contents
        
    def __str__(self):
        t = [ self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '      ' + object.__str__(obj)
            t.append(s)
        return '/n'.join(t)
    
    def put_in_pouch(self, item):
        self.pouch_contents.append(item)
    

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
print(kanga)
