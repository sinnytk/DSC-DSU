from flask import Flask, render_template,redirect,url_for,session,request
from wtforms import Form, StringField, PasswordField, validators
import pymongo as pym

app = Flask(__name__)
app.secret_key = "secret123"

connection = pym.MongoClient("mongodb+srv://mtk:1234@cluster0.pepx2.mongodb.net/test?retryWrites=true&w=majority")
db = connection.get_database("test")

User_details = pym.collection.Collection(db,"User_details")
tweets = pym.collection.Collection(db,"tweets")

class RegisterForm(Form):
    email = StringField("Email",[validators.Email()])
    name = StringField("Username",[validators.Length(min=1,max=50)])
    password = PasswordField("Password",[validators.DataRequired()
        ,validators.EqualTo("confirm",message="Password Doesnt match")])
    confirm = PasswordField("Confirm Password")

@app.route("/",methods=['GET','POST'])
def register():
    
    form = RegisterForm(request.form)
    
    if request.method == "POST":
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        user = User_details.insert_one(
                {"name":name,
                 "email":email,
                 "password":password
                }
                )
        if(user):
            print("Inserted!")
        
        return render_template("Login_template.html")
    
    return render_template("Register_template.html",form=form)


@app.route("/index",methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        Tweet = request.form['tweet']
        
        user_tweet = tweets.insert_one(
                {
                    "tweet" : Tweet,
                    "name" : session['name'],
                    "date" : "26-12-2020",
                    "email":session['email']
                        })
            
        #Tweets = get_tweets(session['email'])
    
    Tweets = get_tweets(session['email'])
    
    return render_template("Social_media_template.html",dictionary=Tweets)

def get_tweets(email):
    user_tweets = tweets.find({"email":email})
    user_tweet = {}
    y = {}
    for documents in user_tweets:
        y = documents
        key = y['_id']
        user_tweet.setdefault(key,[])
        user_tweet[key].append(y['name'])
        user_tweet[key].append(y['tweet'])
        user_tweet[key].append(y['date'])
    
    return user_tweet
        

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        check_user = User_details.find_one({"email":email,"password":password})
        if check_user:
            session['logged_in'] = True
            session['email'] = email
            session['name'] = check_user['name']
            
            return redirect(url_for("index"))
        else:
            return render_template("Login_template.html")
        
        
    return render_template("Login_template.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))





if __name__ == "__main__":
    app.run()