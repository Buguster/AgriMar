from flask import render_template, redirect, url_for, flash, request
from AgriMar.Agrimar.chat import CustomChatBot
from AgriMar.Agrimar.forms import RegistartionForm, LoginForm, MapForm, UpdateAccountForm
from AgriMar.Agrimar.model import User, Conversation, Message
from AgriMar.Agrimar import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["msg"]
        return CustomChatBot(user_input)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/registre", methods=['GET', 'POST'])
def registre():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistartionForm()
    if form.validate_on_submit():
        hash_mdp = bcrypt.generate_password_hash(form.mdp.data).decode('utf-8')
        user = User(
            username=form.username.data,
            email=form.email.data,
            mdp=hash_mdp)
        db.session.add(user)
        db.session.commit()
        flash(
            'Account created successfully! you can now log in to your account',
            'success')
        return redirect(url_for('login'))
    return render_template('registre.html', title='Registre', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.mdp, form.mdp.data):
            flash("Welcome Back " + user.username + "!", 'success')
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(
                "Login Unsuccessful, please check your email and password",
                'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    """
    This Function is to handle the user input image to update it
    into the database.
    """
    random_hex = secrets.token_hex(8)
    _e, extension = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + extension
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)
    return picture_fn


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.img = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your Account has been succesfully Updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.picture.data = current_user.img

    image = url_for('static', filename='images/' + current_user.img)
    return render_template('account.html', title='Account', image=image, form=form)


@app.route("/map")
def map():
    form = MapForm()
    return render_template('map.html', title='map', form=form)

@app.route("/admin/delete_user")
@login_required
def delete_user():
    return render_template('DeleteUser.html', title='Delete user')
