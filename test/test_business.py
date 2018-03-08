import json
from unittest import TestCase
from app import app
from app.models import User, user_info, Business, business_info


class BusinessTestCase(TestCase):

    # setsup after every test
    def setUp(self):
        self.test_app = app.test_client()
        user_info.clear()

    def test_create_business(self):
        '''ensures registered user can register a business'''
        response = self.test_app.post(
            "/api/v1/business",
            bizdata=json.dumps(dict(
                bizID="1",
                bizname="lisaP",
                bizlocation="ngara",
                bizcategory="service"
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("1", business_info, msg="business not found")


    def test_update_business(self):
        '''a user can update his business information'''
        response = self.test_app.post(
            "/api/v1/update_business",
            data=json.dumps(dict(
                bizID="1",
                bizname="lisaP",
                bizlocation="ngara",
                bizcategory="service"
            )),
            content_type="application/json"
        )
        self.assertEqual(response.status_code,200)


        # confirm that the information updates by overwriting the previous data
        # self.assertNotEqual(new_bidata.new_business, business_info.newbizdata)



    def test_remove_business(self):
        '''a user can remove a business'''
        response = self.test_app.delete(
            "/api/v1/business/1",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("bizID", business_info, msg="successfully deleted business")

    #     pass
        
    # def test_retreave_all_businesses(self):
    #     pass

    # def test_get_business(self):
    #     pass

    # def test_add_review(self):
    #     pass

    # def test_get_all_review(self):
    #     pass
