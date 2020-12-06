# Lecture Notes

<p align="center"><img src="../../banner.jpg"></img></p>

# Python Bootcamp | DSC@DSU

## Week 1, Day 2

By _Bahawal Baloch_, Python@DSU Co-Lead and Core Team member

## Naming Convention

The standard naming convention to be followed through out the Python developers. This is the PEP8 naming convention, for more detailed code guidelines: [PEP8](https://www.python.org/dev/peps/pep-0008/).

[Naming Convention Table](https://www.notion.so/8df8f18fd31340d8a65b2abcf0ebdc91)

## Variables

- Dynamically typed

  ```python
  x = "Hello world"
  x = 1.25
  x = 5
  ```

  - No need to initialize variables with data types, like so:

  ```cpp
  int x = 5;
  ```

### Primitive Datatypes

1. int
2. float
3. string(str)
4. bool

   ```python
   bool(True)
   True

   bool(False)
   False

   bool(1)
   True

   bool(0)
   False

   bool(None)
   False

   bool([])
   False

   bool('')
   False
   ```

### Global vs local scope

In most programming languages, variables, classes and objects (and sometimes functions) have scope where they may be referenced and mutated, Python also has a global and local scope.

- Global variables as their name suggests may be accessed through out the program, however cannot be referenced from a function's local scope.
- Local variables exist within a function's scope and cannot be accessed outside that function.

```python
x = "global"
def foo():
    print("x inside:", x)
foo()
print("x outside:", x)
# Output
#  x inside: global
#  x outside: global
```

```python
x = 5

def foo():
    x = x * 2
    print(x)

foo()

# Output
# UnboundLocalError: local variable 'x' referenced before assignment
```

- Using the `global` keyword you can mutate a global variable in a local scope.

  ```python
  x = 5

  def foo():
      global x
      x = x * 2
      print(x)

  foo()

  # Output
  # 10
  ```

### Printing in Python

- F-strings
- Format()

### Input

![Lecture%20Notes%20ab4cded2c8ea400186b447dadfc415bf/Untitled.png](Lecture%20Notes%20ab4cded2c8ea400186b447dadfc415bf/Untitled.png)

### Casting types

![Lecture%20Notes%20ab4cded2c8ea400186b447dadfc415bf/Untitled%201.png](Lecture%20Notes%20ab4cded2c8ea400186b447dadfc415bf/Untitled%201.png)

### Swapping variables without third variable

In conventional language, you require a intermediate variable to swap variables (unless you involve some integer mathematics)

```python
x=1
y=2

temp = x
x = y
y = temp
# y becomes 1 and x becomes 2
```

```python
x = 5
y = 8
print(x,y)
x,y = y,x
print(x,y)
```

## Control Structure

- `if`

  conditional statement with change the control of program

  if condition is true:

  do this

- `else`

  else if a block of code which is written after an if statement and only execute if the "if" condition is not satisfied

- `elif`

  short for else if

  used to make ladder if else condition

```python
x = int(input())
if x > 5 :
	print("x is greater than 5")
elif x < 5 :
	print("x is less than 5")
else :
	print("x is equal to 5")

```

## Loops

- `for`

  - Use case scenario is when number of iterations are **_known_**

  ```python
  for i in range(100): #do something 100 times, increment value in i
  ```

  - What does `range` function do?

    A function which generates a list (we'll discuss lists in detail tomorrow) in the format required: _(start, end, step)_

    start default is 0, step default is 1

    ```python
    range(5)
    # [0,1,2,3,4]
    ```

    ```python
    range(1,5)
    # [1,2,3,4]
    ```

    ```python
    range(0,5,2):
    # [0,2,4]
    ```

  - Iterating over a collection (again, we'll discuss in detail in next lecture)

    ```python
    l = [1,2,3,4]
    for i in l:
    	print(i)

    # 1,2,3,4
    ```

- `while`

  - Use case scenario is when number of iterations are **_unknown_**

  ```python
  x = 0
  while x < 100:
  	print(x)
  	x+=1

  # same output as **for i in range(100)**
  ```

- `break`, `continue`

  Are control statements to be used when you want to skip an iteration based on some condition or break the loop operation entirely

  - Give some use case of `continue`

  ```python
  for letter in 'Python':
     if letter == 'h':
        continue
     print('current letter :',letter)
  ```

  - Give some use case of `break`

  ```python
  for letter in 'Python':
     if letter == 'h':
        break
     print('current letter :',letter)
  ```
