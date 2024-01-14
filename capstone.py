from flask import Blueprint, render_template, request, session
from database import get_database_connection

capstone_bp = Blueprint('capstone', __name__)

@capstone_bp.route('/capstoneDetails/<int:cp_id>')
def capstoneDetails(cp_id):
    # Retrieve session variables
    account_type = session.get('account_type')

    # Connect to the database
    connection = get_database_connection()
    cursor = connection.cursor()

    # Query the specific capstone project by ID
    query = "SELECT * FROM capstone_projects WHERE project_id = %s"
    cursor.execute(query, (cp_id,))
    capstone_project = cursor.fetchone()

    if account_type == "Normal User":
        return render_template('capstoneDetails.html', capstone_project = capstone_project, account_type='Normal User')
    elif account_type == "Administrator":
        return render_template('capstoneDetails.html', capstone_project = capstone_project, account_type='Administrator')