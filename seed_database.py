import os
import server
import model
import crud
import json

os.system('dropdb photos')
os.system('createdb photos')

model.connect_to_db(server.app)
model.db.create_all()

#creation of users

crud.create_user("John","Doe","johnDoe@gmail.com","johnDoe")
crud.create_user("Jane","Derick","janeDerick@gmail.com","janeDoe")
crud.create_user("Kamala","Harris","kamalaHarris@gmail.com","kamalaHarris")
crud.create_user("Sourav","Patel","souravPatel@gmail.com","souravPatel")
crud.create_user("Arnab","Dey","arnabDey@gmail.com","arnabDey")
crud.create_user("Sivarman","Rajaganpathy","SivarmanRajaganpathy@gmail.com","SivarmanRajaganpathy")
crud.create_user("Rachit","Shrivastava","RachitShrivastava@gmail.com","RachitShrivastava")
crud.create_user("Edlund","Connor","edlundConnor@gmail.com","edlundConnor")
crud.create_user("Harish","Doddi","harishDoddi@gmail.com","harishDoddi")
crud.create_user("Mishfad","Veedu","mishfadVeedu@gmail.com","mishfadVeedu")
crud.create_user("Vivek","Khatana","vivekKhatana@gmail.com","vivekKhatana")

#creation of photo records using json upload

with open('./images.json') as f:
    photos_data = json.loads(f.read())
    #print("success")
for photo in photos_data:

    img_path = photo['img_path']
    location = photo['location']
    description = photo['description']
    gps_url = photo['gps_url']
    popular_url = photo['popular_url']
    
    crud.create_photo(img_path, location, description, gps_url, popular_url)
    
    
#getting Two users by user_id

user1=crud.get_user_by_id(1)
user2=crud.get_user_by_id(2)

#getting Two Photos by photo_id

photo1=crud.get_photo_by_id(1)
photo2=crud.get_photo_by_id(2)

# Creating Two ratings by the same user on two different photos
rating1=crud.create_rating(1,"This is an excellent Photo",photo1,user1)
rating2=crud.create_rating(2,"This is a good Photo",photo2,user1)

# Creating  ratings by the another user2 on a common photo ; photo 1
rating3=crud.create_rating(3,"This is an average Photo",photo1,user2)

# Creating two favorite Photos by user1 and one common by user2
favphoto1=crud.create_favorite_photo(user1,photo1)
favphoto2=crud.create_favorite_photo(user1,photo2)
favphoto3=crud.create_favorite_photo(user2,photo1)



