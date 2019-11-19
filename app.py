# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:24:38 2019

@author: 91720
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/movie_details"
mongo = PyMongo(app)


