from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, HealthProgram

# Define the blueprint
main_bp = Blueprint('main', __name__)

# Route for the root URL (/)
@main_bp.route('/')
def home():
    return render_template('index.html')  

@main_bp.route('/create_program', methods=['GET', 'POST'])
def create_program():
    if request.method == 'POST':
        name = request.form.get('program_name')

        if not name:
            return redirect(url_for('main.create_program', message="Name is required"))

        if HealthProgram.query.filter_by(name=name).first():
            return redirect(url_for('main.create_program', message="Program already exists"))

        new_program = HealthProgram(name=name)
        db.session.add(new_program)
        db.session.commit()

        return redirect(url_for('main.create_program', message="Program created successfully!"))

    programs = HealthProgram.query.all()
    message = request.args.get('message')  
    return render_template('create.html', programs=programs, message=message)
