""" seeding database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

model.connect_to_db(server.app)
model.db.create_all()

#create 5 users with first name,last name, email and password

for n in range(5):
    fname = input()
    lname = input()
    email = input()
    password = input()

    user = crud.create_user(fname,lname,email,password)

