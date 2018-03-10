import json
from unittest import TestCase
from instance.config import app_config
from app import app
from app.models import User, user_info, Business, business_info,catalog
from test.helpers import signup, login


class BusinessTestCase(TestCase):

    # setsup after every test
    def setUp(self):
        app.config.from_object(app_config['testing'])
        # seting up testing configurations
        self.test_app = app.test_client()
        self.business = {"business_name": "lisaP",
                         "business_location" : "ngara",
                         "business_category" : "service"
                        } #contains bussiness parameters to be passed
         #signs up a test user               
        signup_response = signup(self)
        #asserts that he has been signed in
        self.assertEqual(signup_response.status_code, 201)
        # login our test user
        login_response =login(self)
        # asserts that he is logged in
        self.assertEqual(login_response.status_code,200)
        # get the response data,and deserialize it(which is msg and token)
        response_data = json.loads(login_response.data)
        # assert that that token exsists in response data
        self.assertIn("access_token", response_data)
        # store the token for later use
        self.authorization = dict(Authorization= "Bearer " + response_data["access_token"])
        # we register a business using the authorization token
        self.register_business = self.test_app.post( #post is a request(containing endpoint,required authorization)
            "/api/v1/business",
            # pass the authorization to header(define nature of request) and bearer
            headers=self.authorization,
            data=json.dumps(self.business),
            content_type="application/json"
        )

        user_info.clear()

    def test_create_business(self):
        '''ensures registered user can register a business'''
        response = self.register_business
        self.assertEqual(response.status_code, 201)
        self.assertIn(1, business_info, msg="business not found")

    def test_remove_business(self):
        '''a user can remove a business'''
        reg_response = self.register_business
        
        self.assertEqual(reg_response.status_code, 201)
        response = self.test_app.delete(
            "/api/v1/business/1",
            headers=self.authorization,#add authorization for this too
            content_type="application/json"
            )
        self.assertEqual(response.status_code, 200)
        
        self.assertNotIn("business_name", catalog, msg="deleted from catalog")
        self.assertNotIn("business_ID", business_info, msg="successfully deleted business")

        
    def test_get_businesses(self):
        # Add a business (to confirm we have something in catalogue)
        self.register_business
        response = self.test_app.get(
            "api/v1/business",
            headers=self.authorization,
            content_type="application/json"
           )
        response_data=json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        #checks if we have an item in catalogue
        catalog = response_data["catalog"]
        self.assertTrue(len(catalog) > 0)

    # def test_update_business(self):
    #     '''a user can update his business information'''
    #     response = self.test_app.post(
    #         "/api/v1/update_business",
    #         data=json.dumps(dict(
    #             business_ID="1",
    #             business_name="lisaP",
    #             business_location="ngara",
    #             business_category="service"
    #         )),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.status_code,200)


        # confirm that the information updates by overwriting the previous data
        # self.assertNotEqual(new_bidata.new_business, business_info.newbizdata)



    

    # def test_get_a_business(self):
    #     response = self.test_app.post(
    #         "api/v1/business/<int:business_ID>",
    #         data=json.dumps(dict(
               
    #         )),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.status_code, 200)

    #     pass
    

    # def test_add_review(self):
    #     pass

    # def test_get_all_review(self):
    #     pass
