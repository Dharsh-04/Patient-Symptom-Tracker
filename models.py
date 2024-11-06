from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    severity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)  # Column name is 'date'

    def __repr__(self):
        return f'<Symptom {self.description}>'
