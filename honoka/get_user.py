# encoding:utf-8
from app.models import User, User_Reading_Map

import redis

def get_id(**kwargs):

    User.query.filter_by()