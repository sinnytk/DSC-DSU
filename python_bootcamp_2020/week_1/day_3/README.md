# Lecture Notes

<p align="center"><img src="../../banner.jpg"></img></p>

# Python Bootcamp | DSC@DSU

## Week 1, Day 3

By _Tarun Kumar_, **Python@DSU Lead** and Core Team **DSC@DSU**

### Index

- [Functions](<###\ Functions>)
- [Main function](<###\ Main\ function>)
- [Importing scripts into other scripts](<###\ Importing\ scripts\ into\ other\ scripts>)
- [Lists](<###\ Lists>)
- [List Indexing](<###\ List\ Indexing>)
- [Common List Functions](<###\ Common\ List\ Functions>)
- [Iterating over lists](<###\ Iterating\ over\ lists>)
- [List Comprehension](<###\ List\ Comprehension>)
- [List is copy by reference](<###\ List\ is\ copy\ by\ reference>)
- [Tuples](<###\ Tuples>)
- [Destructuring Lists or Tuples](<###\ Destructuring\ Lists\ or\ Tuples>)
- [Strings](<###\ Strings>)
- [String functions](<###\ String\ functions>)
- [Dictionaries](<###\ Dictionaries>)
- [Defining dictionaries](<###\ Defining\ dictionaries>)
- [Accessing dictionaries](<###\ Accessing\ dictionaries>)
- [Updating and adding values to dictionaries](<###\ Updating\ and\ adding\ values\ to\ dictionaries>)
- [Dictionary keys](<###\ Dictionary\ keys>)
- [Dictionary functions and operators](<###\ Dictionary\ functions\ and\ operators>)

Now that we've grown up to know the basic programming structures like loops, conditional statements, primitive data types and giving something as input to a Python script.

Let's move onto structures that I personally think make Python's abstraction powerful as compared to lower-level languages like C/C++ where handling datatypes like arrays prove to be a pain.

### Functions

Before we move onto those, I will introduce a building block of any programming language and that is a **function**.

Defining a function in Python is as sample as:

```python
def function_name(arg1,arg):
```

Now we've gone over the scope of variables previously, however to refresh the concept:

A function will have **read and write** access to:

- All variables defined inside it
- Mutable variables (list, set, dict) passed to it through arguments

A function will have **read only** access to:

- Global variables \*
- Immutable variables (int, bool, float, str) passed to it through arguments \*

* While you can assign values to either global variables and passed immutable variables in a function, their value will stay as a local copy to the variable.

\*\* You can however also modify global variables by initializing `global` keyword on the variable before mutating it, like so:

```python
var = 5

def func():
	var = 6 # global value doesn't change

def func2():
	global var
	var = 24 # global value becomes 24

func()
print(var) # output: 5
func2()
print(var) # output: 24
```

### Main function

Now for those coming from C/C++ might be familiar with the concept of a `main` function which acts as an _entry-point_ to your code. Contrary to that, `main` function doesn't exist for languages like Python or JavaScript since the whole code is essentially an entry-point and in other words a `main` function.

However, worry not, for it is considered a good practice at times to have a `main` function calling other functions and acting as an entry point to your whole code in Python as well.

To emulate a similar concept here we have a special variable called `__name__` that defaults to a constant `'__main__'`

These variables are initialized when executing a script using the interpreter, i.e `python script.py` will initialize the `__name__` variable for that script to `'__main__'`

To execute a specific function i.e the main function, we simply do a if check globally and execute that function. The `main` function that is defined below can be of any name.

```python
def main(): # the name of function can be anything, make sure that name is called tho
	print("Main function")

print("global scope")
if __name__ == '__main__':
	main()

#output
#   global scope
#   Main function
```

```python
# Suppose this is foo.py

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(10))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")

## What will be the output?
```

### Importing scripts into other scripts

You can include existing scripts into your script by using the `import` keyword, you can reference the functions and global variables defined in other scripts.

For example:

Suppose we have two scripts `[foo.py](http://foo.py)` and `[bar.py](http://bar.py)` and they're in the same folder:

```python
./
	|-foo.py
	|-bar.py
./
```

```python
# foo.py
global_variable = 'global'
def is_even(n):
	return n % 2 == 0

def main():
	x = 2
	if is_even(x):
		print(f"{x} is even")
	else:
		print(f"{x} is odd")
if __name__ == '__main__':
	main()

## output
#  2 is even
```

```python
# bar.py
import foo

print(f"Global value in foo.py is {foo.global_variable}")
x=5
if foo.is_even(x): # we can reference the other script's function using .
	print(f"{x} is even")
else:
	print(f"{x} is odd")

## output
#  Global value in foo.py is global
#  5 is odd
```

Question arises, why doesn't `main` function of `[foo.py](http://foo.py)` execute automatically?

And answer is that when you import another script, that script's `__name__` is initialized to it's original name, in this case `foo` and hence the `if` statement fails to call the main function.

Let's modify `[foo.py](http://foo.py)` to print `__name__` if it's not equal to `'__main__'` i.e in the case it's being imported.

```python
#foo.py
...
if __name__ == '__main__':
	main()
else:
    print(__name__)
```

Now if I execute `[bar.py](http://bar.py)` I get a different output

```bash
# before
 Global value in foo.py is global
 5 is odd

# after...
foo #going into else in foo.py and printing __name__
Global value in foo.py is global
5 is odd
```

### Lists

A collection of variables or items in Python is called a list, which is the same as an array in other languages but a Python list can also contain **non-homogeneous** items.

```python
l = [1,2,3]
l = [2,2.3,'abc'] #Python list can contain non-homogeneous items

```

### List Indexing

Just like a normal array, the Python list is **also indexed by `0`**

```python
l = [1,2,3]
l[0] # returns 1
```

However the index `i` doesn't need to be positive integer (i.e ≥ 0), in _Python_ you can use negative integers for reverse indexing, i.e getting elements from end of array.

Negative indexing starts from -1, instead of 0.

i.e

```python
l[-1] #returns last element, 3
l[-2] #returns second last element, 2
l[-4] #index out of range
```

### Common List Functions

- `len`

  ```python
  # no of items in the list
  l = [1,2,3,'str']
  print(len(l)) # returns 4
  ```

- `append`

  ```python
  # adds an item to end of list
  l = [1,2,3]
  l.append(4) # l becomes [1,2,3,4]
  ```

- `extend`

  ```python
  # to extend a list with all items of other list
  l1 = [1,2,3]
  l2 = [4,5,6]
  l1.append(l2) # it's an inplace operation,i.e returns nothing

  # alternatively, you can also use + operator to do out of place extension
  l1 = [1,2,3]
  l2 = [4,5,6]
  l3 = l1+l2  # l1 and l2 are unchanged, l3 becomes [1,2,3,4,5,6]
  ```

- `remove`

  ```python
  # to remove element by value from a list, first found!
  l = [1,2,3,4,4]
  l.remove(4) # again, an in-place operation removes 4 from the list
  # new list becomes [1,2,3,4], the first 4 found is removed
  ```

- `pop`

  ```python
  # to remove an element by it's index and return it, if left empty removes last item
  l = [1,2,3,4]
  a = l.pop(3) # 4 is removed from the list and stored in a, new list becomes [1,2,3]
  ```

### Iterating over lists

There are two ways to iterate over list items:

Conventional index incrementing:

```python
l = [1,2,3,4]
for i in range(len(l)):
	print(i, end=' ')
# output
# 1 2 3 4
```

Using list iterator:

```python
l = [1,2,3,4]
for i in l: # acts in a similar fashion as 'for each' or 'foreach'
	print(i, end=' ')
# output
# 1 2 3 4
```

### List Comprehension

Python provides a syntactic sugar to unpack a list in a single line

```python
l = [1,2,3,4]
even_list = [i for i in l if i%2==0] # even_list has all even items from l
squared_list = [i*i for i in l] # squares every element of l
```

You can check out [https://realpython.com/list-comprehension-python/](https://realpython.com/list-comprehension-python/) for more detailed overview

### List is copy by reference

The datatypes that we discussed in last 1.2 were primitive and were passed by copies, however lists are passed by references to save memory (imagine making copies of a list with million items), which means that `listA = listB` actually means any modifications made to either of references(`listA` or `listB`) will be mirrored because both variables refer to same memory space.

```python
# pass by copy
a=5
b=a
b=6 # a stays 5, b becomes 6

# pass by reference
l1 = [1,2,3]
l2 = l1
l2.pop() # pop is discussed above, it removes given element or last element

# l1 and l2 both become [1,2]
```

## List chunk or slicing

Just like our `range(start, stop, step)` function which produces a list given parameters, in a similar fashion we can also retrieve specific parts of our array and in required format using `list[start:stop:step]`

```python
l = [51,45,234,75,55]


# give me elements starting with index 0 and stop before index 2,
l[0:2] # output: [51,45]
# just like the range function stops before stop

# empty start is defaulted to 0
l[:2] # output: [51,45]

l[:] # [1,2,3,4,5] likewise empty stop is defaulted to length of list

# give even **index** elements (0,2,4)
l[::2] # [51,234,55]

#give odd **index** elements (1,3)
l[1::2] # [45,75]

#step could also be negative, i.e to reverse a list
l[::-1] # [55,75,234,45,51]
# ^ start from 0 add -1 (i.e decrement 1) till

#class activity:
# give last two elements
# write function to skip n elements from start and end

```

### Tuples

Tuples are almost same as Lists, in the sense that they're a collection of items. However key difference is that you cannot mutate a tuple, i.e add or remove items from it after initialization.

```python
# Tuples are defined using round braces instead of square as in lists
a = (1,2)

# however, they're indexed in a similar fashion
print(a[0]) # output 1
```

In a world of lists, a tuple might not make sense at first. But one can use tuples when:

1. Immutability of list contents is required
2. More optimized performance
3. Useful when indexes have semantic meaning. For example `point[0], point[1]` might represent x,y coordinates
4. Objects are heterogeneous, think as if a struct in C/C++ or custom storage

### Destructuring Lists or Tuples

```python
a,b = [1,2]
a,b = (1,2)

# a becomes 1
# b becomes 2
```

### Strings

While we did discuss `str` datatype in our previous session, however we didn't go into the details of it. Strings are basically lists of characters, but in Python there's no `char` datatype, even a single alphabet is a `str` in Python

```python
a = 'a'
type(a) # str
```

- You can use either `''`, `""` and even `''' '''`

Unlike lists however, Python strings are immutable.

```python
name = 'tarun'
print(name[0]) # prints 't'
name[0] = 'b' # error, cannot mutate

```

### String functions

- `lower` and `upper`

  Make all letters lowercase and uppercase, respectively:

  ```bash
  >>> "tarun".lower()
  'tarun'
  >>> "TARUNnn".lower()
  'tarunnn'

  >>> "tarun".upper()
  'TARUN'
  >>> "tArun".upper()
  'TARUN'
  ```

- `islower` or `isupper`

  Returns whether a string is all lower or all upper

  ```bash
  >>> "tarun".islower()
  True
  >>> "taruN".islower()
  False
  >>> "TARUN".isupper()
  True
  ```

- `strip`

  Removes any leading or trailing spaces in a string.

  Will be extensively used as we move forward towards web scraping.

  ```bash
  >>> "    tarun".strip()
  'tarun'
  >>> "  tar un".strip()
  'tar un'
  >>> "tarun\n\n".strip()
  'tarun'
  ```

- `replace`

  Replaces a substring in your string with another substring

  ```bash
  >>> "kumarr".replace("rr","r")
  'kumar'
  >>> "tarun kumar".replace(" ","\t")
  'tarun\tkumar'
  ```

- `find`

  Return index of where a substring is first found in a str (case sensitive)

  ```bash
  >>> quote = 'Let it be, let it be, let it be'
  >>>
  >>> # first occurrence of 'let it'(case sensitive)
  >>> result = quote.find('let it')
  >>> print("Substring 'let it':", result)
  Substring 'let it': 11
  >>>
  >>> # find returns -1 if substring not found
  >>> result = quote.find('small')
  >>> print("Substring 'small ':", result)
  Substring 'small ': -1
  ```

- substring `in` str

  Returns `True` if a substring exists in a string.

  ```bash
  >>> "ta" in "tarun"
  True
  >>> "Ta" in "tarun"
  False
  ```

### Dictionaries

Dictionaries are Python's key-value stores, similar to JavaScript's Object.

Imagine an array which you can index and reference by strings.

Some properties of dictionaries shared by lists.

- Mutable
- Dynamic
- Support for nested elements

### Defining dictionaries

```bash
>>> PSL_teams = {
...             "Islamabad":"Islamabad United",
...             "Karachi":"Karachi Kings",
...             "Lahore":"Lahore Qalandars",
...             "Multan":"Multan Sultans",
...             "Quetta":"Quetta Gladiators",
...             "Peshawar":"Peshawar Zalmi"
...             }
```

### Accessing dictionaries

```bash
>>> PSL_teams["Karachi"]
'Karachi Kings'
>>> PSL_teams["Islamabad"]
'Islamabad United'
>>> PSL_teams["Shikarpur"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Shikarpur'
```

### Updating and adding values to dictionaries

```bash
PSL_teams["Lahore"] = "Lahore Lions"
PSL_teams["Thatta"] = "Thatta Tigers" # creates a new entry
```

### Dictionary keys

While I mentioned above it's good practice to have strings as dictionary keys, however Python doesn't stop you from using:

```bash
# ints
>>> d = {0:"Tarun"}
>>> d[0]
'Tarun'
# floats
>>> d = {1.2:"Tarun"}
>>> d[1.2]
'Tarun'

# however you cannot use mutable objects like lists, dicts as keys
>>> d = {[1,2]:4}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

### Dictionary functions and operators

- `in`

  Check whether a key value pair exists in the dictionary

  ```bash
  >>> "Karachi" in PSL_teams
  True
  >>> "Shikarpur" in PSL_teams
  False
  ```

- `len`

  Find number of key-value pairs in a dict

  ```bash
  >>> PSL_teams
  {'Islamabad': 'Islamabad United',
  'Karachi': 'Karachi Kings',
  'Lahore': 'Lahore Qalandars',
  'Multan': 'Multan Sultans',
  'Quetta': 'Quetta Gladiators',
  'Peshawar': 'Peshawar Zalmi'}

  >>> len(PSL_teams)
  6
  ```

- `get`

  Finds the value for given key otherwise returns a default value. This is used if you're not sure whether a dict contains a key-value pair or not.

  ```bash
  >>> PSL_teams.get("Shikarpur") # returns none, hence nothing printed
  >>> PSL_teams.get("Shikarpur","Not found")
  'Not found'
  ```

- `.keys()` `.values()` and `.items()`

  ```bash
  >>> PSL_teams.keys()
  dict_keys(['Islamabad', 'Karachi', 'Lahore', 'Multan', 'Quetta', 'Peshawar'])

  >>> PSL_teams.values()
  dict_values(['Islamabad United', 'Karachi Kings',
  'Lahore Qalandars', 'Multan Sultans',
  'Quetta Gladiators', 'Peshawar Zalmi'])

  >>> PSL_teams.items()
  dict_items([('Islamabad', 'Islamabad United'),
  ('Karachi', 'Karachi Kings'),
  ('Lahore', 'Lahore Qalandars'),
  ('Multan', 'Multan Sultans'),
  ('Quetta', 'Quetta Gladiators'),
  ('Peshawar', 'Peshawar Zalmi')])
  ```
