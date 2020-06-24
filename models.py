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
        unique=True,
        nullable=False
    )
    nume = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    localitate = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    adresa = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    telefon = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    adresa_ip = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    abonament = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return '<Client {}>'.format(self.prenume)