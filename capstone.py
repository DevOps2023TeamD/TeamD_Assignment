from flask import Blueprint, render_template, request
from database import get_database_connection

capstone_bp = Blueprint('capstone', __name__)

@capstone_bp.route('/createCapstone', methods=['GET', 'POST'])
def feature1():
    if request.method == "POST":
        cp_name = request.form['cp-name']
        cp_title = request.form['cp-title']
        cp_noOfStudents = request.form['cp-noOfStudents']
        cp_academicYear = request.form['cp-academicYear']
        cp_companyName = request.form['cp-companyName']
        cp_pointOfContract = request.form['cp-pointOfContact']
        cp_desc = request.form['cp-description']

        # Get radio input value
        cp_roleOfContact = request.form.get('cp-roleOfContact')
        print(cp_roleOfContact)

        # Connect to database
        connection = get_database_connection()
        cursor = connection.cursor()

        #SQL Query base
        query = """INSERT INTO capstone_projects (person_in_charge, role_of_contact, num_students, academic_year, capstone_title, company_name, company_contact, project_description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        
        cursor.execute(query, (cp_name, cp_roleOfContact, cp_noOfStudents, cp_academicYear, cp_title, cp_companyName, cp_pointOfContract, cp_desc))
        connection.commit()

        return render_template('createCapstone.html', message="Successful Capstone Creation")
    else:
        return render_template('createCapstone.html')