from flask import jsonify, request, make_response
from app.models import User, user_info, Business, business_info
from app import app 

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    '''register user'''
    # get post data in form of a dict
    data = request.get_json()

    print(data)
    # new_user is an instance of class User (new_user object) using the value above ie.data
    new_user = User(
        data["name"],
        data["username"],
        data["email"],
        data["password"]
    )
# this is where the data will be stored
    user_info[new_user.name] = {
        "name": new_user.name,
        "username": new_user.username,
        "email":new_user.email,
        "password":new_user.password
    }
    print(user_info)

    response = {"message":"welcome you are now registered"}
# the make_response function(inbuilt) turns the response in to json format
    return make_response(jsonify(response), 201)

'''register a business'''
@app.route('/api/auth/v1/business', methods=['POST'])
def create_business():
    data =request.get_json()

    print(data)

    new_business = Business(
       int(data["bizID"]),
        data["bizname"],
        data["bizlocation"],
        data["bizcategory"]
    )

    business_info[new_business.bizID]={
        "bizID": new_business.bizID,
        "bizname": new_business.bizname,
        "bizlocation":new_business.bizlocation,
        "bizcategory": new_business.bizcategory

    }
    print(business_info)

    response = "message ""you have registered a business"

    return make_response(jsonify(response),201)




