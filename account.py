from flask import Blueprint, render_template, request, session
from database import get_database_connection
from datetime import datetime

account_bp = Blueprint('account', __name__)

@account_bp.route('/')
def index():
    return render_template('index.html')