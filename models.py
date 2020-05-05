from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

volunteers_streets_associations = db.Table('volunteers_streets',
                                           db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteers.id')),
                                           db.Column('street_id', db.Integer, db.ForeignKey('streets.id')))

streets_districts_association = db.Table('streets_districts',
                                         db.Column('streets_id', db.Integer, db.ForeignKey('streets.id')),
                                         db.Column('districts_id', db.Integer, db.ForeignKey('districts.id')))


class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    userpic = db.Column(db.String())
    phone = db.Column(db.String())
    streets = db.relationship('Street', secondary=volunteers_streets_associations, back_populates='volunteers')


class Street(db.Model):
    __tablename__ = 'streets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    volunteers = db.relationship('Volunteer', secondary=volunteers_streets_associations, back_populates='streets')
    districts = db.relationship('District', secondary=streets_districts_association, back_populates='streets')


class District(db.Model):
    __tablename__ = 'districts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    streets = db.relationship('Street', secondary=streets_districts_association, back_populates='districts')






