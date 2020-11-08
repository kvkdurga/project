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
crud.create_user("Jane","Doe","janeDoe@gmail.com","janeDoe")
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
    
    



# crud.create_photo("./data/images/img1.jpg","Halebidu, Karnataka, India","Halebidu is a small town located in Hassan District in Karnataka state. It is a hindu temple for god Shiva. It's famous for its architecture with intricate detials.",  "https://en.wikipedia.org/wiki/Halebidu","https://en.wikipedia.org/wiki/Halebidu")


# crud.create_photo("./static/images/img2.jpg",
#         "Maui", "View of mountains from black sand beach on Hana Hwy in Maui, Hawaii.Black sand beaches are so beautiful with cyrstal clean waters and black pebbles on the beach.","https://www.hawaii-guide.com/maui/beaches/black-sand-beach-maui","https://www.tourmaui.com/black-sand-beach/")

# crud.create_favorite_photo(1,1)
# crud.create_favorite_photo(1,2)

