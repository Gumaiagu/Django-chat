# Simple Django chat

This chat was made by me to to understand the Django framework, Django channels and Django channels layers.

## Executing

To execute, use a [virtual environment](https://docs.python.org/3/library/venv.html) or the Python environment.

First, install the libraries with:

#### Unix/macOs:
```
python3 -m pip install django 'channels[daphne]' channels_redis markupsafe
```

#### Window:
```
py -m pip install django 'channels[daphne]' channels_redis markupsafe
```

### Executing

To execute, use inside the main directory (the same as the "manage.py"):

#### Unix/macOs

```
python3 manage.py runserver
```

#### Window

```
py manage.py runserver
```

To change the port, use the number of the port at the end of the code.

## With Ngrok

This project was made with everything you need to use Ngrok, but we only need to change the project's settings.

In "chat/settings.py" change SAFE_HOST for the URL of the site.

### How to use

Use this to run the HTTP server:

```
ngrok http 8000
# if you want to change the port change the number
```

You'll get a link like "https://8fb3-2804-ae0-82d8-3100-279d-cdb6-720b-9438.ngrok-free.app".

So, use the link without "https://", in this example, you'll use "8fb3-2804-ae0-82d8-3100-279d-cdb6-720b-9438.ngrok-free.app".

Then, the site will work correctly.

## Admin

First, use this command to create a super user:

#### Unix/macOs

```
python3 manage.py createsuperuser
```

#### Window

```
py manage.py createsuperuser
```

Then, it will appear 3 question, the user name, the email (that is not obligatory) and the password, you'll need to answer them.

To access admin, enter in the main page, then, add "admin/" in the URL.

Use the user that you created to log in the admin site.

Then you'll be able to manipulate the database.

## Banning

Banning people is a little difficult, because we need to enter in the admin page, add someone to the group called banned, and save the changes.

With just a few people, it's easy to ban, but, when there's a lot of them to ban, it'll be boring and difficult. I didn't add a good system for it.

## Possible errors

### DisallowedHost at /

This error happens when you're using Ngrok (or other services) and you forgot to add the URL in the SAFE_HOST variable inside the settings.py file, there's more details in the Ngrok theme.