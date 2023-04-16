from flask import Flask, render_template
from dotenv import load_dotenv
import pyrebase
import os


app = Flask(__name__)

# load_dotenv()

# config = {
#     "apiKey": os.environ.get("APIKEY"),
#     "authDomain": os.environ.get("AUTHDOMAIN"),
#     "databaseURL": os.environ.get("DATABASEURL"),
#     "storageBucket": os.environ.get("STORAGEBUCKET")
#     }

# firebase = pyrebase.initialize_app(config)
# db = firebase.database()

@app.route("/")
def home():

    return render_template('index.html')