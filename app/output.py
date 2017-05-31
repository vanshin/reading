#coding=utf-8
import json
import datetime

from flask import jsonify
from flask import request
from app.models import Reading, Sentence, Sentence_Note, Word, Word_Note
from app import db

def json_default_trans(obj):
    '''json对处理不了的格式的处理方法'''
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    if isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')
    raise TypeError('%r is not JSON serializable' % obj)

def GET_FNone_True(data):
    data = data.to_json()
    data['code'] = 200
    data['message'] = 'SUCCESS'
    print data
    return json.dumps(data, ensure_ascii=True, cls=None, separators=(',', ':'), default = json_default_trans)

def GET_None_True(data):
    data = dict(code=404, message='NOT FOUND')
    return jsonify(data)

def GET_FNone_False(data):
    data['code'] = 200
    data['message'] = 'SUCCESS'
    print data
    return jsonify(data)

def PUT_FNone_True(data):
    data = data.to_json()
    data['code'] = 200
    print data
    return jsonify(data)

def PUT_None_True(data):
    data = dict(code=404, message='NOT FOUND')
    return jsonify(data)

def GET_None_False(data):
    data = dict(code=404, message='NOT FOUND')
    return jsonify(data)

def POST_FNone_True(data):
    data = data.to_json()
    data['code'] = 200
    data['message'] = 'SUCCESS'
    return jsonify(data)

# 根据相应的情况，分别使用不同的处理方法
def output(data=None, to_json=True):
    """ 中间处理函数 """
    methods = {
        'PUT_None_True': PUT_None_True,
        'PUT_FNone_True': PUT_FNone_True,
        'GET_FNone_False': GET_FNone_False,
        'GET_FNone_True': GET_FNone_True,
        'GET_None_True': GET_None_True,
        'GET_None_False': GET_None_False,
        'POST_FNone_True': POST_FNone_True
    }
    data_string = 'None'
    to_json_string = 'True'
    if data:
        data_string = 'FNone'
    if not to_json:
        to_json_string = 'False'

    method_name = request.method + '_' + data_string + '_' + to_json_string
    return methods[method_name](data)


    