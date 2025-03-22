from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    doodle = db.Column(db.Text, nullable=False)
    generated = db.Column(db.Text, nullable=False)
    creationdate = db.Column(db.DateTime, nullable=False)
