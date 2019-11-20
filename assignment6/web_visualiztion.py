from visualize import *
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('')
