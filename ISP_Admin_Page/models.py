from . import db


class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    prenume = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    nume = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    localitate = db.Column(
        db.String(64),
        index=False,
        nullable=True
    )
    adresa = db.Column(
        db.String(64),
        index=False,
        nullable=True
    )
    telefon = db.Column(
        db.String(64),
        index=False,
        nullable=True
    )
    adresa_ip = db.Column(
        db.String(64),
        index=False,
        nullable=True
    )
    abonament = db.Column(
        db.String(64),
        index=False,
        nullable=True
    )

    def __repr__(self):
        return '<Client {}>'.format(self.prenume)

class Abonament(db.Model):
    __tablename__ = 'abonament'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    valoare = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    vitezamin = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    vitezamax = db.Column(
        db.String(64),
        index=False,
        nullable=True
    )

class IP(db.Model):
    __tablename__ = 'ip'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    adresa_ip = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    client = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    activ = db.Column(
        db.String(64),
        index=False,
        nullable=True
    )

    def __repr__(self):
        return '<IP {}>'.format(self.adresa_ip)