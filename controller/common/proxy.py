from flask import Blueprint

proxy = Blueprint('proxy', __name__)


@proxy.route('/grab')
def grab():
    return "hello"