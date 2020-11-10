import os
import server
import model
import crud
import json

model.connect_to_db(server.app)
model.db.create_all()

