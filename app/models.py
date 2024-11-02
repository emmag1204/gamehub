from . import db

class Section(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    image = db.Column(db.String(200))

class Game(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(100), db.ForeignKey('section.name'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    platform = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200))

    section_rel = db.relationship('Section', backref='games')