from flask import Flask
import os
import server
import model
import crud
import json







app = Flask(__name__)
model.connect_to_db(app)
model.db.create_all()

iterate=0

if (iterate==0):
    crud.create_user("Jose","Doe","jedis5s@gmail.com","Does")
    iterate=1
# Replace this with routes and view functions!


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)