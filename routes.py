from datetime import datetime as dt
from flask import request, render_template, make_response, redirect, url_for
from flask import current_app as app
from flask_wtf import FlaskForm
from .models import db, Client

class AdaugaClientForm(FlaskForm):
    prenume = StringField('prenume', validators=[InputRequired(message='Trebuie introdus un prenume!')])
    nume = StringField('nume', validators=[InputRequired(message='Trebuie introdus un nume!')])


@app.route('/clienti', methods=['GET'])
def clienti():
    return render_template(
        'clienti.jinja2',
        users=Client.query.all(),
        title="Clienti"
    )

@app.route('/clienti/aduga', methods=['POST', 'GET'])
def clienti_adauga():
    form = AdaugaClientForm()

    if form.validate_on_submit():
        client_nou = Client(prenume=form.prenume.data, nume=form.nume.data, )
        return redirect(url_for('clienti'))

    return render_template('clientiform.jinja2', form=form)