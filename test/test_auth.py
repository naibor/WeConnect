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
            # why?i has specified below
            content_type= "application/json"
        )
        self.assertEqual(response.status_code,201)
        self.assertIn("Liz", user_info,msg="user not found")
        

    def test_login(self):
        # response =self.test_app.post(
        #     "/api/vi/auth/ )
        pass

    def test_logout(self):
        pass
        
    def test_reset_password(self):
        pass

    def test_create_business(self):
        '''ensures registered user can register a business'''
        response =self.test_app.post(
            "/api/v1/auth/businesses",
            data =json.dumps (dict(
                bizID="1",
                bizname="lisaP",
                bizlocation="ngara",
                bizcategory="service"
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,201)
        self.assertIn("1", business_info, msg="business not found")
    

    def test_upda_business(self):
        pass

    def test_remove_business(self):
        pass
        
    def test_retreave_all_businesses(self):
        pass

    def test_get_business(self):
        pass

    def test_add_review(self):
        pass

    def test_get_all_review(self):
        pass

    def tearDown(self):
        pass
