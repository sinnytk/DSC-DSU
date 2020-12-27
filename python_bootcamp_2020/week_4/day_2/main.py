from flask import Flask, render_template, flash, redirect, url_for, session, request
from wtforms import Form, StringField, PasswordField, validators
import pymongo as pym
import datetime

app = Flask(__name__)
app.secret_key='secret123'

connection = pym.MongoClient("mongodb+srv://mtk:1234@cluster0.pepx2.mongodb.net/test?retryWrites=true&w=majority")
db = connection.get_database('test')

user_detail = pym.collection.Collection(db, 'User_details')
tweets = pym.collection.Collection(db, 'tweets')

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'POST':
            tweet = request.form['tweet']            
            ct = datetime.datetime.now()
            
            user_id = tweets.insert_one(
            {   "email" : session["username"],
                "tweet" : tweet,
                "name" : session['name'], 
                "time" : str(ct.date())
            })
    
            #flash('Tweet added', 'success')
            
            answer = get_tweets(session['username'])
            return render_template('Home.html',dictionary=answer)

    answer = get_tweets(session['username'])                   
    return render_template('Home.html',dictionary=answer)

# Register Form Class
class RegisterForm(Form):
    email = StringField('Email', [validators.Email()])
    name = StringField('Name', [validators.Length(min=1, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


# User Register
@app.route('/', methods=['GET', 'POST'])
def register():
    
    users = user_detail
    
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        myid = users.insert_one(
            {   "name" : name,
                "email" : email,
                "password" : password
            })
        
        flash('You are now registered and can log in', 'success')

        redirect(url_for('login'))
        #return render_template('Login.html') 
    return render_template('Register.html', form=form)

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    user = user_detail
    if request.method == 'POST':
        # Get Form Fields
        email = request.form['username']
        password_candidate = request.form['password']
        
        response = user.find_one({'email': email})
        

        if response:
            password = response['password']

            # Compare Passwords
            if password_candidate == password:
                # Passed
                session['logged_in'] = True
                session['username'] = email
                session['name'] = response['name']
                
                flash('You are now logged in', 'success')
                return redirect(url_for('index'))
            else:
                error = 'Invalid login'
                return render_template('Login.html', error=error)
        else:
            error = 'Email not found'
            return render_template('Login.html', error=error)

    return render_template('Login.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


def get_tweets(email):
    pid = tweets.find({"email":session['username']})
                
    user_tweets = {}
    y = {}
    for docs in pid:
        y = docs
        key = y["_id"]
        user_tweets.setdefault(key,[])
        user_tweets[key].append(y["name"])
        user_tweets[key].append(y["tweet"])
        user_tweets[key].append(y["time"])
    
    return user_tweets


if __name__ == '__main__':
    app.run()
    