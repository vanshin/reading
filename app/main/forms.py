from flask_wtf import Form
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Required,Length

class readingForm(Form):
    title = StringField('标题',validators=[Required()])
    reading = TextAreaField('阅读理解')
    submit = SubmitField('提交')