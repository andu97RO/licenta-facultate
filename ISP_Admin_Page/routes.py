from datetime import datetime as dt

from flask import current_app as app
from flask import redirect, render_template, url_for, request
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


@app.route('/clienti/<int:page>', methods=['GET'])
def clienti(page=1):
    per_page = 4
    clienti = Client.query.paginate(page, per_page, error_out=False)

    return render_template(
        'clienti.html',
        clienti=clienti,
        title="Clienti",
    )


@app.route('/clienti/afiseaza/<id_client>')
@app.route('/clienti/modifica/<id_client>', methods=['GET'])
def clienti_modifica(id_client):
    pass


@app.route('/clienti/arata/<id_client>', methods=['GET'])
def clienti_arata(id_client):
    pass


@app.route('/clienti/sterge/<id_client>', methods=['GET'])
def clienti_sterge(id_client):
    pass


@app.route('/factura/<id_client>', methods=['GET'])
def factura(id_client):
    pass


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
