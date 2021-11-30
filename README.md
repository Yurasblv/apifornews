Project dockerized.
Code reviewed by black, flake8, pyright. :shipit:

```
[Deployment on heroku]
```
https://testapinews.herokuapp.com/
```
Steps:
Clone repository:
1 : git clone 
```
https://github.com/Yurasblv/apifornews.git
```
    1.1: cd apifornews

2: docker-compose up(migrations apply automatically)

3: docker exec -it <container:app> bash
   script >> python manage.py createsuperuser
   
```

```
Trying to make postman checks 
```
1. https://www.postman.com/spaceflight-pilot-77997851/workspace/my-workspace/collection/16571220-daa0ce18-f71d-476d-8ae9-6bfec8a65677
2. https://www.getpostman.com/collections/8d861b672e443ccb6410
