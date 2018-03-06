user_info={}
# where user data is stored
business_info = {}
# where business registrations are stored
bizID = 0
class User:
    '''user model'''
    # the class constructor with parameters
    def __init__(self,name,username,email,password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password


class Business:
    '''business model'''
    
    
    def __init__(self,bizID,bizname,bizlocation,bizcategory):
        self.bizID = bizID
        self.bizname = bizname
        self.bizlocation = bizlocation
        self.bizcategory = bizcategory
        # business_info.append(bizID)
        

class Review:
    '''review model'''
    def __init__(self,review):
        self.review = review





