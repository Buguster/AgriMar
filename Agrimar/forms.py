from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from AgriMar.Agrimar.model import User


class RegistartionForm(FlaskForm):
    username = StringField(
        'Username', validators=[
            DataRequired(), Length(
                min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mdp = PasswordField(
        'Password', validators=[
            DataRequired(), Length(
                min=6, max=15)])
    con_mdp = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), Length(
                min=6, max=15), EqualTo('mdp')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken , please choose another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken , please choose another one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    mdp = PasswordField(
        'Password', validators=[
            DataRequired(), Length(
                min=6, max=15)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class MapForm(FlaskForm):
    lat = FloatField('Latitude', validators=[DataRequired()])
    lon = FloatField('Longtitude', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateAccountForm(FlaskForm):
    username = StringField(
        'Username', validators=[
            DataRequired(), Length(
                min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                'That username is taken , please choose another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                        'That email is taken , please choose another one')
            
class AddMessageHistory(FlaskForm):
    content = TextAreaField("message", validators=[DataRequired()])
    