#codingutf-8
from flask import render_template, jsonify,request
from . import main
from .forms import readingForm,controlForm
from ..models import Reading, Sentence
from .. import db

@main.route('/')
def index():
    """ empty """
    readings = Reading.query.order_by(Reading.reading_order).all()
    order_list = set()
    for reading in readings:
        order_list.add(reading.reading_order)
        
    return render_template('index.html',order_list=order_list,readings=readings)

@main.route('/input',methods=['GET','POST'])
def input():
    form = readingForm()
    if form.validate_on_submit():
        reading_order = form.reading_order.data
        reading_name = form.reading_name.data
        reading_body = form.reading_body.data
        sentences_list_tmp = reading_body.split('.')
        sentences_list = list()
        for sentence in sentences_list_tmp:
            sentence = sentence.replace('\r\n', '').lstrip()
            sentences_list.append(sentence)
        reading = Reading(reading_order=reading_order,reading_name=reading_name,reading_body=reading_body)
        db.session.add(reading)
        db.session.commit()
        reading_id = reading.id
        for sentence_body in sentences_list:
            sentence = Sentence(reading_id=reading_id,sentence_body=sentence_body)
            db.session.add(sentence)
    return render_template('input.html',form=form)

@main.route('/reading/<int:id>', methods=['GET'])
def reading(id):
    reading = Reading.query.filter_by(id=id).first().to_json()
    return jsonify(reading) 

@main.route('/sentence/<int:id>', methods=['GET'])
def sentence(id):
    sentence = Sentence.query.filter_by(id=id).first().to_json()
    return jsonify(sentence)

@main.route('/sentence/notes',methods=['POST'])
def notes():
   note = request.json
    