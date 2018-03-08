from flask import jsonify, request, make_response
from app.models import User, Business, business_info, get_business_catalogue
from app import app
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/api/v1/business', methods=['POST'])
@jwt_required
def create_business():
    '''register a business'''
    data = request.get_json()
    # get the user name using jwt
    current_user=get_jwt_identity()

    new_business = Business(
        data["business_name"],
        data["business_location"],
        data["business_category"],
        current_user
     )
#this adds the created business to a list of all businesses
    new_business.save()
    
    business_info[new_business.business_ID] = {
        "business_ID": new_business.business_ID,
        "business_name": new_business.business_name,
        "business_location": new_business.business_location,
        "business_category": new_business.business_category,
        "owner": current_user
    }
    
    response = {"message": "you have registered a business",
                "business": business_info[new_business.business_ID]
                }
    return make_response(jsonify(response),201)
 

@app.route('/api/v1/business', methods=['GET'])
@jwt_required
def get_a_businesses():
    '''user can get a business'''
    #get business catalogue is a method in models
    catalogue = get_business_catalogue() 
    response ={"catalogue":catalogue}
    return make_response(jsonify(response), 200)


@app.route('/api/v1/business/<int:business_ID>', methods=['DELETE'])
@jwt_required
def remove_business(business_ID):
    '''user can delete a business'''
    business_info.pop(business_ID)
    response = "message", "successfully delete business"
    return make_response(jsonify(response),200)

    # if User.user_info:  # '''this ensures the user_info is not empty'''
    #     for user in User.user_info:
    #         User.user_info[user]['business'].append(
    #             business_info[new_business.business_ID])


@app.route('/api/v1/business/<int:business_ID>', methods=['GET'])
def get_business():
    '''user can get all businesses'''
    
    response = "message", "successfully delete business"
    return make_response(jsonify(response), 200)


@app.route('/api/v1/business/<int:business_ID>',methods=['PUT'])
def update_business():
    '''user can update their business information'''


    response = "message", "successfully delete business"
    return make_response(jsonify(response), 200)


