# Lecture Notes

# Python Bootcamp | DSC@DSU

<p align="center"><img src="../../banner.jpg"></img></p>

## Week 3, Day 2

By _Tarun Kumar_, **Python@DSU Lead** and Core Team **DSC@DSU**

Let's get our hands dirtied by going one step further into automating website access.

I discussed in the previous session that we can automate keyboard input on websites, so let's get started with that first?

### Searching and playing songs on Soundcloud

Let's a build a bot that'll:

1. Go to [Soundcloud](http://soundcloud.com)
2. Search a song in the search field
3. Press enter to execute search
4. Play the first song from search results.

```bash
# opens chrome driver
# goes to soundcloud
# selects search input element
>>> driver = webdriver.Chrome()
>>> driver.get("https://soundcloud.com")
>>> input_el =driver.find_element_by_css_selector("input[type='search']")
>>> input_el.get_attribute("placeholder")
'Search for artists, bands, tracks, podcasts'
```

However when we click on the search bar to put it into focus, like a normal human user would. I get an `ElementNotInteractableException`

```bash
>>> input_el.click()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/tarun/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py", line 80, in click
    self._execute(Command.CLICK_ELEMENT)
  File "/home/tarun/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "/home/tarun/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "/home/tarun/.local/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
  (Session info: chrome=85.0.4183.121)
```

What can cause the above issue?

- Element is not loaded yet (not possible, we can see the element)
- Element is hidden inside other elements (check the inspect element to make sure)

Now there are multiple ways to fix this and usually the best way to do is the simplest one.

_Query using the XPath_

`Right click on element -> Inspect element -> Copy XPath`

![Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled.png](Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled.png)

```bash
>>> input_el = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[1]/span/span/form/input')
>>> input_el.click()
```

### Keyboard input

Selenium `WebElement` provides a convenient function called `send_keys` that you can use to emulate user input into fields, like so:

```bash
>>> input_el.send_keys("Amir Zaki The Day She Left")
```

![Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled%201.png](Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled%201.png)

Now to initiate the search we need to hit `enter`, we have two options to do so:

- Sending in raw `\n` which is basically a enter in most search fields.

  ```bash
  >>> input_el.send_keys("\n")
  ```

- Using the Keys object from Selenium common keys.

  ```bash
  >>> from selenium.webdriver.common.keys import Keys
  >>> Keys.ENTER
  '\ue007'
  >>> input_el.send_keys(Keys.ENTER)
  ```

Finally playing the song:

```bash
driver.find_element_by_css_selector("a.snippetUXPlayButton").click()
```

![Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled%202.png](Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled%202.png)

### Logging into Facebook

Let's get to logging into your Facebook accounts using Selenium.

```bash
>>> driver.get("https://facebook.com")
>>> email_input = driver.find_element_by_id("email")
>>> password_input = driver.find_element_by_id("pass")
```

![Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled%203.png](Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled%203.png)

```bash
# **getpass** is a tool which you can use to hide user input from terminal stdout

>>> from getpass import getpass
>>> email = "rovekoy922@94jo.com"
>>> password = getpass()
Password:
>>> login_btn = driver.find_element_by_css_selector("button[data-testid='royal_login_button']")
>>> login_btn.click()
```

![Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled%204.png](Lecture%20Notes%208078ffb6e5f84399b2d64c93984199b4/Untitled%204.png)

Questions to ponder:

- Look into `Action Chains`
  - Sending a series of inputs
  - Key_up, key down
  - Drag and drop
  - Action Chains for form filling
- How would you select a specific value in a `select` field?
