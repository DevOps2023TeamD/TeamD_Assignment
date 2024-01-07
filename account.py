from flask import Blueprint, render_template, request, session
from database import get_database_connection
from datetime import datetime

account_bp = Blueprint('account', __name__)

@account_bp.route('/')
def index():
    return render_template('index.html')

@account_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        # Get username and password inputs
        username = request.form['username']
        password = request.form['password']

        # Connect to database
        connection = get_database_connection()
        cursor = connection.cursor()

        # SQL Query to check login credentials and status
        query = "INSERT INTO accounts (username, password, creation_date, account_type, approval_status) VALUES (%s, %s, %s, 'Normal User', 'Pending')"
        # Get current datetime
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query, (username, password, current_date))
        connection.commit()
        return render_template('register.html', message='Successful registration')
    else:
        return render_template('register.html')