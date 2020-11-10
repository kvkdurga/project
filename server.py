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

    photo = crud.get_photo_by_id(photo_id)

    return render_template('photo_details.html',photo=photo) 

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""
    # if (request.method=='POST'):
    #     print("its a post request")
    # else:
    #     print("its not a post request")
    # print(request.method)
    # fname = request.form.get('fname')
    # lname = request.form.get('lname')
    email = request.form.get('email')
    # print(email)
    password = request.form.get('password')
    # print(password)

    user = crud.get_user_by_email(email)
    if user:
        flash('Welcome!')
        if (user.password == password):
        #return render_template("all_photos.html")
        #photos = crud.get_photos()
            return redirect('/all_photos')
        else:
            flash("Invalid password, please try again")
            return redirect('/')
    else:
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')
        crud.create_user(fname, lname, email, password)
        flash('Account created! Please log in.')
        return redirect('/')
        # return "User does not exist"
    return  "user does not exist"

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)