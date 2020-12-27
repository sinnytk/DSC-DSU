# Lecture Notes

This is the session covering python web framework Flask basics, templating with Jinja and Simple social media web app using flask
### What is Flask?
Flask is a web application framework written in Python. It is developed by Armin Ronacher, who leads an international group of Python enthusiasts named Pocco. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects.
Flask documentation: https://flask.palletsprojects.com/en/1.1.x/

### WSGI
Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. WSGI is a specification for a universal interface between the web server and the web applications.

### Jinja2
Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.
Flask is often referred to as a micro framework. It aims to keep the core of an application simple yet extensible. Flask does not have a built-in abstraction layer for database handling, nor does it have form validation support. Instead, Flask supports the extensions to add such functionality to the application.
Jinja documentation: https://jinja.palletsprojects.com/en/2.11.x/

### Installing Flask
```bash
pip install Flask
```

### Hello World in Flask
```bash
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()
 ```
Importing the flask module in the project is mandatory. An object of the Flask class is our WSGI application.
The Flask constructor takes the name of the current module (__name__) as an argument.
The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.

### Routing in Flask
```bash
from flask import Flask
app = Flask(__name__)

@app.route('/home/<name>')
def hello_name(name):
   return ("Hello" + name)

@app.route('/home/<int:number>')
def hello_int(number):
   return ("Hello" + number)

@app.route('/home/<float:number>')
def hello_float(number):
   return ("Hello" + number)

if __name__ == '__main__':
   app.run()
```
Run the above code from Python Shell. Visit the URL http://localhost:5000/home/John in the browser.
The given string is used as argument to the hello_name() function. The browser displays the following output −
```
Hello John
```
Same as for other variable types url the following result should appear:
For  http://localhost:5000/home/11:
```
Hello 11
```
For  http://localhost:5000/home/1.1:
```
Hello 1.1
```

### Templating in Flask
Consider the following HTML code we will save this code as home.html:
```html
<html>
   <body>
      <h1>FLASK<h1>
   </body>
</html>
```
Now write python script:
```bash
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template(‘home.html’)

if __name__ == '__main__':
   app.run(debug = True)
```
This will render template of home.html and "FLASK" will be displayed in browser.

Similary for displaying name html code below:
```html
<html>
   <body>
      <h1>Hello {{ name }}!</h1>
   </body>
</html>
```
Python code below:
```bash
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)
```

### Handling HTML Form Data with Flask
To get the form data from html forms we will be using POST method in app.route method and request function from Flask library to get form element.
HTML code:
```html
<form action="{{ url_for('handle_form') }}" method="post">
    <input type="text" name="text_data" placeholder="Enter your name">
    <input type="submit">
</form>
```

Python code:
```bash
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template(‘form.html’)

@app.route('/handle_form', methods=['POST'])
def handle_data():
    text = request.form['text_data']
		return render_template("name.html")

if __name__ == '__main__':
   app.run(debug = True)
```

### Building a Simple Social Media Web App

Covered in live session.

The social media web-app will:

- Register User
- Login User
- Post and display user tweets

Some necessary libraries to import and install:
-WTForms
-Pymongo
Installation:
```
pip install WTForms
```
```
pip install pymongo
```
