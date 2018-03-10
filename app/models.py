import re

business_info = {} # users and their business infos found here
catalog =[] #a list of business names
user_info = {}  # where user data is stored
class User:
    '''user model'''
    # the class constructor with parameters
    def __init__(self, name, username, email, password ):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.business=[]

    def validate_name(self):
        '''validates user's name'''
        if len(self.name) >= 2:
            # compiles the character combinations from start check alphanumeric then end
            name_re = re.compile(r"^\w+$")
            result_name = re.fullmatch(name_re, self.name)
            if not result_name:
                return "incorrect username,no special character or spaces allowed"


    def validate_username(self):
        '''validates username'''
        if len(self.username) >= 2:
            username_re = re.compile(r"^\w+$") #compiles the character combinations from start check alphanumeric then end
            result_name = re.fullmatch(username_re, self.username)
            if not result_name:
                return "incorrect username,no special character or spaces allowed"

    def validate_password(self):
        '''validates password'''
        if self.password:
            # from start check alphanumeric then end
            psw_re = re.compile(r"^\S+$")
            result_password = re.fullmatch(psw_re, self.password)
            if not result_password:
                return "incorrect password,no spaces allowed"
            

    def validate_email(self):
        '''validates emails'''
        if self.email:
            email_re=re.compile(r"^[\w.+]+@\w+\.\+w+$")#accounts for \w words and . ,@ and word ,more words then end
            result_email = re.fullmatch(email_re, self.email)
            if result_email:
                # print (result_email)
                return "incorrect email,try again"
        
    def save_user(self):
        '''users are saved here'''
        new_user = {
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "business": self.business
        }

        user_info[self.username] = new_user
        
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
    
    def validate_business_name(self):
        if len(self.business_name) >= 2:
            business_name_re = re.compile(r"^\w+$")
            result_business = re.fullmatch(business_name_re, self.business_name)
            if not result_business:
                return "incorrect business name, no special character or spaces allowed"

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

# this is the method to create and returns catalog .
def get_business_catalog():#not working as expected
    '''a user can get and view business catalog'''
    if business_info:
        for item in business_info:
            catalog.append(dict(
                name=business_info[item]["business_name"],#getting the value of keys from business info
                category=business_info[item]["business_category"],
                location=business_info[item]["business_location"]
            ))
            # print (catalog)
        return catalog
    else:
        return "no items"
