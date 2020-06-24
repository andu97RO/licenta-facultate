from datetime import datetime as dt

from flask import current_app as app
from flask import redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired

from .models import Client, db

from flask_bootstrap import Bootstrap

Bootstrap(app)


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


@app.route('/clienti', methods=['GET'])
def clienti():
    return render_template(
        'clienti.html',
        clienti=Client.query.all(),
        title="Clienti"
    )


@app.route('/clienti/adauga', methods=['POST', 'GET'])
def clienti_adauga():
    form = AdaugaClientForm()

    if form.validate_on_submit():
        client_nou = Client(prenume=form.prenume.data,
                            nume=form.nume.data,
                            localitate=form.localitate.data,
                            adresa=form.adresa.data,
                            telefon=form.telefon.data,
                            adresa_ip=form.adresa_ip.data,
                            abonament=form.abonament.data)
        db.session.add(client_nou)
        db.session.commit()
        return redirect(url_for('clienti'))

    return render_template('clientiform.html', form=form)
