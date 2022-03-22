

- you start from the example codes displayed on the website

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

```

`__name__` refers to the file name in which the codes live.


I accidently discovered another way to run flask

you can write codes `app.run()` at  the end of the `.py` file but to be honest it's not a really good practice in my opinion. It demonstrates the person doesn't read documentation properly.

We usually run codes in the command line such as `export FLASK_APP= [YOUR FILE NAME.py]` and `flask run` after that. 

Turning on debug mode by writing `app.config['DEBUG'] = True` or run `export FLASK_ENV=development` and `flask run` without `app.config[`DEBUG`]=True`