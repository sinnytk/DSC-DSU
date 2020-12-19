# DSC-DSU | Python Bootcamp 2020

<p align="center"><img src="../../banner.jpg"></img></p>

## Week 2, Day 1 (File system, filing and CSV)

By _Tarun Kumar_, **Python@DSU Lead** and Core Team **DSC@DSU**

As we move towards the usefulness of a programming language in real-life applications, filing is one of the important aspect that comes to our mind.

If you come languages like C/C++, Java or JavaScript even, filing is relatively easier in Python.

But before we get into handling individual files, let's explore how we interact with an operating system's file system using the `os` module.

`os` is a builtin Python library that as the name suggests contains various functions and attributes to work with your operating system.

### Functions with default parameters

I forgot to discuss default parameters in the previous lecture notes. Simply, these are parameters that may take a default value for a function if they're not passed through the calling function.

e.g

```bash
>>> def foo(name="Tarun"):
...     print(name)
...
>>> foo("Kumar")
Kumar
>>> foo()
Tarun
```

### Working with directories in `os`

One thing to remember is when you execute any Python script, interactive notebook or shell, the working directory defaults to the folder where the script exists. We can use this working directory to relatively refer to different directories in the file system.

To start working with the `os` module, we need to import the library using a `import os` statement at top of our script.

Some cool functions that `os` library has:

- `os.getcwd()`

  Return a string representing the current working directory.

  ```bash
  >>> os.getcwd()
  '/home/tarun'
  ```

- `os.listdir(path=".")`

  Lists all the files and folders of the given path, by default returns the files and folders of current working directory.

  ```bash
  >>> os.listdir()
  ['week_3', 'smart_questioning_guidelines.md',
   'week_2', 'banner.jpg', 'test.html', 'week_4',
   'overview_timetable.md', 'README.md', 'timetable.md', 'week_1']

  >>> sorted(os.listdir()) # sorted() function sorts a given list
  ['README.md', 'banner.jpg', 'overview_timetable.md',
   'smart_questioning_guidelines.md', 'test.html', 'timetable.md',
   'week_1', 'week_2', 'week_3', 'week_4']
  ```

- `os.walk(top=".")`

  Walk a given path in top-down (or bottom-up) fashion. In other words, print all files and folders in root then go into each folder and repeat.

  ```python
  for folder, subfolders, filenames in os.walk('/home/tarun/Tarun/DSC@DSU'):
      print(f'The current folder is {folder}')

      for subfolder in subfolders:
          print(f'SUBFOLDER OF {folder}: {subfolder}')

      for filename in filenames:
          print(f'FILE INSIDE {folder} : {filename}')

      print("\n")
  ```

  ```bash
  The current folder is /home/tarun/Tarun/DSC@DSU
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: Git_assets
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: Social Media Kit
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: SilabGit
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: .ipynb_checkpoints
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: github_repos
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: Hit-With-Git-Feedback
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: dsc-certificate-generator
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: notion_lecture_notes_tools
  SUBFOLDER OF /home/tarun/Tarun/DSC@DSU: hit_with_git_github
  FILE INSIDE /home/tarun/Tarun/DSC@DSU : Frame-34609.png
  FILE INSIDE /home/tarun/Tarun/DSC@DSU : Git.osp
  FILE INSIDE /home/tarun/Tarun/DSC@DSU : Final.mp4
  ```

  Skipping specific folders or directories in `os.walk`:

  While traversing in topdown fashion(default behavior of os.walk), you can modify the subfolders list **in-place** to filter out that subdirectory from being traversed.

  list[:] ensures we reference the original list instead of assigning the variable with the new list's memory.

  ```bash
  >>> lA = [1,2,3]
  >>> lB = [4,5,6]
  >>> lC = [7,8,9]
  >>> lB = lA
  >>> lA.append(5)
  >>> lB
  [1, 2, 3, 5]
  >>> lA
  [1, 2, 3, 5]
  >>> lA = lC
  >>> lA
  [7, 8, 9]
  >>> lB
  [1, 2, 3, 5]

  >>> lA = [1,2,3]
  >>> lB = [4,5,6]
  >>> lC = [7,8,9]
  >>> lB = lA
  >>> lA.append(5)
  >>> lB
  [1, 2, 3, 5]
  >>> lA
  [1, 2, 3, 5]
  >>> lA[:] = lC
  >>> lA
  [7, 8, 9]
  >>> lB
  [7, 8, 9]
  ```

  ```bash
  for folder, subfolders, filenames in os.walk('/home/tarun/Tarun/DSC@DSU'):
      subfolders[:] = [subfolder for subfolder in subfolders if subfolder!='.git']
  		print(f'The current folder is {folder}')

      for subfolder in subfolders:
          print(f'SUBFOLDER OF {folder}: {subfolder}')

      for filename in filenames:
          print(f'FILE INSIDE {folder} : {filename}')

      print("\n")
  ```

