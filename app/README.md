
##weConnect

 WeConnect is an E-commerce  platform that bringing businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted in.
The Users have the liberty to register their businesses.Review reviews sent to them by clients.Editing and updating of their business information is made possible and also deleting their businesses.

# Version

python3.5

# Prerequisites

visual studio code
postman

## installation

clone the repo:

```$https://github.com/naibor/WeConnect.git```

cd into the folder:

```$ /weConnect```

create a virtual environment for the project:

```$ virtualenv --python=python3.5 virtualenv-name```

activate the virtual environment:

```$ source virtualenv-name/Scripts/activate```

use virtualenv-wrapper alternative:

```$ mkvirtualenv --python=python3.6 virtualenv-name```


remember to run to install libraries

 ```$pip install -r requirements.txt```
 ##API endpoints

| Endpoint                                   |                  Functionality |
| ------------------------------------------ | ------------------------------ |
| `POST /api/auth/register`                  | Creates a user account         |
| `POST /api/auth/login`                     | Logs in a user                 |
| `POST /api/auth/logout`                    | Logs out a user                |
| `POST /api/auth/reset-password`            | Password reset                 |
| `POST  /api/businesses`                    | Register a busines             |
| `PUT /api/businesses/<businessId>`         | Updates a business profile     |
| `DELETE /api//businesses/<businessId>`     | Remove a business              |
| `GET/api/businesses`                       | Retrieves all businesses       |
| `GET  /api/businesses/<businessId>`        | Get a business                 |
| `POST/api/businesses/<businessId>/reviews` | Add a review for a business    |
| `GET/api/businesses/<businessId>/reviews`  | Get all reviews for a business |

## Running the tests

- use postman to test the endpoints
- use pytest to test the test codes

## Authors

 Naibor Elizabeth Leona