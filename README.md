# django-task-manager
Simple task tracking manager written on Django


## Check it on Render
[Task manager deployed on Render](https://task-manager-m1jl.onrender.com)

## Installing / Getting started
Python3 with pip must be installed and ready

1. Clone project from Github repository
```sh
git clone https://github.com/amber-marichi/django-task-manager.git
cd django-task-manager
```
2. Set up and activate environment

For Mac and Linux systems:
```sh
python3 -m venv venv
source venv/bin/activate
```
For Windows:
```sh
python -m venv venv
venv\Scripts\activate
```
3. Install requirements
```sh
pip install -r requirements.txt
```
4. Run migrations to set up database
```sh
python manage.py migrate
```
5. Start local django server
```sh
python manage.py runserver
```

Now service can be accessed by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

## Some features
* Authenticate as a user
* User can create task, browse available tasks, join team-members on existing, and track between ongoing and finished.
* Find out who are on task with you by see their details, contact and history.


## To check out
use these creds:
```sh
login: test.user
password: u$er4321
```

## Preview
![Screenshot 2023-04-16 at 21-16-00 Hacelo - New task](https://user-images.githubusercontent.com/72259870/232333666-5b94a8c8-88d9-4f0e-81d2-5361d15832ce.png)
![Screenshot 2023-04-16 at 21-14-30 Hacelo - Task 23 Fix User Template](https://user-images.githubusercontent.com/72259870/232333667-9c7cf20e-f6e7-4253-9679-8b92c8fb79e8.png)
![Screenshot 2023-04-16 at 21-13-49 Hacelo - Main taskboard](https://user-images.githubusercontent.com/72259870/232333668-5e72643b-be07-4ca6-b909-fa2b2a96e214.png)