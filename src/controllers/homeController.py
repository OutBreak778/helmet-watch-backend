from flask import jsonify

def home():
    return jsonify({'message': "Hello world"}), 201

def hello():
    return jsonify({'message': "This is hello page"}), 201
