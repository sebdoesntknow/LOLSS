from flask import render_template
from . import api_search
from .forms import ApiSearchForm
from ..tools.riot_api_tools import query_riot_api as qa

@api_search.route('/api_search', methods=['GET', 'POST'])
def index():
    form = ApiSearchForm()
    if form.validate_on_submit():
        api_response = qa(form.search_bar.data)
        streams = api_response['streams']
        return render_template('api_search/api_search.html',
                               form=form,
                               search_results=streams)
    return render_template('api_search/api_search.html', form=form)
