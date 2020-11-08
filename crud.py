""" Create,Read,Update,Delete(CRUD) operations."""

from model import db, User, Photo, Favorite_Photo, Rating, connect_to_db

def create_user(fname,lname, email,password):
    """create and return a new user."""

    user = User(fname=fname,lname=lname,email=email,password=password)
    
    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """ Return all users."""

    return User.query.all()

def get_user_by_fname(fname):
    """ Return a user by first name."""

    return User.query.filter(User.fname == fname).first()

def get_users_by_fname(fname):
    """ Return all users by first name."""

    return User.query.filter(User.fname== fname).all()

def get_user_by_lname(lname):
    """ Return a user by last name."""

    return User.query.filter(User.lname== lname).first()

def get_users_by_lname(lname):
    """ Return all users by last name."""

    return User.query.filter(User.lname== lname).all()

def get_user_by_id(user_id):
    """ Return a user by primary key."""

    return User.query.filter(User.user_id == user_id).first()

def get_user_by_email(email):
    """ Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_photo(img_path, location, description, gps_url, popular_url):
    """ create and return a photo"""

    photo = Photo(img_path=img_path, location=location, description=description, gps_url=gps_url, popular_url=popular_url)

    db.session.add(photo)
    db.session.commit()

    return photo

def get_photos():
    """ Return all photos"""

    return Photo.query.all()

def get_photo_by_id(photo_id):
    """ Return a photo by it's primary key"""

    return Photo.query.filter(Photo.photo_id==photo_id).first()

def get_photo_by_location(location):
    """Return a photo by location"""

    return Photo.query.filter(Photo.location==location).first()

def create_favorite_photo(user_id,photo_id):
    """ Return a favorite photo of an user"""

    favorite_photo = Favorite_Photo(user_id=user_id,photo_id=photo_id)
    
    db.session.add(favorite_photo)
    db.session.commit()

    return favorite_photo

def get_favorite_photo_of_user_by_user_id(user_id):
    """get a favorite photo of an user"""

    fav_photo_rec = Favorite_Photo.query.filter(user_id==user_id).first()
    photo_id = fav_photo_rec.photo_id
    return get_photo_by_id(photo_id)
    
def get_favorite_photos_of_user_by_user_id(user_id):
    """get all favorite_photos of an user"""

    fav_photo_recs = Favorite_Photo.query.filter(user_id==user_id).all()
    photo_recs = [] 
    for id in range(len(fav_photo_recs)):
        photo_id = fav_photo_recs[id].photo_id
        photo_rec = get_photo_by_id(photo_id)
        photo_recs.append(photo_rec)
    return photo_recs

# def create_rating(rating,date_liked,comments, photo,user):
#     """create and return comments and favorite rating of a photo by an user"""

#     rate_and_comment = Rating(rating=rating,date_liked=date_liked,comments=comments,photo=photo,user=user)

#     db.session.add(rate_and_comment)
#     db.session.commit()

#     return rate_and_comment


if __name__ == '__main__':
    from server import app
    
    connect_to_db(app)