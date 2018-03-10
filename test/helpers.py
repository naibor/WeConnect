#where helper functions will be held.
# they help achieve a certain functionality across 
# files without having to repeat yourself

import json

def signup(self):
    return self.test_app.post(
        "/api/v1/auth/register",
        data=json.dumps(dict(
            name="Liz",
            username="naibor",
            email="lix@gmail.com",
            password="7896"
        )),
        content_type="application/json"
    )

def login(self):
    return self.test_app.post(
        "/api/v1/auth/login",
        data=json.dumps(dict(
            username="naibor",
            password="7896"
        )),
        content_type="application/json"
    )
# def save():
#     return self.test_app.pos(
#        )