from sqlalchemy.orm import relationship, backref
from datetime import datetime, timezone, timedelta
from AgriMar.Agrimar import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    """
    to reload the user that is logged in the 
    current sesssion based on the user id
    """
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    mdp = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(20), nullable=False, default='default.jpg')
    privilege = db.Column(db.String(15), nullable=False, default='user')
    acd = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now(
            timezone.utc) +
        timedelta(
            hours=1))
    conversations = db.relationship(
        'Conversation', backref='author', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"User('{self.username}' , '{self.email}' , '{self.img}')"

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    loc_lat = db.Column(db.Float)
    loc_lon = db.Column(db.Float)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    messages = relationship('Message', backref='convo', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"Conversation('{self.title}' , '{self.date}' )"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    time = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now(
            timezone.utc))
    convo_id = db.Column(
        db.Integer,
        db.ForeignKey('conversation.id'),
        nullable=False)

    def __repr__(self):
        return f"Message('{self.content}' , '{self.role}' , '{self.time}' )"
