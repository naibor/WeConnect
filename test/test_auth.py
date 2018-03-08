import json
from unittest import TestCase
from app import app
from app.models import User,user_info, Business, business_info
# we create a tests class that inherits from testcase,the one imported up there
class RegistrationTestCase(TestCase):

    # setsup after every test
    def setUp(self):
        self.test_app = app.test_client()
        user_info.clear()
       
    def test_register_account(self):
        '''ensures users are created on the register account'''
        response =self.test_app.post(
            "/api/v1/auth/register",
            # this tell json to serialize the data
            data = json.dumps (dict(
                name="Liz",
                username="naibor",
                email="lix@gmail.com",
                password="7896"
            )),
            # why?i have specified below
            content_type= "application/json"
        )
        # print(response)
        self.assertEqual(response.status_code,201)
        self.assertIn("naibor", user_info,msg="user not found")
        # self.assertEqual("message":"welcome you are now registered", msg=response )

    def test_signin(self):
        response =self.test_app.post(
            "/api/v1/auth/login",
            data = json.dumps (dict(
                username= "naibor",
                password= "7896"
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        # self.assertIn("naibor", user_info, msg="user not found")
        # self.assertEqual("7896", user_info["password"])
        # print("this is the", response)
        # self.assertEqual(response.status_code, 404)
        # self.assertNotEqual("5698",user_info["password"], msg="wrong password")
        # self.assertEqual(response.status_code, 404)


    def test_logout(self):
        pass
        
    def test_reset_password(self):
        response = self.test_app.post(
            "/api/v1/auth/reset-password",
            data=json.dumps(dict( #serialilzes this dictionary..
                name="liz",
                username="naibor",
                email="lix@gmail.com",
                password="7896"
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,200 )
        self.assertIn("lix@gmail.com",user_info, msg="email not found")

        
        # self.assertEqual(response.status_code,200)
        

    
    def tearDown(self):
        pass
