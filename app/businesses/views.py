from flask import jsonify, request, make_response
from app.models import User, Business, business_info, get_business_catalog
from app import app
from flask_jwt_extended import jwt_required, get_jwt_identity
import re

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
    new_business.validate_business_name()
#this adds the created business to a list of all businesses
    new_business.save()
    # print(business_info)
    
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
def get_businesses():
    '''user can get a business'''
    #get business catalogue is a method in models
    catalog = get_business_catalog() 
    response ={"catalog":catalog}
    return make_response(jsonify(response), 200)


@app.route('/api/v1/business/<int:business_ID>', methods=['DELETE'])
@jwt_required
def remove_business(business_ID):
    '''user can delete a business'''
    catalog = get_business_catalog()
    # print (catalog)
    business = business_info.pop(business_ID)
    business_name = business["business_name"]
    print(business)
    for item in catalog:
        if item["name"] == business_name:
            catalog.remove(item)
    response = "message", "successfully delete business"
    return make_response(jsonify(response),200)


@app.route('/api/v1/business/<int:business_ID>', methods=['GET'])
def get_business():
    '''user can get all businesses'''
    
    response = "message", "successfully delete business"
    return make_response(jsonify(response), 200)


@app.route('/api/v1/business/<int:business_ID>',methods=['PUT'])
@jwt_required
def update_business(business_ID):
    '''user can update their business information'''
    current_user = get_jwt_identity()

    new_business_details = request.get_json()
    if business_ID in business_info:
        current_details = business_info[business_ID]
        if current_details["owner"] == current_user:
            current_details["name"] = new_business_details["name"]
            current_details["location"] = new_business_details["location"]
            current_details["category"] = new_business_details["category"]
            response = {"message": "Updated successfuly", "business_details": business_info[business_ID]}
        else:
            response = {"message": "You can only update your own business details."}
    else:
        response = {"message": "Business doesn't exist"}

    return make_response(jsonify(response), 200)

    # if User.user_info:  # '''this ensures the user_info is not empty'''
    #     for user in User.user_info:
    #         User.user_info[user]['business'].append(
    #             business_info[newi_business.business_ID])

