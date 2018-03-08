from flask import jsonify, request, make_response
from app.models import user_info, Business, business_info
from app import app
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/api/v1/business', methods=['POST'])
@jwt_required
def create_business():
    '''register a business'''
    data = request.get_json()

    new_business = Business(
        data["bizname"],
        data["bizlocation"],
        data["bizcategory"],
        current_user 
     )

    new_business.save()

    # this displays the created business layout
    business_info[new_business.id] = {
        "bizID": new_business.id,
        "bizname": new_business.bizname,
        "bizlocation": new_business.bizlocation,
        "bizcategory": new_business.bizcategory,
        "owner": current_user
    }
    # '''this ensures the user_infois not empty'''
    if user_info:
        for user in user_info:
            user_info[user]['business'].append(business_info[new_business.bizID])
 
    response = {"message": "you have registered a business",
                "business": business_info[new_business.id]
                }
    return make_response(jsonify(response),201)

@app.route('/api/v1/business/<int:bizID>', methods=['DELETE'])
def remove_business( bizID ):
    '''user can delete a business'''
    print(business_info)
    business_info.pop(bizID)
    print(business_info)
    response = "message", "successfully delete business"
    return make_response(jsonify(response),200)

