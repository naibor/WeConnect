from flask import jsonify, request, make_response
from app.models import User, user_info
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
# this turns the response in to json format
    return make_response(jsonify(response), 201)

# user_info[new_user.name]=dict(
#     name=new_user.name,
#     username=new_user.email,
#     email=new_user.email,
#     password=new_user.password
# ) this is another way of writting the nested dict



