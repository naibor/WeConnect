import json
from unittest import TestCase
from instance.config import app_config
from app import app
from app.models import User, user_info, Business, business_info, catalog
# we create a tests class that inherits from testcase,the one imported up there
class RegistrationTestCase(TestCase):

    # setsup after every test
    def setUp(self):
        app.config.from_object(app_config['testing'])
        self.test_app = app.test_client()
        self.register_response = self.test_app.post(
            "/api/v1/auth/register",
            data=json.dumps(dict(
                name="Liz",
                username="naibor",
                email="lix@gmail.com",
                password="7896"
            )),
            content_type="application/json"
        )
       
    def test_register_account(self):
        '''ensures users are created on the register account'''
        response = self.register_response
        self.assertEqual(response.status_code,201)
        self.assertIn("naibor", user_info, msg="user not found")
        self.assertIn("welcome you are now registered", str(response.data)) 

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
        # get response data and deserialize
        response_data = json.loads(response.data)
        self.assertIn("access_token", response_data)


    # def test_reset_password(self):
    #     response = self.test_app.post(
    #         "/api/v1/auth/reset-password",
    #         data=json.dumps(dict(  # serialilzes this dictionary..
    #             name="liz",
    #             username="naibor",
    #             email="lix@gmail.com",
    #             password="7896"
    #         )),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("lix@gmail.com", user_info, msg="email not found")

    #     pass


    # def test_logout(self):
    #     response = self.test_app.post(
    #         "/api/v1/auth/login",
    #         data=json.dumps(dict(
    #             username="naibor",
    #             password="7896"
    #         )),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.status_code, 200)

    #     pass
        
   

        
        # self.assertEqual(response.status_code,200)
        

    
    def tearDown(self):
        pass