Class activity:

- Sort files based on their extensions
- Use os

### Handling different OS paths using `pathlib`

As you might've noticed from my notes, I primarily use Linux which uses forward slashes `/` as representation of path directory, while Windows systems use back slashes `\`

- You should use forward slashes with pathlib functions. The Path() object will convert forward slashes into the correct kind of slash for the current operating system. Nice!

To read up more on the module, I found this Medium article to be helpful: [https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f](https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f)

### Reading files with `open`

Reading files in Python is extremely easy, you can open an existing file using a function called `*open(filepath)*`

```bash
>>> f = open('timetable.md')
>>> f
<_io.TextIOWrapper name='timetable.md' mode='r' encoding='UTF-8'>

>>> f = open("timetable2.md")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'timetable2.md'
```

**By default**, the file (if it exists in the current working directory or specified path) opens up in read mode, that is you can only read the file contents but not modify them.

### Different file modes

`"r"` - Read - Default value. Opens a file for reading, error if the file does not exist

`"a"` - Append - Opens a file for appending, creates the file if it does not exist

`"w"` - Write - Opens a file for writing, creates the file if it does not exist

`"x"` - Create - Creates the specified file, returns an error if the file exists, you can also write in the created file, but not read

Some advanced modes to remember:

- Read and write the file (but also truncate or create if doesn't exist): `w+`
- Read and write the file (without truncate or creation): `r+`
- Read and write the file (create file but append at last if it exists): `a+`

### Reading files

You can read a file at once using `file.read()`

**Class activity: do the song example with filing this time.**

### CSV Files

Humans seek structure in whatever they use and CSVs are the easiest and most commonly used flat database storage structure today.

The magic's in the name. Comma-separated value files are one of the best ways to represent and store tables of data, like so.

![Lecture%20Notes%2084b61ffb043f4d6f9a0513bee92d74ec/Untitled.png](Lecture%20Notes%2084b61ffb043f4d6f9a0513bee92d74ec/Untitled.png)

To view CSV files you can use Excel, LibreOffice Calc, Google Sheets or any other spreadsheet parsing reader.

Which may look like this:

![Lecture%20Notes%2084b61ffb043f4d6f9a0513bee92d74ec/Untitled%201.png](Lecture%20Notes%2084b61ffb043f4d6f9a0513bee92d74ec/Untitled%201.png)

In raw format, CSV files look like this:

![Lecture%20Notes%2084b61ffb043f4d6f9a0513bee92d74ec/Untitled%202.png](Lecture%20Notes%2084b61ffb043f4d6f9a0513bee92d74ec/Untitled%202.png)

So it means you can write files as you normally would using loops, but this time only appending commas at the end of each separation, right?

Let's try it.

```bash
>>> f = open("sample.csv")
>>> a = f.read()
>>> a
',Name,Age,Semester\n,Tarun,201,7\n,Bahawal,22,7\n'

>>> f = open("sample.csv","a")
>>> f.write(",Zain,26,7\n") # file comma is to leave first col empty

>>> f = open("sample.csv")
>>> a = f.read()
>>> a
',Name,Age,Semester\n,Tarun,21,7\n,Bahawal,22,7\n,Zain,26,7\n'
```

**Class activity: output multiplication tables**

### `with` keyword

Sometimes we require access to a resource only for single time or for a limited access. Python provides a with keyword to automatically delete resources after they're consumed within a block of a code.

Like so.

### `csv` module

As common as CSV reading and writing are, Python developers decided to include a builtin module to support and simplify CSV operations using the `csv` module.

### Reading CSV files with `csv.reader`

```python
import csv

with open('sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {row}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is {row[1]} years old, and is currently in semester {row[2]}.')
            line_count += 1
```

```bash
Column names are ['', 'Name', 'Age', 'Semester']
	Tarun is 21 years old, and is currently in semester 7.
	Bahawal is 22 years old, and is currently in semester 7.
	Zain is 26 years old, and is currently in semester 7.
```

### Writing csv files with `csv.writer`

You can also write into CSV files in a similar fashion.

```python
import csv

with open('sample.csv', mode='a') as friends:
    friends_writer = csv.writer(friends, delimiter=',')

    friends_writer.writerow(['', 'Hamza Fayyaz', '22', '7'])
    friends_writer.writerow(['', 'Syed Ali', '25', '7'])
```

### Reading and writing into `dict` with `DictReader` and `DictWriter`:

CSV module also provides classes to read and write using dictionaries, which make for a ton of readability and convenient data pipeline modeling.

- Using `DictReader` to automatically read columns and create dictionaries of each row:

```bash
>>> import csv
>>> with open('sample.csv', mode='r') as friends:
...     friends_reader = csv.DictReader(friends)
...     for friend in friends_reader:
...         print(friend)
...
{'': '', 'Name': 'Tarun', 'Age': '21', 'Semester': '7'}
{'': '', 'Name': 'Bahawal', 'Age': '22', 'Semester': '7'}
{'': '', 'Name': 'Zain', 'Age': '26', 'Semester': '7'}
{'': '', 'Name': 'Zain', 'Age': '26', 'Semester': '7'}
{'': '', 'Name': 'Hamza Fayyaz', 'Age': '22', 'Semester': '7'}
{'': '', 'Name': 'Syed Ali', 'Age': '25', 'Semester': '7'}

#first key and value is empty due to empty column
>>> friends_reader.fieldnames
['', 'Name', 'Age', 'Semester']
```

- Using `DictWriter` to automatically map a dictionary to corresponding columns

```bash
>>> with open('sample.csv', mode='a') as friends:
...     friends_writer = csv.DictWriter(
...         friends, fieldnames=["", "Name", "Age", "Semester"])
...     friends_writer.writerow(
...         {"Age": "22", "Name": "Maaz Ahmed", "Semester": "7"})
...
# Notice how the dict may miss some column names and is order-agnostic
# Even then, the output is correctly written
{'': '', 'Name': 'Tarun', 'Age': '21', 'Semester': '7'}
{'': '', 'Name': 'Bahawal', 'Age': '22', 'Semester': '7'}
{'': '', 'Name': 'Zain', 'Age': '26', 'Semester': '7'}
{'': '', 'Name': 'Zain', 'Age': '26', 'Semester': '7'}
{'': '', 'Name': 'Hamza Fayyaz', 'Age': '22', 'Semester': '7'}
{'': '', 'Name': 'Syed Ali', 'Age': '25', 'Semester': '7'}
{'': '', 'Name': 'Maaz Ahmed', 'Age': '22', 'Semester': '7'}
```

### Ending notes

- You can also use Pandas to clear most of the overhead for writing and reading CSVs, you can explore such here: [https://towardsdatascience.com/pandas-dataframe-playing-with-csv-files-944225d19ff](https://towardsdatascience.com/pandas-dataframe-playing-with-csv-files-944225d19ff)

### Some practice activities:

- Try to do all previous assignments using CSVs
- Can you write diagonally like we did in previous assignment in CSV?
