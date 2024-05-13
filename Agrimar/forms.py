from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistartionForm(FlaskForm):
    user = StringField(
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


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    mdp = PasswordField(
        'Password', validators=[
            DataRequired(), Length(
                min=6, max=15)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CoordinateForm(FlaskForm):
    latitude = StringField('Latitude', validators=[DataRequired()])
    longitude = StringField(
        'Longitude', validators=[
            DataRequired()])
    submit = SubmitField('submit')

