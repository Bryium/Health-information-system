# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HealthProgram(db.Model):
    __tablename__ = 'health_programs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<HealthProgram {self.name}>"

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    programs = db.relationship('HealthProgram', secondary='client_health_program', backref=db.backref('clients', lazy='dynamic'))

    def __repr__(self):
        return f"<Client {self.client_name}>"

# Junction Table for Many-to-Many relationship between clients and programs
class ClientHealthProgram(db.Model):
    __tablename__ = 'client_health_program'

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id', ondelete='CASCADE'), primary_key=True)
    health_program_id = db.Column(db.Integer, db.ForeignKey('health_programs.id', ondelete='CASCADE'), primary_key=True)