from flask import jsonify, request, make_response
from app.models import User, user_info, Business, business_info
from app import app
from  flask_jwt_extended import create_access_token

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
    # this is where the data will be stored
    user_info[new_user.username] = {
        "name": new_user.name,
        "username": new_user.username,
        "email":new_user.email,
        "password":new_user.password,
        "business": new_user.business # attach attribute business to user_info
    }
    response = {"message":"welcome you are now registered"}
    # print (response)
    return make_response(jsonify(response), 201) #created

@app.route('/api/v1/auth/login', methods=['POST'])
def signing_in():
    '''signing in'''
    data = request.get_json()
    # from the user_info where our users are stored
    if  not request.is_json:
        return jsonify({"msg": "JSON not in request,data validation failed"}), 400 #bad request
    if user_info:
        # create a variable username to store the key which is username in the
        thisusername = data['username']
    # print(thisusername)
        # if the user name is saved in the info proceed to get username
        if thisusername in user_info:
                # print(thisusername)
            # then assign a variable to the accessed username for the particular user in the user_info
                user = user_info[thisusername]
                # print(user)
            # compare the passwords 
                if user["password"] == data["password"]:
                    # assign token
                    access_token = create_access_token(identity=thisusername)
                    response = {"message": "successfully logged in", "access_token":access_token }
                    return make_response(jsonify(response), 200) #ok
                else:
                    response = {"message": "wrong password"}
                    return make_response(jsonify(response), 401) #unauthorised
        else:
            response = {"message": "user does not exist"}
            return make_response(jsonify(response), 401) #unauthorised
        

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    '''user can reset their password'''
    pass



