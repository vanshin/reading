#codingutf-8
from . import main
from flask import render_template
from .forms import readingForm
from ..models import Reading,Sentence
from .. import db

@main.route('/')
def index():
    readings = Reading.query.order_by(Reading.order_name).all()
    order_list = set()
    
    for reading in readings:
        order_list.add(reading.order_name)
        
    return render_template('index.html',order_list=order_list,readings=readings)

@main.route('/input',methods=['GET','POST'])
def input():
    form = readingForm()
    if form.validate_on_submit():
        order_name = form.order_name.data
        reading_name = form.reading_name.data
        reading_body = form.reading_body.data
        sentences_list = reading_body.split('.')
        reading = Reading(order_name=order_name,reading_name=reading_name)
        db.session.add(reading)
        db.session.commit()
        print reading.id
        reading_id = reading.id
        # db.session.add(reading)
        for sentence_body in sentences_list:
            sentence = Sentence(reading_id=reading_id,sentence_body=sentence_body)
            db.session.add(sentence)
        db.session.add(reading)
    return render_template('input.html',form=form)

@app.route('/getReading/<id>',methods=['GET','POST'])
def getReading(id):
    reading = Reading.query.filter_by(id=id).first()
    reading.sentences
    return jsonify