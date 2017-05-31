#coding=utf-8
from flask import Blueprint

show = Blueprint('show', __name__)
from . import views