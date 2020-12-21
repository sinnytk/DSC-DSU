# Lecture Notes

# Python Bootcamp | DSC@DSU

<p align="center"><img src="../../banner.jpg"></img></p>

## Week 2, Day 3

By _Bahawal Baloch_, **Python@DSU Co-Lead** and Core Team **DSC@DSU**

why is it hard to scrap dynamic web content ?

Dynamic web content is such content that is added to the web page on run time. for example load more option adds more items to the webpage on the run time. This creates a problem for scrapers since when we use requests to get a page we get a static page which do not contain the complete information we need to scrap.

How does dynamic web content works ?

data is requested to the server then the HTML page is modify based on the response using jquery.

Most commonly web devs use AJAX for this job. AJAX stands for asynchronous javascript XML.

XML stands for Extensible Markup Language.

How do we know if a website is using AJAX ?

we can check it by simply checking the Network tab in inspect

[https://directory.ntschools.net/#/schools](https://directory.ntschools.net/#/schools)

![lecture%20notes%20-%202%203%20b111b8ff3373478abf32962786aa1994/inspect.png](lecture%20notes%20-%202%203%20b111b8ff3373478abf32962786aa1994/inspect.png)

As you can we the Data coming from an AJAX request can be found in the XHR tab

XHR stands for XML Http request.

let's see how can we find the address where we need to make AJAX request to get the required data.

![lecture%20notes%20-%202%203%20b111b8ff3373478abf32962786aa1994/header.png](lecture%20notes%20-%202%203%20b111b8ff3373478abf32962786aa1994/header.png)

after finding the address we need to find the parameter which is used to call the data.

if we scroll down we'll find

![lecture%20notes%20-%202%203%20b111b8ff3373478abf32962786aa1994/parameters.png](lecture%20notes%20-%202%203%20b111b8ff3373478abf32962786aa1994/parameters.png)

this section which tell us how to pass parameters to our request.

now we have both things now we need to iterate over the school code to

### the code.

What is the return type of the request ?

JSON ?

JavaScript Object Notation is most similar to the python dictionary.

how to read JSON ?

using the JSON package in python.

`parsed_data = json.loads(data.content)`

## Web Sessions

What are web sessions ?

whenever we login into a website or whenever you go to an eCommerce website and you are able to create a cart and maintain your data in cookies. This process of saving the user's data in local storage is called a web session. The session terminates by either leaving the website or deleting the cookies.

Why do we need web sessions ?

Some of the website's data might not be available directly we might need to login into a website to retrieve the data. We use the `requests` library to handle such scenarios.

Example of a website.

Explain Headers

HTTP headers let the client and the server pass additional information with an HTTP request or response. Header cards or headers are extra parameters which go with our requests with tells the receiver certain things about us. Like what web browsers are we using etc

Explain web tokens

```python
import requests as r
from bs4 import BeautifulSoup as soup
link = 'https://www.codechef.com/'
payload = {
    'name': 'bahawal32',
'pass': 'Python321!',
'form_id': 'new_login_form',
'op': 'Login'
}

headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
with r.Session() as s:
    p = s.get(link,headers=headers)
    soup_page = soup(p.content)
    payload['csrfToken']=soup_page.select('#edit-csrfToken')[0]['value']
    payload['form_build_id']=soup_page.find('input',{'name':'form_build_id'})['id']
    log_in = s.post(link,headers=headers,data=payload)
    soup_in = soup(log_in.content)
    print(soup_in)
```
