# Lecture Notes

# Python Bootcamp | DSC@DSU

<p align="center"><img src="../../banner.jpg"></img></p>

## Week 3, Day 3

By _Tarun Kumar_, **Python@DSU Lead** and Core Team **DSC@DSU**

This will be the last session on Selenium and I plan to cover the different functionalities, caveats and cool features that the library provides.

### Pausing on SoundCloud

But first let's discuss the Soundcloud example which played a song you queried for. As it happens in a professional environment, you sometimes come upon examples or implementations that should work but for some reason don't, the Soundcloud bot that we were trying to create in the last session is the prime example of that.

I found out that (and built up on what we found in the live session) that the classes of the play button change and as they do, the previous triggered action is overridden in the chain of actions.

![Lecture%20Notes%20121d9a943593432e8769f200aa9621cf/Untitled.png](Lecture%20Notes%20121d9a943593432e8769f200aa9621cf/Untitled.png)

I found out that `XPath` does fix this if you just copy the Xpath of the element, which comes out to be:

```bash
>>> elem_xpath = '//*[@id="content"]/div/div/div[3]/div/div/div/ul/li[1]/div/div/div/div[2]/div[1]/div/div/div[1]/a'
>>> driver.find_element_by_xpath(elem_xpath).click()
# song plays
>>> driver.find_element_by_xpath(elem_xpath).click()
# song pauses

```

As I have mentioned a few times, I personally prefer using CSS Selectors so I got a similar selector working for pausing as well!

```bash
>>> play_pause_btn = driver.find_element_by_css_selector("div.sound__header div div div")
>>> play_pause_btn.click()
# song plays
>>> play_pause_btn.click()
# song paused
```

### Expected Wait Conditions

All good right? The bot works now.. _only in theory_, not in script.

When I converted the bot to a full-fledged script (available in the repository as `soundcloud_script.py`), I found out that the bot errors out when trying to play a song after searching it:

```bash
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.sound__header div div div"}
  (Session info: chrome=85.0.4183.121)
```

Looking into the error, we can deduce that we're trying to search for an element that doesn't exist in on the page yet.

This is because we're not waiting for the page to load before accessing that element.

What would be a simple fix? A way to make the script wait before querying that element (i.e letting the page load?)

The simplest fix is to use `time.sleep()` to make the script stop execution for a while. And that does indeed fix the script and makes the script execute smoothly by adding a constant execution halt of `2` seconds. (see `soundcloud_script_sleep.py` in the repo)

Some problems with using `time.sleep`

- It's constant, therefore:
  - If the page load takes more time than explicitly defined, it'll fail
  - Or if the page load takes much less time than before, time is wasted
- It's not dynamic enough to account for complex conditions where you want specific content to load instead of an element

One way to use sleep dynamically would be to handle exceptions like so:

```bash
>>>from selenium.common.exceptions import NoSuchElementException
>>> while True:
...     try:
...             play_pause_btn = driver.find_element_by_css_selector("div.sound__header div div div")
...             play_pause_btn.click()
...             break
...     except NoSuchElementException:
...             print("play button not found, waiting 0.5 seconds")
...             time.sleep(0.5)
...
play button not found, waiting 0.5 seconds
play button not found, waiting 0.5 seconds
```

Selenium provides a really good wait condition framework to accommodate page loading. These wait conditions are called `Expected Conditions` and can make a `WebDriver` check for existence of an element and then do something or throw a timeout exception.

You can read up on [Explicit Waits over here](https://selenium-python.readthedocs.io/waits.html#explicit-waits).
Let's try to use a `presence_of_element_located` check before clicking on the button for our Soundcloud example.

We'll need to import 3 things to use expected conditions.

- `selenium.webdriver.support.expected_conditions`
- `selenium.webdriver.support.ui.WebDriverWait`
- `selenium.webdriver.common.by.By`

These 3 classes will help us simplify the dynamic sleep we defined above.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

try:
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
except TimeoutException:
	print("Element not found, exiting driver")
	driver.quit()

# WebDriverWait(driver, 10) | make the webdriver keep checking for 10 seconds
# .until | until the following condition returns true
# EC.presence_of_element_located | use an element's presence as check
# (By.ID, "myDynamicElement") | find element by ID of myDynamicElement
```

Let's convert the above for our play button element.

```python
play_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.sound__header div div div")))
play_btn.click()
```

### Building a Facebook bot

Covered in live session.

The bot will:

- use m.facebook.com
- go to a given post link
- like and comment on it
