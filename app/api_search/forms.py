from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class ApiSearchForm(Form):
    search_bar = StringField('Type your search below...')
    submit = SubmitField('Go!')
