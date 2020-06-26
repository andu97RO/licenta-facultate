from datetime import datetime as dt

from flask import current_app as app
from flask import redirect, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField
from wtforms.validators import InputRequired

from .models import Client, Abonament, IP, db

from flask_bootstrap import Bootstrap

import json

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
    nume = StringField('VitezaMin', validators=[InputRequired(
        message='Trebuie introudsa o viteza min (in kbps)!')])
    prenume = StringField('VitezaMax', validators=[
                          InputRequired(message='Trebuie introdusa o viteza maxima (in kbps)!')])
    activ = RadioField('Activeaza')


@app.route('/clienti/<int:page>', methods=['GET'])
def clienti(page=1):
    per_page = 4
    clienti = Client.query.paginate(page, per_page, error_out=False)

    return render_template(
        'clienti.html',
        clienti=clienti,
        title="Clienti",
    )


@app.route('/ip/<int:page>', methods=['GET'])
def ip(page=1):
    per_page = 4
    ipuri = IP.query.paginate(page, per_page, error_out=False)

    return render_template(
        'ip.html',
        ip=ipuri,
        title="IP",
    )


@app.route('/abonament/<int:page>', methods=['GET'])
def abonament(page=1):
    per_page = 4
    abonamente = Abonament.query.paginate(page, per_page, error_out=False)

    return render_template(
        'abonament.html',
        abonament=abonamente,
        title="Abonamente",
    )


@app.route('/clienti/modifica/<id_client>', methods=['POST', 'GET'])
def clienti_modifica(id_client):
    form = AdaugaClientForm()

    client = Client.query.get(id_client)

    if form.validate_on_submit():

        update_dict = {"prenume": form.prenume.data, "nume": form.nume.data,
                       "localitate": form.localitate.data,
                       "adresa": form.adresa.data, "telefon": form.telefon.data,
                       "abonament": form.abonament.data}

        db.session.query(Client).filter(
            Client.id == id_client).update(update_dict)
        db.session.commit()
        return redirect(url_for('clienti_arata', id_client=id_client))

    return render_template('clientiedit.html', id_client=id_client, form=form,
                           client=client)


@app.route('/abonament/modifica/<id_abonament>', methods=['POST', 'GET'])
def abonament_modifica(id_abonament):
    form = AdaugaAbonamentForm()

    abonament = Abonament.query.get(id_abonament)

    if form.validate_on_submit():

        update_dict = {"valoare": form.valoare.data, "vitezamin": form.vitezamin.data,
                       "vitezamax": form.vitezamax.data}

        db.session.query(Abonament).filter(
            Abonament.id == id_abonament).update(update_dict)
        db.session.commit()
        return redirect(url_for('abonament_arata', id_abonament=id_abonament))

    return render_template('abonamentedit.html', id_abonament=id_abonament, form=form,
                           abonament=abonament)


@app.route('/clienti/arata/<id_client>', methods=['GET'])
def clienti_arata(id_client):

    client = Client.query.get(id_client)
    print(client)
    return render_template('clientishow.html', client=client,
                           title="Arata client")


@app.route('/abonament/arata/<id_abonament>', methods=['GET'])
def abonament_arata(id_abonament):

    abonament = Abonament.query.get(id_abonament)
    return render_template('abonamentshow.html', abonament=abonament,
                           title="Arata abonament")


@app.route('/clienti/sterge/<id_client>', methods=['GET'])
def clienti_sterge(id_client):
    Client.query.filter(Client.id == id_client).delete()
    db.session.commit()

    return json.dumps({'success': True}), 200,
    {'ContentType': 'application/json'}


@app.route('/abonament/sterge/<id_abonament>', methods=['GET'])
def abonament_sterge(id_abonament):
    Abonament.query.filter(Abonament.id == id_abonament).delete()
    db.session.commit()

    return json.dumps({'success': True}), 200,
    {'ContentType': 'application/json'}


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
                            abonament=form.abonament.data)
        db.session.add(client_nou)
        db.session.commit()
        return redirect(url_for('clienti', page=1))

    return render_template('clientiform.html', form=form)


@app.route('/ip/adauga', methods=['POST', 'GET'])
def ip_adauga():
    form = AdaugaClientForm()

    if form.validate_on_submit():
        ip_nou = Client(adresa_ip=form.adresa_ip.data,
                        nume=form.nume.data,
                        prenume=form.prenume.data,
                        activ=form.activ.data)
        db.session.add(ip_nou)
        db.session.commit()
        return redirect(url_for('ip', page=1))

    return render_template('ipform.html', form=form)


@app.route('/abonament/adauga', methods=['POST', 'GET'])
def abonament_adauga():
    form = AdaugaAbonamentForm()

    if form.validate_on_submit():
        abonament_nou = Abonament(valoare=form.valoare.data,
                                  vitezamin=form.vitezamin.data,
                                  vitezamax=form.vitezamax.data)
        db.session.add(abonament_nou)
        db.session.commit()
        return redirect(url_for('abonament', page=1))

    return render_template('abonamentform.html', form=form)


@app.route('/regula/adauga/<int:client_id>')
def regula_adauga(client_id):
    client = Client.query.filter(Client.id == client_id).first()
    abonament = Abonament.query.filter(
        Abonament.valoare == client.abonament).first()

    # $downmax = $line5['value'];
    # $upmax = floor($downmax / 2);

    # // upload eno1
    # $filename = '/etc/sysconfig/htb/eno1-2:'.($line["id"]+1);
    # $continut = "RATE=".$line4['value']."kbit\nCEIL=".($upmax)."kbit\nMARK=".($line['id']+1)."\nPRIO=5\n";

    # // download eno2
    # $filename2 = '/etc/sysconfig/htb/eno2-2:'.($line["id"]+1);
    # $continut2 = "RATE=".$line4['value']."kbit\nCEIL=".$downmax."kbit\nPRIO=5\n";
