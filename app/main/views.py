from . import main
from flask import render_template
from .forms import readingForm


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/input')
def input():
    form = readingForm()
    if form.validate_on_submit():
        print('111')
    return render_template('input.html',form=form)