from flask import jsonify

def output(data, code, location=None):
    data['code'] = code
    data['location'] = location
    return jsonify(data)