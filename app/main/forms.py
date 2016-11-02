from flask_wtf import Form
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Required,Length

class readingForm(Form):
    order_name = StringField('序列',validators=[Required()])
    reading_name = StringField('标题',validators=[Required()])
    reading_body = TextAreaField('阅读理解')
    submit = SubmitField('提交')