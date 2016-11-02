from . import main
from flask import render_template
from .forms import readingForm
from ..models import Reading,Sentence,Word
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/input')
def input():
    form = readingForm()
    if form.validate_on_submit():
        order_name = form.order_name
        reading_name = form.reading_name
        reading_body = form.reading_body
        sentences_list = reading_body.split('.')
        reading = Reading(order_name=order_name,reading_name=reading_name)
        reading_id = reading.id
        db.session.add(reading)
        for sentence_body in sentences_list:
            sentence = (reading_id=reading_id,sentence_body=sentence_body)
            db.session.add(sentence)
    return render_template('input.html',form=form)