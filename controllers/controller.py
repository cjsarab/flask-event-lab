from flask import render_template, request
from app import app
from models.event_list import events, add_new_event
from models.event import Event


@app.route('/events')
def index():
    return render_template('index.html', title='Events', sub_title='All events', events=events)

@app.route('/events/<index>')
def event(index):
    event = events[int(index)]
    return render_template('event.html', event=event)

@app.route('/events', methods = ['POST'])
def add_event():
    event_title = request.form['title']
    event_description = request.form['description']
    event_date = request.form['date']
    event_guests = request.form['guests']
    event_location = request.form['location']
    new_event = Event(event_date, event_title, event_guests, event_location, event_description)
    
    add_new_event(new_event)
    return render_template('index.html', title='Events', events=events)