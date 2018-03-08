@app.route('/api/v1/auth/login', methods=['POST'])
def signing_in():
    '''signing in'''
    data = request.get_json()

def __init__(self,bizname,bizlocation,bizcategory, bizowner):
        self.bizname = bizname
        self.bizlocation = bizlocation
        self.bizcategory = bizcategory
        self.bizowner = bizowner
        # Auto assign id on creation
        if len(all_businesses) == 0:
            self.id = 1
        else:
            self.id = all_businesses[-1]["id"]+1


    def save (self):
        '''user business info can be saved'''
        new_biz = {
            "id": self.id,
            "name": self.bizname,
            "location": self.bizlocation,
            "category": self.bizcategory,
            "onwer": self.bizowner
        }
            
        all_businesses.append(new_biz)

    @staticmethod #it has a logical connection but doesnt really depend on the 
    # i need to use the get_business_catalogue method but dont need the (self) in my method  below    
    def get_business_catalogue():
        pass


        from flask import jsonify, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, user_info, Business, business_info
from app import app

@app.route('/api/v1/business', methods=['POST'])
@jwt_required
def create_business():
    '''register a business'''
    current_user = get_jwt_identity()
    bizdata = request.get_json()

    new_business = Business(
        bizdata["bizname"],
        bizdata["bizlocation"],
        bizdata["bizcategory"],
        current_user
    )

    new_business.save()    
    # this displays the created business layout 
    business_info[new_business.id]={
        "bizID": new_business.id,
        "bizname": new_business.bizname,
        "bizlocation":new_business.bizlocation,
        "bizcategory": new_business.bizcategory,
        "owner": current_user
    }

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
    return make_response