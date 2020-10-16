from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import os
import math
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_mail import Mail
from datetime import datetime

with open('config.json', 'r') as c:
    params = json.load(c)["para"]

local_server = params["local_server"]
app = Flask(__name__)
app.secret_key= '1234'
app.config["Upload_Folder"] = params['upload_location']
# app.config
 
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params["g-email"],
    MAIL_PASSWORD = params["g-password"]
)
mail = Mail(app)

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
    db = SQLAlchemy(app)
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
    db = SQLAlchemy(app)

class Contacts(db.Model):
    sn = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    message = db.Column(db.String(500), unique=True, nullable=False)
    date = db.Column(db.String(20), unique=True, nullable=False)

class Posts(db.Model):
    sn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=False, nullable=False)
    sub_title = db.Column(db.String(100), unique=False, nullable=False)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    content = db.Column(db.String(1000), unique=True, nullable=False)
    img_file = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.String(20), unique=True, nullable=False)

@app.route("/")
def home():
    # Paginatio
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_post']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_post']):(page-1)*int(params['no_post'])+int(params['no_post'])]
    if (page==1):
        go = "#"
        back = "/?page=" + str(page+1)
    elif (page==last):
        go = "/?page=" + str(page - 1)
        back = "#"
    else:
        go = "/?page=" + str(page - 1)
        back = "/?page=" + str(page + 1)


    return render_template('index.html', params=params , posts=posts, go=go, back=back)
    # posts = Posts.query.filter_by().all[0:params['no_post']]
@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/login', methods=['GET','POST'])
def login():
    if ('user' in session and session['user'] == params["login_email"]):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method=='POST':
        username = request.form.get('a_name')
        password = request.form.get('a_password')
        if (username == params["login_email"] and password == params["login_password"]):
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)

    
    return render_template('login.html', params=params)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')


@app.route('/delete/<string:sn>', methods=['GET','POST'])
def delete(sn):
    if ('user' in session and session['user'] == params["login_email"]):
        post = Posts.query.filter_by(sn=sn).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/login')

@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html', params=params, post=post)


@app.route('/edit/<string:sn>', methods=['GET','POST'])
def edit(sn):
    if ('user' in session and session['user'] == params["login_email"]):
        if request.method == 'POST':
            title = request.form.get('title')
            sub_title = request.form.get('sub_title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img')
            date=datetime.now()

            if sn =='0':
                post = Posts(title=title,sub_title=sub_title, slug=slug, content=content, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit() 
            else:
                post = Posts.query.filter_by(sn=sn).first()
                post.title=title
                post.sub_title = sub_title
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date= date
                db.session.commit()
                return redirect('/edit/'+ sn)
        post = Posts.query.filter_by(sn=sn).first()
        return render_template('edit.html', params=params, post=post)



@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        if name != '':
            entry = Contacts(name=name, email=email, phone=phone, message=message, date=datetime.now())
            db.session.add(entry)
            db.session.commit()

            mail.send_message(
                'Message From ' + name,
                sender=email,
                recipients=[params["g-email"]],
                body= "Name: " + name + "\n" + "Email Address: " + email + "\n" + "Phone Number: " + phone + "\n\n" + "Message: \n\t\t" + message 
                )

    return render_template('contact.html', params=params)

@app.route('/uploader', methods=['GET','POST'])
def upload():
    if ('user' in session and session['user'] == params["login_email"]):
        if (request.method == 'POST'):
            f =request.files['file']
            f.save(os.path.join(app.config['Upload_Folder'], secure_filename(f.filename)))
            return "Uploaded Successfully"


app.run()