user_info={}
# where user data is stored


class User:
    '''user model'''
    # the class constructor with parameters
    def __init__(self,name,username,email,password):
        self.name = name
        self.username=username
        self.email = email
        self.password = password


class Business:
    '''business model'''

    def __init__(self,business_ID,business_name,location,category):
        self.business_ID = business_ID
        self.business_name = business_name
        self.location = location
        self.category = category


class Review:
    '''review model'''
    def __init__(self,review):
        self.review = review





