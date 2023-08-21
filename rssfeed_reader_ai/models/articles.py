from db import db
import datetime

class Article(db.Model):
    # define articles table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=True)
    guid = db.Column(db.String(255), nullable=False)
    unread = db.Column(db.Boolean, default=True, nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
    source = db.relationship('Source', db.backref('articles', lazy=True))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_published = db.Column(db.DateTime)
    # make sure there is no duplicate source_id + guid pair in the table
    __table_args__ = (
        db.UniqueConstraint('source_id', 'guid', name='uc_source_guid'),
    )