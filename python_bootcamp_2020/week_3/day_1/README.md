# Python Bootcamp | DSC@DSU

<p align="center"><img src="../../banner.jpg"></img></p>

## Week 3, Day 1

By _Tarun Kumar_, Python@DSU Lead and Core Team member

We have tried requesting HTML pages and retrieving content from APIs using the `BeautifulSoup4` and `Requests` packages.

Now we move towards full-fledged web browser automation where you can replicate opening a complete browser and performing actions a human would, like:

- Entering text into fields
- Clicking on buttons
- Submitting forms
- Scrolling
- Copying content
- Hovering and navigating all around websites

Interested yet?

The powerful framework that we'll be using is called Selenium, specifically it's WebDriver module.

### Installing Selenium WebDriver

You need two things to start working with Selenium.

1. Installing the Python library using `pip`

```bash
pip install selenium
```

2.  Downloading the binary for your respective browser and put it either in your script's folder or your Python default path

```
Download the driver binary for your respective browser. I'll be using Chrome so I'll put in the guide for that.

	Chrome:	https://chromedriver.chromium.org/downloads
	Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
	Firefox:	https://github.com/mozilla/geckodriver/releases

1. Check your chrome version by going to chrome://version
2. Download the respective binary from the link above
3. Extract the .zip containing the .exe (or for Unix systems normal object file) to your Python path, that we discussed in the first lecture.
My path was: /usr/bin
For windows, if we put the chromedriver.exe under C:/Windows, then there is no need to specify executable_path since Python will search under C:/Windows.
```

### Opening Chrome and accessing sites

To start working with Selenium, you can simply import the WebDriver and open a Chrome instance like:

```bash
>>> from selenium import webdriver
>>> driver = webdriver.Chrome()
>>> driver.get("www.github.com/sinnytk")
```

![Lecture%20Notes%200c08aa6d2c274766a967cdc4fd129b8a/Untitled.png](Lecture%20Notes%200c08aa6d2c274766a967cdc4fd129b8a/Untitled.png)

### Finding and selecting DOM elements

Similar to the `select` function in a BeautifulSoup parsed object, you can find elements using CSS selector, but Selenium being much more robust has options to find elements by:

- xpath
- id
- class names

You can find more on the different selector methods [here](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements)

Suppose, I want to find all the pinned repositories on my Github.

Using `inspect element` I could find that the clickable links are enclosed in a `div` with class `pinned-item-list-item-content` and then an `a` tag with class `text-bold`

![Lecture%20Notes%200c08aa6d2c274766a967cdc4fd129b8a/image_(2).png](<Lecture%20Notes%200c08aa6d2c274766a967cdc4fd129b8a/image_(2).png>)

```bash
>>> driver.find_elements_by_css_selector("**div.pinned-item-list-item-content a.text-bold**")

[<selenium.webdriver.remote.webelement.WebElement (session="595715d972040c8e3337e983b8da8c1f", element="d8fc00f2-0579-4f39-a25a-bc7a08dc6250")>, <selenium.webdriver.remote.webelement.WebElement (session="595715d972040c8e3337e983b8da8c1f", element="b0f14c13-0e30-4934-b380-ad669546a8f9")>, <selenium.webdriver.remote.webelement.WebElement (session="595715d972040c8e3337e983b8da8c1f", element="d481f1be-1413-4192-be75-fb5de60a9157")>, <selenium.webdriver.remote.webelement.WebElement (session="595715d972040c8e3337e983b8da8c1f", element="0ea3bf2c-5601-4af7-b19c-38a64d3946e2")>, <selenium.webdriver.remote.webelement.WebElement (session="595715d972040c8e3337e983b8da8c1f", element="3b2a08bd-c08c-4188-bbc1-b723a1acea79")>, <selenium.webdriver.remote.webelement.WebElement (session="595715d972040c8e3337e983b8da8c1f", element="b3583802-3894-456a-8109-53e8f913f467")>]

```

### `WebElement` properties

Now if you may notice, we're not getting a list of `Tag` objects like with `BeautifulSoup4`, but instead we're getting a list of `WebElement` objects. These are native to Selenium and provide numerous functions and actions that can be performed on them.

Let's try some of them:

```bash
>>> repo_links_elems = driver.find_elements_by_css_selector("div.pinned-item-list-item-content a.text-bold")
```

- Raw text of the element:

  ```bash
  >>> repo_links_elems[0]
  <selenium.webdriver.remote.webelement.WebElement (session="595715d972040c8e3337e983b8da8c1f", element="d8fc00f2-0579-4f39-a25a-bc7a08dc6250")>
  >>> repo_links_elems[0].get_attribute("text")
  '\n          ration-app\n'
  >>> repo_links_elems[0].text
  'ration-app'
  >>>
  ```

