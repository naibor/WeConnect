from flask import jsonify, request, make_response
from app.models import User, user_info, Business

from app import app

from  flask_jwt_extended import create_access_token

import re 

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    '''register user'''
    # get post data in form of a dict
    data = request.get_json()
    # new_user is an instance of class User (new_user object) using the value above ie.data
    new_user = User(
        data["name"],
        data["username"],
        data["email"],
        data["password"]
        )
    

    if new_user.name in user_info:
        response = {"message":"user already exist"}
        return make_response(jsonify(response),409) #user conflict

#validate user's name
    invalid_name = new_user.validate_name()
    if invalid_name:
        print(invalid_name)
        return make_response(jsonify({"message": invalid_name}), 400)

    #validate username
    invalid_username = new_user.validate_username()
    if invalid_username:
        print(invalid_username)
        return make_response(jsonify({"message": invalid_username}), 400)

    #validate email
    invalid_email = new_user.validate_email()
    if invalid_email:
        print(invalid_email)
        return make_response(jsonify({"message": invalid_email}),400)

    #validate password
    invalid_password = new_user.validate_password()
    if invalid_password:
        print(invalid_password)
        return make_response(jsonify({"message": invalid_password}),400)

   #this stores the user information in user info
    new_user.save_user()
    response = {"message":"welcome you are now registered"}
    return make_response(jsonify(response), 201) #created

@app.route('/api/v1/auth/login', methods=['POST'])
def signing_in():
    '''signing in'''
    data = request.get_json()
    if  not request.is_json:
        return jsonify({"msg": "JSON not in request,data validation failed"},400)  #bad request
    if user_info:
        this_username = data['username']
    # print(thisusername)
        # if the user name is saved in the info proceed to get username
        if this_username in user_info:
                # print(thisusername)
            # then assign a variable to the accessed username for the particular user in the user_info
                user = user_info[this_username]
                # print(user)
            # compare the passwords 
                if user["password"] == data["password"]:
                    # assign token
                    access_token = create_access_token(identity=this_username)
                    response = {"message": "successfully logged in", "access_token":access_token }
                    return make_response(jsonify(response), 200) #ok
                else:
                    response = {"message": "wrong password"}
                    return make_response(jsonify(response), 401) #unauthorised
        else:
            response = {"message": "user does not exist"}
            return make_response(jsonify(response), 401) #unauthorised
    response = {"message": "No users exist. Please register."}
    return make_response(jsonify(response), 401)
        

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    '''user can reset their password'''
    pass



