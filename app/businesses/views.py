from flask import jsonify, request, make_response
from app.models import user_info, Business, business_info
from app import app

@app.route('/api/auth/v1/business', methods=['POST'])
def create_business():
    '''register a business'''
    data = request.get_json()

    new_business = Business(
        data["bizID"],
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
    # one user can have several businesses
    # '''this ensures the user_infois not empty'''
    if user_info:
        for user in user_info:
            user_info[user]['business'].append(business_info[new_business.bizID])
 
    response = "message ""you have registered a business"

    return make_response(jsonify(response),201)
