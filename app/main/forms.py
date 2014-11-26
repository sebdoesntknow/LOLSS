from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class WillThisEverWork(Form):
    wdyt = StringField('Do you think so?', validators=[Required()])
    submit = SubmitField('Magic happens!')

