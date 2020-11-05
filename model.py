""" Models for Durga's Photo viewings app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """ A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    access_code = db.Column(db.String)
    pwd = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email}>'

# class Photo(db.Model):
#     """ A photo."""

#     __tablename__ = 'photos'

#     photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     img = db.Column(db.String) 
#     description = db.Column(db.Text)
#     location = db.Column(db.String)
#     date_taken = db.Column(db.DateTime)
#     gps_url = db.Column(db.String)
#     popular_url = db.Column(db.String)

#     def __repr__(self):
#         return f'<Photo photo_id={self.photo_id} location={self.location} date_taken={self.date_taken}>'

# class Favorite_Photo(db.Model):
#     """ A favorite photo of an user."""

#     __tablename__ = 'favoritephotos'

#     fav_photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     photo_id = db.Column(db.Integer, db.ForeignKey('photos.photo_id'))

#     def __repr__(self):
#         return f'<FavoritePhoto fav_photo_id={self.fav_photo_id}>'

# class Rating(db.Model):
#     """A photo rating and comments."""

#     __tablename__ = 'ratings'

#     rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     rating = db.Column(db.Integer)
#     date_liked = db.Column(db.DateTime)
#     comments = db.Column(db.String)
#     photo_id = db.Column(db.Integer, db.ForeignKey('photos.photo_id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

#     def __repr__(self):
#         return f'<Rating rating_id={self.rating_id} rating={self.rating}>'


def connect_to_db(flask_app, db_uri='postgresql:///photos', echo=True):

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    #from server import app
    from flask import Flask

    app = Flask(__name__)

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    





