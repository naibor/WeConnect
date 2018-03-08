
user_info = {}
# where user data is stored
business_info = {}
all_businesses = []
# where business registrations are stored
bizID = 0
class User:
    '''user model'''
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

    #     if data :
    #         username=data["username"]
    #         if username :

        #validate the email
        #validate username
        #validate password
        
class Business:
    '''business model'''
    def __init__(self, bizname, bizlocation, bizcategory, bizowner):
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

    # @staticmethod #it has a logical connection but doesnt really depend on the 
    # i need to use the get_business_catalogue method but dont need the (self) in my method  below    
    # def get_business_catalogue():
    #     next_num = -1
    #     for item in all_businesses:
    #         if all_businesses:
    #             next_num +=1
    #             catalogue = all_businesses[next_num]["bizname"}

    #         else:
    #             return "no items"
    
class Review:
    '''review model'''
    def __init__(self,review):
        self.review = review


