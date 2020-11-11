"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
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

    photos = crud.get_photos()

    return render_template('all_photos.html', photos=photos)

@app.route('/all_photos/<photo_id>')
def show_photo(photo_id):
    """display details of a specific photo."""
    flash(photo_id)
    photo = crud.get_photo_by_id(photo_id)
    session['photo_id']=photo_id

    return render_template('photo_details.html',photo=photo) 

@app.route('/user_details/')
def user_details():
    """display all details of a user"""

    
    return render_template('user_details.html') 

@app.route('/user_details/<user_id>')
def view_user_details(user_id):
    """display all details of a user"""

    user = crud.get_user_by_id(user_id)
    print(user.user_id)
    #user_fav_photos = crud.get_favorite_photos_of_user_by_user_id(user_id)

    return render_template('display_user_details.html',user=user)


@app.route('/my_fav_photo')
def fav_photo(user_id):
    """display favorite photo of an user"""

    fav_photo = crud.get_favorite_photo_of_user_by_user_id(user_id)
    pass

@app.route('/create_rating', methods=['POST'])
def create_rating():
    comments=request.form.get('comments')
    rating=request.form.get('rating')
    print ("rating",rating)
    print ("Comments",comments)
    user=crud.get_user_by_id(session['user_id'])
    photo=crud.get_photo_by_id(session['photo_id'])
    rating_rec=crud.create_rating(rating,comments,photo,user)
    print(rating_rec.user.fname)
    return redirect('/all_photos')


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




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)