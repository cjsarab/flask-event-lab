import datetime
from models.event import *

event1 = Event(datetime.date(2022, 11, 9), "Birthday Party", 8, "Garden", "Birthday party for the kids")
event2 = Event(datetime.date(2022, 9, 15), "Mini Golf", 10, "Jungle Rumble", "Thursday social event")
event3 = Event(datetime.date(2022, 4, 12), "Football", 12500, "Tannadice Park", "Dundee United vs Dundee")

events = [event1, event2, event3]
