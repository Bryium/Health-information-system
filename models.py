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