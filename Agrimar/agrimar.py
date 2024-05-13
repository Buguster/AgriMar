from flask import Flask, render_template , redirect , url_for , flash , request
from forms import RegistartionForm, LoginForm
from chat import CustomChatBot 

app = Flask(__name__)
app.config['SECRET_KEY'] = '092b93416967f9fec0c22c76420ed834'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' )

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
    form = RegistartionForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.user.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registre.html', title='Registre', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "email@gmail.com" and form.mdp.data == "password":
            flash(f'Welcome Back, {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful, please check your email and password", 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
