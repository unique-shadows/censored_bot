from flask import Flask, redirect
from os import getenv

username = getenv("USERNAME")

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(f"https://t.me/{username}")