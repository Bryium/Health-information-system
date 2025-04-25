from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Client, db, HealthProgram

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

# Route for registering a new client
@main_bp.route('/register-client', methods=['GET', 'POST'])
def register_client():
    if request.method == 'POST':
       
        client_name = request.form['client_name']
        age = request.form['age']
        gender = request.form['gender']

        
        new_client = Client(client_name=client_name, age=age, gender=gender)
        db.session.add(new_client)

        
        selected_programs = request.form.getlist('programs')

       
        for program_id in selected_programs:
            program = HealthProgram.query.get(program_id)
            if program:
                new_client.programs.append(program)

        
        db.session.commit()

        
        flash('Client registered successfully!', 'success')
        return redirect(url_for('main.view_client', client_id=new_client.id))

    
    programs = HealthProgram.query.all()
    return render_template('register_client.html', programs=programs)

# Route for viewing a client's profile
@main_bp.route('/client/<int:client_id>', methods=['GET'])
def view_client(client_id):
    client = Client.query.get_or_404(client_id)
    return render_template('view_client.html', client=client)

@main_bp.route('/search-client', methods=['GET', 'POST'])
def search_client():
    if request.method == 'POST':
        
        client_name = request.form.get('client_name')

        
        client = Client.query.filter(Client.client_name.ilike(f'%{client_name}%')).first()

        
        if client:
            return redirect(url_for('main.view_client', client_id=client.id))

        
        flash('Client not found!', 'danger')
        return redirect(url_for('main.search_client'))

    return render_template('search_client.html')