- Attributes of the element:

  ```bash
  >>> repo_links_elems[0].get_attribute('href')
  'https://github.com/sinnytk/ration-app'
  >>> repo_links_elems[0].get_attribute('class')
  'text-bold flex-auto min-width-0 '
  ```

- Accessing child elements

  ```bash
  >>> repo_links_elems[0].get_attribute("outerHTML")
  '<a class="text-bold flex-auto min-width-0 " data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:32937387,&quot;target&quot;:&quot;PINNED_REPO&quot;,&quot;user_id&quot;:null,&quot;originating_url&quot;:&quot;https://github.com/sinnytk&quot;}}" data-hydro-click-hmac="183ea35877f7c9535bc15ea21cbf9f7ecc26bbf6abac61e43a1e848a9b53adaf" href="/sinnytk/ration-app">\n          <span class="repo" title="ration-app">ration-app</span>\n</a>'
  # the outerHTML tag returns the HTML of the element.
  # we can see a <span> tag enclosed in the anchor tag.

  >>> repo_links_elems[0].find_elements_by_css_selector("span")
  [<selenium.webdriver.remote.webelement.WebElement (session="0b592a4f8ff6ea0e4066d79a9d74d5dd", element="f40c7ff7-27e2-43f4-b637-c8f7147e3ddd")>]
  >>> repo_links_elems[0].find_elements_by_css_selector("span")[0].text
  'ration-app'
  ```

### Interacting using clicks and other human behavior

Now I showed you some properties of the `WebElement` object above, but that's not even half of what Selenium can do.

Selenium was originally produced as a testing framework where you can run automated tests on your websites to ensure every nook and cranny is working as expected without have a human manually laboring through the different test cases.

And as is often in websites, they require interactions like clicks, scrolling, hovering and sending key input for typing and shortcuts etc.

You can do all such actions using a Selenium WebDriver.

If you remember the [React based Calculator site](https://ahfarmer.github.io/calculator/) that I showed requiring JavaScript in the web scraping sessions, let's try having Selenium perform actions for us on that site?

![Lecture%20Notes%200c08aa6d2c274766a967cdc4fd129b8a/Untitled%201.png](Lecture%20Notes%200c08aa6d2c274766a967cdc4fd129b8a/Untitled%201.png)

1. Go to the site using `driver.get()`

   ```bash
   >>> from selenium import webdriver
   >>> driver = webdriver.Chrome()
   >>> driver = webdriver.get("https://ahfarmer.github.io/calculator/")
   ```

2. From inspection, we can find that all the buttons are enclosed in `button` which is enclosed in a `div` with class `component-button`

   ```bash
   >>> btns = driver.find_elements_by_css_selector('div.component-button button')
   >>> for btn in btns:
   ...     print(btn.text)
   ...
   AC
   +/-
   %
   ÷
   7
   8
   9
   x
   4
   5
   6
   -
   1
   2
   3
   +
   0
   .
   =

   ```

   Now that you've queried the buttons, let's try to click them?

   A dumb approach would be to iterate over the buttons and search for values we want to press.

   But as we do not have a specific ID or way to correctly find a specific button, but what we do have a list of elements which can be mapped to what they represent in value.

   And what's the best structure to map values? A **dictionary**

   ```bash
   SYMBOL_TO_INDEX = {'AC': 0, '%': 2, '/': 3,
                      '7': 4, '8': 5, '9': 6,
                      '*': 7, '4': 8, '5': 9,
                      '6': 10, '-': 11, '1': 12,
                      '2': 13, '3': 14, '+': 15,
                      '0': 16, '.': 17, '=': 18}
   # You may notice I haven't assigned the mapping **+/-** to 1.
   # This is just to avoid wasting time on supporting negative numbers for now
   ```

   Now if I wanted to evaluate 2+2, I would do:

   ```bash
   >>> btns[SYMBOL_TO_INDEX['2']].click() # retrieves index of 2 and presses it
   >>> btns[SYMBOL_TO_INDEX['+']].click() # retrieves index of + and presses it
   >>> btns[SYMBOL_TO_INDEX['2']].click() # retrieves index of 2 and presses it
   >>> btns[SYMBOL_TO_INDEX['=']].click() # retrieves index of = and presses it

   # result is evaluated in a div called component-display
   >>> driver.find_element_by_css_selector('div.component-display div').text
   '4'
   ```

Live session:

- Build quotes scraper using Selenium

And that's how you make your browser do stuff for you.

Look into:

- Selenium options
  - Start headless processes
  - Define custom browsers like Brave

Some tasks you can do on your own:

- Try going over the BS4 examples using Selenium now.
- Scrap the school listings by clicking instead of API interaction.
- Create a bot that plays a song using terminal on Patari.pk
