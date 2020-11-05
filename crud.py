""" Create,Read,Update,Delete(CRUD) operations."""

from model import db, User, connect_to_db
#, Photo, Favorite_Photo, Rating

def create_user(fname,lname, email,password):
    """create and return a new user."""

    user = User(fname=fname,lname=lname,email=email,password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """ Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """ Return a user by primary key."""

    return User.query.filter(User.user_id == user_id).first()

def get_user_by_fname_lname(fname,lname):
    """ Return a user by fname and lname."""

    full_name = fname + " " + lname

    return User.query.get(full_name)

def get_user_by_email(email):
    """ Return a user by email."""

    return User.query.filter(User.email == email).first()


if __name__ == '__main__':
    from server import app
    
    connect_to_db(app)