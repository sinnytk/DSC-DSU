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

## Assignments

In progress

- You can use main function to predefine anything but make sure you divide everything you can in functions.
- Submit your github folder link and your output on Google Classroom
- Make sure you fork [https://github.com/sinnytk/Python-Bootcamp-DSC-DSU](https://github.com/sinnytk/Python-Bootcamp-DSC-DSU), clone the repo locally and create your scripts in the respective week's folder and push it.
- Make sure in each folder there's a [readme.md](http://readme.md) file with code output and brief explanation of what you did and why you did it (not necessary, but good practice)
1. Use AJAX to get first 50 school details. You need to get the following fields.
  - School Name
  - school code
  - school display  address     
  - school contact (email)
  - school contact (number)
  - first management personal name
  - first management personal position

    You need to submit an csv file with these fields. 

2. login into your university LMS using requests sessions. You'll need to go through your university page to find of they use web tokens or not. After you logging in you need to scrap all the course you are currently enrolled in and provide them in a csv file in the follow way

    course code , course name , instructor (if posible)
    CS102,Programming fundamentals, Twaha Ahmed Minai....

