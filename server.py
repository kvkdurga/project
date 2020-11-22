"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, url_for)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!

@app.route('/',methods=['GET'])
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/all_photos')
def all_photos():
    """View all photos."""

    if session['user_id'] == "":
        #flash(" You are not signed in.Please sign in")
        return redirect('/')
        
    photos = crud.get_photos()
    user = crud.get_user_by_id(session['user_id'])

    return render_template('all_photos.html', photos=photos, user=user)

@app.route('/all_photos/<photo_id>')
def show_photo(photo_id):
    """display details of a specific photo."""

    if session['user_id'] == "":
        #flash(" You are not signed in.Please sign in")
        return redirect('/')

    photo = crud.get_photo_by_id(photo_id)
    session['photo_id']=photo_id

    return render_template('photo_details.html',photo=photo) 

@app.route('/user_details/')
def user_details():
    """display all details of a user"""
    if session['user_id'] == "":
        #flash(" You are not signed in.Please sign in")
        return redirect('/')

    return render_template('user_details.html') 

@app.route('/user_details/<user_id>')
def view_user_details(user_id):
    """display all details of a user"""

    if session['user_id'] == "":
        #flash(" You are not signed in.Please sign in")
        return redirect('/')

    user = crud.get_user_by_id(user_id)
        
    user_fav_photos = crud.get_favorite_photos_of_user_by_user_id(user_id)

    user_rated_recs = crud.get_all_rating_recs_by_user(user_id)
    
    return render_template('display_user_details.html',user=user, user_fav_photos=user_fav_photos, user_rated_recs=user_rated_recs)


@app.route('/create_fav_photo', methods=['POST'])
def create_fav_photo():
    
    user=crud.get_user_by_id(session['user_id'])
    photo=crud.get_photo_by_id(session['photo_id'])
    photo_id = session['photo_id']
    url_str = '/all_photos/' + photo_id
    
    test_fav_recs = crud.get_favorite_photos_of_user_by_user_id(user.user_id)
    for fav_rec in test_fav_recs:
        if str(fav_rec.photo_id) == photo_id:
            flash(" THIS IS ALREADY YOUR FAVORITE PHOTO ")
            return redirect(url_str)
    fav_rec=crud.create_favorite_photo(user, photo)
    # print("FAVORITE PHOTO CREATED")

    # print("PHOTO ID IS :", photo_id)    
    # print("Favorite PHoto id is ",fav_rec.photo_id)
    return redirect(url_str)

    

@app.route('/create_rating', methods=['POST'])
def create_rating():

    
    user=crud.get_user_by_id(session['user_id'])
    photo=crud.get_photo_by_id(session['photo_id'])
    photo_id = session['photo_id']
    url_str = '/all_photos/' + photo_id
    # print ("rating",rating)
    # print ("Comments",comments)
    
    test_rating_recs = crud.get_all_photos_rated_by_user(user.user_id)
    for rate_rec in test_rating_recs:
        if str(rate_rec.photo_id) == photo_id:
            flash("THIS PHOTO WAS ALREADY RATED BY YOU ")
            return redirect(url_str)
        
    comments=request.form.get('comments')
    rating=request.form.get('rating')
    rating_rec=crud.create_rating(rating,comments,photo,user)
   
    return redirect(url_str)

#********************************* AJAX*******************
@app.route('/stats_on_photo', methods =['POST'])
def stats_on_photo():
    """ Get all user for a favorite photo """

    photo_id = session['photo_id']

    return render_template('/stats_photo.html')


@app.route('/countOfUsersWhoRatedPhoto')
def countOfUsersWhoRatedPhoto():
    """ Get the count of all users who rated photo """

    photo_id = session['photo_id']
    user_recs= crud.get_all_users_who_rated_photo(photo_id)
    count = len(user_recs)
    user_recs_json = []
    #user_recs_json.append(count)

    if (len != 0):
        for user_rec in user_recs:
            fname = user_rec.fname
            lname = user_rec.lname
            user_rec_json = {

                 "name" : fname + ' '+ lname
                
            }
            user_recs_json.append(user_rec_json)

    return jsonify(user_recs_json)
    #return "<h1>hello world</h1>"

@app.route('/get_img_data')
def get_img_data():
    """ jsonify the photo data"""

    photo_id = session['photo_id']
    photo_rec = crud.get_photo_by_id(photo_id)
    img_path = photo_rec.img_path
    location = photo_rec.location
    gps_url = photo_rec.gps_url
    popular_url = photo_rec.popular_url

    json_data = {
        'photo_id': photo_id,
        'img_path': img_path,
        'location': location,
        'gps_url': gps_url,
        'popular_url':popular_url

    }
    return jsonify(json_data)

#*******************************Google Maps*****************************

@app.route('/get_my_maps')
def get_my_maps():
    """ get the google map for the photo"""

    #photo_id = session['photo_id']

    return render_template('/stats_on_maps.html')

#***************************Login/Register******************************

@app.route('/register_user', methods=['POST'])
def register_user():
    """Create a new user."""
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash(" The user with this email exists. Register with a different email.")
        return redirect('/')
    else:
        crud.create_user(fname, lname, email, password)
        flash('Account created! Please log in.')
        return redirect('/')
 

@app.route('/login_user', methods=['POST'])
def login_user():
    """Create a new user."""

    email = request.form.get('email')
    print(email)
    password = request.form.get('password')
    print(password)

    user = crud.get_user_by_email(email)
    print(user)
    if user:
        
        if (user.password == password):
            flash('Welcome!')
            session['user_id']=user.user_id
        #return render_template("all_photos.html")
        #photos = crud.get_photos()
            return redirect('/all_photos')
        else:
            flash("Invalid password, please try again")
            return redirect('/')

    else:  

        flash("you are login email is not registered")
        return redirect('/')


@app.route('/logout_user', methods=['POST'])
def logout_user():
    """ user logout"""
    session['user_id'] = ""
    session['photo_id'] = ""

    return redirect('/')

#*****************************Main******************************

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)