import os
from flask import Flask

#app =Flask(__name__)
BASE_PATH = os.path.abspath(os.environ.get('HOME'))

print(BASE_PATH)
