# DSC-DSU | Python Bootcamp 2020

<p align="center"><img src="../banner.jpg"></img></p>
Repository to hold DSC@DSU Python Bootcamp 2020 resources.

- ## Week 2 | File system, API and web scraping

  - ### [Day 1](day_1/)

    - Opening and handling files with different modes
    - `OS` module to handle paths and directories
    - Writing, reading structured file formats like CSV

  - ### [Day 2](day_2/)

    - Introduction to HTTP Requests and `requests` library
    - Working with Public APIs
    - Parsing HTML using `BeautifulSoup4`
    - Accessing DOM tree using `CSS selectors`

  - ### [Day 3](day_3/)
    - Handling dynamic web content scraping (`AJAX`)
    - Using web sessions to handle cookies
    - User login, authentication

## Assignment

### 1. Take as user input a folder path and print all the files in descending order of their respective sizes

Hints:

- You can create a tuple for each file (filename, filesize) or perhaps even a dictionary(filename, filesize, root etc). You'll be creating a list of those dictionaries or tuples.
- We have so far discussed sorting a list of primitive types (strings, ints, floats) but how do you go about sorting a list of tuples or dictionaries.. or even a list of lists? How does the sorting function know what list is greater or lesser than the other list? Google it.

**Optional** : Give option for users to remove these files

### 2. Build a Facebook bot that will retrieve the number of likes a Facebook page. Input Facebook page handles using CSVs

- The script will take as input a CSV with a list of Facebook page handles

  - The handle is FB Page's url, not the name.

    ![Assignment%2026ad56b85d694c8397104cf0eac24689/Untitled.png](Assignment%2026ad56b85d694c8397104cf0eac24689/Untitled.png)

    For example, **DeveloperStudentClubDHASuffaUniversity**

- And the output will be another CSV (or update original CSV)

![Assignment%2026ad56b85d694c8397104cf0eac24689/New_Project_(13).png](<Assignment%2026ad56b85d694c8397104cf0eac24689/New_Project_(13).png>)

### 3. Build a school scraper that'll scrap 50 schools' info and generate a CSV.

- Locate the API endpoint of the following education directory

  [https://directory.ntschools.net/#/schools](https://directory.ntschools.net/#/schools)

- Using BS4 only for the main page and JSON + Requests libraries for interacting with those endpoints
- Produce a well structured CSV with the following fields:
  1. School name
  2. Single lined formatted physical address
  3. Principal/Admin Name
  4. Principal/Admin Position
  5. Principal/Admin Email
  6. School Telephone number

Sample output:

![Assignment%2026ad56b85d694c8397104cf0eac24689/Untitled%201.png](Assignment%2026ad56b85d694c8397104cf0eac24689/Untitled%201.png)

### 4 (optional, submission not required): Try accessing your university's dashboard where your assignments and resources are uploaded. Alternatively try accessing any site which requires you to access

- You can use main function to predefine anything but make sure you divide everything you can in functions.
- Submit your github folder link and your output on Google Classroom
- Make sure you fork [https://github.com/sinnytk/Python-Bootcamp-DSC-DSU](https://github.com/sinnytk/Python-Bootcamp-DSC-DSU), clone the repo locally and create your scripts in the respective week's folder and push it.
- Make sure in each folder there's a [readme.md](http://readme.md) file with code output and brief explanation of what you did and why you did it (not necessary, but good practice)
