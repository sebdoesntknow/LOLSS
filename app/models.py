from flask import current_app
from . import db, login_manager
from flask.ext.login import UserMixin

# App perms
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

# User base
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.username

## Streams 
class Streams(db.Model):
    __tablename__ = 'streams'
    id = db.Column(db.Integer, primary_key=True)
    stream_name = db.Column(db.String(64), unique=True, index=True)
    current_champ = db.Column(db.String(64))

    def __repr__(self):
        return 'Stream %r' % self.stream

## Summoners linked to streams
class Summoners(db.Model):
    __tablename__ = 'summoners'
    id = db.Column(db.Integer, primary_key=True)
    summoner_riot_id = db.Column(db.Integer)
    summoner_name = db.Column(db.String(64))

    def __repr__(self):
        return 'Summoner %r' % self.summoner
