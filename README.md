# Bucketlist
flask web service application which manages bucketlists. It always for multiple users where each user can only manage and view his/hers bucketlists. It implements token based authentication to manage security.

# Requirements
- Postgres Database
- Python Flask api

**[# Installation](url)**

1. Clone the repo on github

`https://github.com/kjagoo/Bucketlist`

2. Install requirements

`pip install -r requirements.txt`

3. Create database bucketlist 
   -  edit in `manage.py` `postgresql+psycopg2://[username]:[password]@localhost:5432/bucketlist`
   - `createdb bucketlist`
   -  `python manage.py db init`
   -  `python manage.py db migrate`


**[Running the Program](url)**

`python run.py`

**[Usage Routes](url)**

register new user
- `POST` - `127.0.0.1:5000/auth/register/`

login
- `POST` - `127.0.0.1:5000/auth/login/`

get list of all bucketslists
- `GET` - `127.0.0.1:5000/bucketlists/`

add a bucketlist
- `POST` - `127.0.0.1:5000/bucketlists/`

edit a bucketlist
- `PUT` - `127.0.0.1:5000/bucketlists/<id>`

delete a bucketlist
- `DELETE` - `127.0.0.1:5000/bucketlists/<id>`

get and display a specific bucketlist
- `GET` - `127.0.0.1:5000/bucketlists/<id>`

add bucketlist item
- `POST` - `127.0.0.1:5000/bucketlists/<id>/items/`

get a specific bucketlist item
- `GET` - `127.0.0.1:5000/bucketlists/<id>/items/<id>`

edit and update a bucketlist item
- `PUT` - `127.0.0.1:5000/bucketlists/<id>/items/<id>`

delete bucketlist item
- `DELETE` - `127.0.0.1:5000/bucketlists/<id>/items/<id>`

**[#Tests](url)**

<img width="723" alt="screen shot 2017-01-27 at 7 57 29 am" src="https://cloud.githubusercontent.com/assets/8224798/22361045/e6c6a506-e466-11e6-914c-60fb57207741.png">


**[#Usage guide](url)**
- register a new user
 `POST` - `127.0.0.1:5000/auth/register/`
<img width="1047" alt="screen shot 2017-01-25 at 3 28 42 pm" src="https://cloud.githubusercontent.com/assets/8224798/22339329/a3c303b0-e3fa-11e6-9541-045cb35ab77c.png">

- login using credentials after registration
 `POST` - `127.0.0.1:5000/auth/login/`
<img width="1045" alt="screen shot 2017-01-25 at 3 29 41 pm" src="https://cloud.githubusercontent.com/assets/8224798/22339301/8779cc3e-e3fa-11e6-96f8-a32406bd3890.png">

- get bucketlist and use the token provided passed as header
 `GET` - `127.0.0.1:5000/bucketlists/`
<img width="1132" alt="screen shot 2017-01-25 at 3 26 44 pm" src="https://cloud.githubusercontent.com/assets/8224798/22339337/ad1f00b2-e3fa-11e6-978d-d20c46402655.png">

- add bucketlist
 `POST` - `127.0.0.1:5000/bucketlists/`
<img width="926" alt="screen shot 2017-01-27 at 7 37 52 am" src="https://cloud.githubusercontent.com/assets/8224798/22360726/974e234e-e463-11e6-8247-86d74b79b6ff.png">

- get bucketlist
 `GET` - `127.0.0.1:5000/bucketlists/`
<img width="1038" alt="screen shot 2017-01-25 at 3 51 34 pm" src="https://cloud.githubusercontent.com/assets/8224798/22339254/64fec90c-e3fa-11e6-82e6-9ca9430b14e0.png">

- add bucketlist item
 `POST` - `127.0.0.1:5000/bucketlists/`
<img width="966" alt="screen shot 2017-01-27 at 7 47 30 am" src="https://cloud.githubusercontent.com/assets/8224798/22360850/efd44f24-e464-11e6-90b6-590b71fea811.png">

**[# Credits](url)**

Joshua Kagenyi 
