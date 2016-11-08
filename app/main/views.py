#codingutf-8
from . import main
from flask import render_template,jsonify
from .forms import readingForm
from ..models import Reading,Sentence
from .. import db

@main.route('/')
def index():
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
        sentences_list = reading_body.split('.')
        reading = Reading(reading_order=reading_order,reading_name=reading_name,reading_body=reading_body)
        db.session.add(reading)
        db.session.commit()
        reading_id = reading.id
        for sentence_body in sentences_list:
            sentence = Sentence(reading_id=reading_id,sentence_body=sentence_body)
            db.session.add(sentence)
    return render_template('input.html',form=form)

@main.route('/reading/<id>',methods=['GET','POST'])
def reading(id):
    reading = Reading.query.filter_by(id=id).first().to_ison()
    return jsonify(reading) 