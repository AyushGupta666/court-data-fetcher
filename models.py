from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class QueryLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String(50))
    case_number = db.Column(db.String(50))
    filing_year = db.Column(db.String(10))
    raw_response = db.Column(db.Text)
