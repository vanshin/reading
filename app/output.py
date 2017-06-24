#coding=utf-8
import json
import datetime
import config

from flask import jsonify
from flask import request
from app.models import Reading, Sentence, Sentence_Note, Word, Word_Note, User_Reading_Map
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
    return jsonify(data)
    # return json.dumps(data, ensure_ascii=True, cls=None, separators=(',', ':'), default = json_default_trans)


def output(code, data=None):
    message = config.MES[code]
    ret = {}
    ret['code'] = code
    ret['message'] = message
    if not data:
        return jsonify(ret)
    if isinstance(data, db.Model) and data is not None:
        data = data.to_json()
    ret.update(data)
    return jsonify(ret)

def output2():
    pass
