# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:05:59 2019

@author: 91720
"""


from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request


@app.route('/add', methods=['POST'])  #CREATE OPERTAION
def add_movie():
    _json = request.json
    _movie_name = _json['movie_name']
    _actors = _json['actors']
    _genre = _json['genre']
    _release_date = _json['release_date']
    
    if _movie_name and _actors and _genre and _release_date and request.method == 'POST':
        
        mongo.db.movie.insert({'movie_name': _movie_name, 'actors': _actors, 'genre': _genre, 'release_date':_release_date})
        resp = jsonify('Movie details added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()
        
@app.route('/movies')   #Read Operation
def movies():
    movies = mongo.db.movie.find()
    resp = dumps(movies)
    return resp
        
@app.route('/movie/<id>')  #Read operation by giving "Id"
def movie(id):
    movie = mongo.db.movie.find_one({'_id': ObjectId(id)})
    resp = dumps(movie)
    return resp

@app.route('/update', methods=['PUT'])   #UPDATE OPERATION
def update_movie():
    _json = request.json
    _id = _json['_id']
    _movie_name = _json['movie_name']
    _actors = _json['actors']
    _genre = _json['genre']
    _release_date = _json['release_date']
    
    if _movie_name and _actors and _genre and _release_date and _id and request.method == 'PUT':
        # save edits
        mongo.db.movie.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'movie_name': _movie_name, 'actors': _actors,'genre': _genre,'release_date':_release_date}})
        resp = jsonify('Movie details updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()
        
@app.route('/delete/<id>', methods=['DELETE']) #DELETE OPERATION
def delete_movie(id):
    mongo.db.movie.delete_one({'_id': ObjectId(id)})
    resp = jsonify('Movie deleted successfully!')
    resp.status_code = 200
    return resp
        
@app.errorhandler(404)  #ErroR Handling
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
        'Suggestion':'Please try valid URL'
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()
