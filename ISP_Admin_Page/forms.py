from wtforms import StringField, SelectField
from wtforms.validators import InputRequired

from .models import Client, Abonament, IP

from flask_wtf import FlaskForm

class AdaugaClientForm(FlaskForm):
    prenume = StringField('Prenume', validators=[
                          InputRequired(message='Trebuie introdus un prenume!')])
    nume = StringField('Nume', validators=[InputRequired(
        message='Trebuie introdus un nume!')])
    localitate = StringField('Localitate')
    adresa = StringField('Adresa')
    telefon = StringField('Telefon')
    adresa_ip = StringField('adresa_ip')
    abonament = SelectField('Abonament', choices=[(
        '30 RON', '30 RON'), ('50 RON', '50 RON'), ('100 RON', '100 RON')])


class AdaugaAbonamentForm(FlaskForm):
    valoare = StringField('Valoare', validators=[
        InputRequired(message='Trebuie introdusa o valoare in RONI!')])
    vitezamin = StringField('VitezaMin', validators=[InputRequired(
        message='Trebuie introudsa o viteza min (in kbps)!')])
    vitezamax = StringField('VitezaMax', validators=[
        InputRequired(message='Trebuie introdusa o viteza maxima (in kbps)!')])


class AdaugaIPForm(FlaskForm):
    adresa_ip = StringField('IP', validators=[
        InputRequired(message='Trebuie introdusa o valoare in RONI!')])
    client = StringField('Client', validators=[
        InputRequired(message='Trebuie introdus numele clientului')])
    activ = SelectField('Activ', choices=[('NU', 'NU'), ('DA', 'DA')])
