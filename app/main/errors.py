from config import RRET

from . import main
from flask import request, jsonify
from app.output import output

@main.app_errorhandler(404)
def page_not_found(e):
    return output(RRET.RES_NOT_EXIST)

@main.app_errorhandler(500)
def internal_server_error(e):
    return output(RRET.RES_NOT_EXIST)
