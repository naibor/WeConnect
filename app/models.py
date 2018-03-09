business_info = {} # users and their business infos found here
catalogue =[] #a list of business names
class User:
    '''user model'''
    user_info = {}  # where user data is stored
    # the class constructor with parameters
    def __init__(self, name, username, email, password ):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.business=[]

    # @staticmethod

    # def validate_auth_data(self, data):
    #     '''a method that validates data from user '''
    # special_character = (" ", '$',' %' ,' & ', '*','>','<' )
    # for char in data:
    #     if char in special_character:

    #         return "no special characters allowed." 
            
    #         pass
    # if data :
    #         username=data["username"]
    #         if username :
        #validate the email
        #validate username
        #validate password
        
class Business:
    '''business model'''
    def __init__(self, business_name, business_location, business_category, business_owner):
        self.business_name = business_name
        self.business_location = business_location
        self.business_category = business_category
        self.business_owner = business_owner
        # Auto assign id on creation
        if len(business_info) == 0:
            self.business_ID = 1
        else:
            self.business_ID = len(business_info)+1


    def save (self):
        '''user business info can be saved'''
        new_business = {
            "id": self.business_ID,
            "name": self.business_name,
            "location": self.business_location,
            "category": self.business_category,
            "onwer": self.business_owner
        }
        business_info[self.business_ID] = new_business#addind a dict to a dict
    
class Review:
    '''review model'''
    def __init__(self,review):
        self.review = review

# Other CRUD helper functions
# Deleting business
def delete(business_ID):
    del business_info[business_ID]

# this is the method to create and returns catalogue .
def get_business_catalogue():
    '''a user can get and view business catalogue'''
    if business_info:
        for key in business_info:
            catalogue.append(dict(
                name=business_info[key]["business_name"],#getting the value of keys from business info
                category=business_info[key]["business_category"],
                location=business_info[key]["business_location"]
            ))
        return catalogue
    else:
        return "no items"
