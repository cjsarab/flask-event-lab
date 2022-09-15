from flask import render_template, request
from app import app
from models.event_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Events', sub_title='All events', events='Events')