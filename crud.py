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

def create_favorite_photo(user,photo):
    """ Return a favorite photo of an user"""

    favorite_photo = Favorite_Photo(user=user,photo=photo)
    
    db.session.add(favorite_photo)
    db.session.commit()

    return favorite_photo

def get_fav_photo_rec_by_user_and_photo(user_id, photo_id):
    """get a favorite photo of an user"""
    
    fav_photo_rec = Favorite_Photo.query.filter(Favorite_Photo.user_id==user_id, Favorite_Photo.photo_id==photo_id)
    
    return fav_photo_rec
    
def get_favorite_photos_of_user_by_user_id(user_id):
    """get all favorite_photos of an user"""

    fav_photo_recs = Favorite_Photo.query.filter_by(user_id=user_id).all()
    photo_recs = [] 
    #print("length of favorite photo records", len(fav_photo_recs))
    for id in range(len(fav_photo_recs)):
        photo_id = fav_photo_recs[id].photo_id
        photo_rec = get_photo_by_id(photo_id)
        photo_recs.append(photo_rec)
        
    return photo_recs

def get_users_of_a_favorite_photo(photo_id):
    """get all users of a favorite photo"""

    fav_recs = Favorite_Photo.query.filter(Favorite_Photo.photo_id==photo_id).all()
    #print("lengthFavREcs",len(fav_recs))
    user_recs = [] 

    for id in range(len(fav_recs)):
        user_id = fav_recs[id].user_id
        user_rec = get_user_by_id(user_id)
        user_recs.append(user_rec)

    return user_recs


def create_rating(rating, comments, photo, user):
    """create and return comments and favorite rating of a photo by an user"""

    rate_and_comment = Rating(rating=rating, comments=comments, photo=photo, user=user)

    db.session.add(rate_and_comment)
    db.session.commit()

    return rate_and_comment

def get_all_photos_rated_by_user(user_id):
    """get all photos that were rated by an user."""

    rating_recs = Rating.query.filter_by(user_id=user_id).all()
    photo_recs = [] 
    for id in range(len(rating_recs)):
        photo_id = rating_recs[id].photo_id
        photo_rec = get_photo_by_id(photo_id)
        photo_recs.append(photo_rec)
    return photo_recs

def get_all_rating_recs_by_user(user_id):
    """get all photos that were rated by an user."""

    rating_recs = Rating.query.filter_by(user_id=user_id).all()
    
    return rating_recs

def get_all_users_who_rated_photo(photo_id):
    """get all users who have rated a particular photo."""

    rating_recs = Rating.query.filter_by(photo_id=photo_id).all()
    print("RATING RECORDS = ", rating_recs)
    user_recs = [] 
    #print(len(rating_recs))
    for id in range(len(rating_recs)):
        user_id = rating_recs[id].user_id
        #photoId = rating_recs[id].photo_id
        #print("user id is ",user_id)
        #print("photo id is",photoId)
        user_rec = get_user_by_id(user_id)
        user_recs.append(user_rec)
    return user_recs

if __name__ == '__main__':
    from server import app
    
    connect_to_db(app)