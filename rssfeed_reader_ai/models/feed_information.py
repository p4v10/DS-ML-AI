from db import db
import datetime

# Class for the Feed Information Table
class FeedInformation(db.Model):
    # define the source table columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    rss_feed = db.Column(db.Text, nullable=False)
    # when the source is created, this will tell us what date time
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
