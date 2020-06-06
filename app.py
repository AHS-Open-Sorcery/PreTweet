from flask import Flask, render_template, request
from dataRetrieval import *

app = Flask("HTNE-Project")


@app.route("/")
def index():
	return ""


@app.route("/create-post")
def create_post():
	return ""


@app.route("/display-posts")
def display():
	return ""

