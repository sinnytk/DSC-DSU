# Lecture Notes

# Python Bootcamp | DSC@DSU

## Week 2, Day 2

By *Tarun Kumar*, **Python@DSU Lead** and Core Team **DSC@DSU**

Connection with internet is one of the important things for any human in today's time, same goes for the applications and software that you write.

### Hypertext Transfer Protocol (HTTP)

Any connection over the internet is carried out through the **H**yperText **T**ransfer **P**rotocol and as protocols go, they define a set of rules so that communication is easier.

Think any human communication, we communicate using a verbal protocol and in that verbal protocol there's a language used and that language has some a set of rules called grammar. 

In the same fashion, to communicate over the web, you use HTTP.

HTTP protocol supports the transfer of any hypermedia (interactive multimedia) in a client-server protocol using **requests**(client request of a resource or status from server) and **responses** (server's response after processing the request). 

To see the different transfers that happen between a client and server, go to any website on your browser and check ***Developer Tools -> Network Tab***

![Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/Untitled.png](Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/Untitled.png)

You may notice when you click on any one request there, you'll see some header information.

![Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/Untitled%201.png](Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/Untitled%201.png)

What's important for you know the requested **url, request method** used ****and ****the **status code** returned.

In HTTP protcol, there are different request methods which help you categorize the requests and respond from the server accordingly. I won't be getting into too much detail on all the different methods and status codes, for that you can read up this [cheatsheet](https://cheatography.com/kstep/cheat-sheets/http-status-codes/). 

**GET** (retrieving some resource) and **POST** (sending and storing some resource) ****are the commonly used request methods and is what you'll be dealing with on the daily.

GET gets a resource while with POST you send in resources.

Now covering HTTP is not the purpose of this bootcamp, so you can read it up on [here](https://www.freecodecamp.org/news/restful-services-part-i-http-in-a-nutshell-aab3bfedd131/) or any other resource you find good.

### Using `requests` library

Similar to JavaScript, if you can think of something there's probably a package or library for it (and I sincerely hope that you guys create a library for the masses one day too).

`requests` is a wonderful library to use HTTP and interact with APIs and websites and what we'll be using throughout the bootcamp.

Let's get started on working with it?

First you'll need to install the library if you haven't already:

```bash
pip install requests
```

Then import into your script or shell using

```bash
import requests
```

And voila!, you're ready to make Python talk with the internet.

### Using `requests` on APIs

To test out how you can emulate HTTP requests with requests library, let's take out any API from [https://any-api.com/](https://any-api.com/) a repository of open-access APIs.

I'll be using Discog's API which is a music release database.

From reading up on their [documentation](https://www.discogs.com/developers/#page:database,header:database-artist), I have access to 25 unregistered requests for 60 minutes. Let's try it out.

- The base url is: [https://api.discogs.com/](https://api.discogs.com/)
- Then the API provides access to different resources like releases, artists and other entities they have in their database along with the request and response schema.

Let's try to get all Led Zepplin releases:

- I found that to get releases, the endpoint is:
    - `/artists/{artist_id}/releases{?sort,sort_order}`
- The artist ID can easily be retrieved by Googling "Discog [artist name]" and I found Led Zeppelin's to be `34278`

Now let's emulate a `GET` on the aforementioned endpoint:

```bash
import requests
base_url = "https://api.discogs.com/"
response = requests.get(f"{base_url}/artists/34278/releases")
>>> response.status_code
200
>>> response.content
b'{"pagination": {"page": 1, "pages": 43, "per_page": 50, "items": 2118, "urls":...
# Response content truncated
 
```

Evidently, I get a Python dictionary like response from the API. This type of schema is called **J**avaScript **O**bject **N**otation or more commonly **JSON**. This is how REST APIs communicate with each other, to read up more what REST APIs are and what JSONs are: you can either watch [Mosh's video](https://www.youtube.com/watch?v=SLwpqD8n3d0), read up on this [FreeCodeCamp writeup](https://www.freecodecamp.org/news/rest-api-tutorial-rest-client-rest-service-and-api-calls-explained-with-code-examples/) or Google around to find whatever seems to follow your pace because REST APIs are an important concept modern web development and something every Computer Scientist should be aware of.

Now we got the response, however as the response is a huge one and not something we can scroll through and understand the schema of, let's use an online tool called [JSON Formatter](https://jsonformatter.org/) which can provide us a good overview of the schema.

1) Just open the site jsonformatter.org

2) Paste in the response body.

3) Click "Beautify"

![Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/Untitled%202.png](Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/Untitled%202.png)

You can also change the "code" format to "tree" for a better indented view in the right column.

### Using `json` to parse API responses

To convert that response byte string to a local Python dictionary, you can use the `json` module like so.

```bash

>>> import json
>>> data = json.loads(response.content)
>>> data["releases"][7]['title']
'Babe I’m Gonna Leave You / Dazed & Confused'
```

### Scraping website data using `requests`

Now APIs are a direct communication platform between a website and the server and hence they're heavily structured, however APIs are not something you usually have access to (Discog for example only allowed 25 accesses per hour).

But what about websites? You don't really have someone stopping you from accessing a website and it's contents right? (unless of course the website requires logging which Bahawal covers in the next session).

Let's try to do a `GET` on a normal website, my Facebook account: [https://www.facebook.com/sinnytk](https://www.facebook.com/sinnytk)

```bash
>>> response = requests.get("https://www.facebook.com/sinnytk")
>>> response.content
b'<!DOCTYPE html>\n<html lang="ur" id="facebook" clas'...
```

Evidently, I am getting a HTML document in response (again, to know more about HTML, CSS, you can follow Traversy Media's tutorials on [HTML](https://www.youtube.com/watch?v=UB1O30fR-EE), [CSS](https://www.youtube.com/watch?v=UB1O30fR-EE))

Let's save this response in a `.html` file and see what the browser shows.

```bash
>>> with open("sinnytk.html","w") as file:
...     file.write(response.content.decode())
... 
353363
```

![Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/New_Project_(11).png](Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/New_Project_(11).png)

You can see the difference (Urdu language being returned). The reason behind this is that web browsers are capable of executing the included JavaScript scripts in the HTML files, however a normal HTTP GET only retrieves the HTML resource without executing the underlying CSS file linking, JavaScript execution and other cascaded events that normal web browsers can do.

This result can be more evident by doing the same GET request and saving response content on [https://ahfarmer.github.io/calculator/](https://ahfarmer.github.io/calculator/), a React based single page application which is completely JavaScript generated.

![Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/New_Project_(12).png](Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/New_Project_(12).png)

### Parsing and querying HTML code with `BeautifulSoup`

Now imagine the previous example of retrieving my Facebook profile. Suppose I want to get my username or alternative name? 

How do I go about it? There are some solutions like:

- Using Regular Expressions to search for a specific pattern in text
- Use string functions like split or find

But yet again, we have a cool library called `BeautifulSoup` which parses markup-language files and strings and gives you ability to query it using DOM selection methods like CSS Selectors or XPATH.

You can read up [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) and [XPATHs](https://developer.mozilla.org/en-US/docs/Web/XPath) from the Mozilla web docs.

We'll work mainly on CSS Selectors and in short.

- To select elements IDs, you use `#`
- To select elements by classes, you use `.`
- And to select elements by attributes, you use `[ ]`

Using the inspect element, you can notice that my alternative name is described as following:

![Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/Untitled%203.png](Lecture%20Notes%2013778c78ac534a93aa4b6a6c8104467c/Untitled%203.png)

We can refer to this element by saying:

"Get me the span tag with class of **alternate_name**"

And in CSS selectors, that'll be translated to:

`span.alternate_name`

or

`span[class="alternate_name"]`

Let's do this using BeautifulSoup.

1. Install BeautifulSoup library using `pip install beautifulsoup4`
2. Import the BeautifulSoup parser in your script using `from bs4 import BeautifulSoup`
3. Send BeautifulSoup class your HTML code and define a parser to use
4. Voila, you can now use CSS selectors using `select()` and `select_one()`

```bash
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(response.content,'html.parser')
>>> soup.select("span.alternate_name")
[<span class="alternate_name">(Sinny)</span>]
>>> soup.select_one("span.alternate_name")
<span class="alternate_name">(Sinny)</span>
>>> soup.select_one("span.alternate_name").text
'(Sinny)'
>>> soup.select_one("span.alternate_name").text[1:-1]
'Sinny'
```

Live example:

[https://quotes.toscrape.com/](https://quotes.toscrape.com/)

Note: script also attached

Some sample projects i did(explained in live session): 

- Allison's project for different sites

Some caveats to remember:

- What you see in `***Right Click → View Page Source`*** is what you'll actually see when you download and parse using Requests and BS4
- BeautifulSoup isn't capable of querying JavaScript code or CSS styles and hence only works on static sites without dynamically loaded content