# Elite Lab 4: Controllers

## Intro
In this lab, we will be building our first HTTP APIs with Flask. We have provided the sandwich API as a demo, and by the end, you should also have a simple messages API running locally on your computer.

Since this is the first time we'll be getting into the nitty gritty with Python code, I've prepped some quick reference links down below to help you out:

* https://www.python.org/doc/
* https://www.tutorialspoint.com/python/python_functions.htm
* https://realpython.com/python-for-loop/
* https://flask.palletsprojects.com/en/1.1.x/quickstart/
* https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing

* https://realpython.com/instance-class-and-static-methods-demystified/

Remember to always use Google and StackOverflow as a resource if you are not sure how to implement something. Feel free to reach out to me as well.


## Objective
Your goal is to build the routing and controllers for the messages API.

We have provided you with starter and demo code. You do NOT need to change anything in the `app/models.py` file. All of your work should go into `app/controllers.py` file. You can use the sandwiches API code as a working reference (you do not need to change this code).

We have also provided two scripts inside the `scripts/ ` directory that you can run in the command line (see below). These scripts use python to simplify sending HTTP requests to your local server.

The sandwiches script should work immediately (since the sandwich API is already built out).

Lab is complete when you are able to successfully run the `check_if_lab_complete` function in the `scripts/call_messages_api.py` file.

If you look closely into that file, it will test for these APIs to work:
* delete a message (`DELETE /messages/<message_id>`)
* create message (`POST /messages/`)
* get all messages (`GET /messages/`)
* get a message by id (`GET /messages/<message_id>`)
* filter messages by chat id (`GET /chat/<chat_id>`)
* get last number of messages (`GET /last/?count=<number of message>`)


## Set Up
* Fork and clone the repository to your local dev environment

* Activate your virtual environment
```
python -m venv venv
source venv/bin/activate
```

* Install the dependencies to your virtual environment
```
pip install -r requirements.txt
```

* Start up your SQLite database with:
```
FLASK_APP=lab-app.py flask db init
FLASK_APP=lab-app.py flask db migrate -m "my first migration"
FLASK_APP=lab-app.py flask db upgrade
```

* Spin up the local web server with:
```
FLASK_APP=lab-app.py FLASK_ENV=development flask run
```

* Open up a new terminal window

* Navigate to the Lab directory

* Run the sandwich test script with:
```
python scripts/call_sandwiches_api.py
```


## Lab Steps
* First try to run the messages test script:
```
python scripts/call_message_api.py
```

* Notice how it fails with an Assertion Error

* Complete the lab by building out each API. You should be working on passing each assertion statement step-by-step (this is called test driven development). I would recommend this order:
  * delete a message (`DELETE /messages/<message_id>`)
  * create message (`POST /messages/`)
  * get all messages (`GET /messages/`)
  * get a message by id (`GET /messages/<message_id>`)
  * filter messages by chat id (`GET /chat/<chat_id>`)
  * get last number of messages (`GET /last/?count=<number of message>`)

* When you are done, run the script to completion and watch it print out `Done!`


## Lab Advice
* I highly recommend using the demo code as a reference. It should help you get through the first 4 APIs.
* The last API will require some research into getting the URL arguments (the count) from Flask.
* You do not need to modify `models.py`. I have already provided all the functions needed to complete the lab. Instead, use it as a reference for what you can retrieve from the database.
* Use the bottom of the sandwich and message scripts to play around with the APIs and see what calling them does. Being able to test them in isolation should be useful
  * Use the `#` character to comment out certain lines to prevent them from running
* You should not need to modify the schema, but if your database goes out of sync with your schema, you can run these commands:
```
FLASK_APP=lab-app.py flask db stamp head
FLASK_APP=lab-app.py flask db migrate
FLASK_APP=lab-app.py flask db upgrade
```
