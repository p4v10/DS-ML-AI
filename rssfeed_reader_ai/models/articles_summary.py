from db import db
import datetime

class ArticlesSummary(db.Model):
    # define articles table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=True)
    guid = db.Column(db.String(255), nullable=False)
    unread = db.Column(db.Boolean, default=True, nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('feed_information.id'), nullable=False)
    source = db.relationship('FeedInfo', backref=db.backref('articles', lazy=True))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_published = db.Column(db.DateTime)
    # make sure there is no duplicate source_id + guid pair in the table
    __table_args__ = (
        db.UniqueConstraint('source_id', 'guid', name='uc_source_guid'),
    )
    
    # add a decorator for a method that belong to a class FeedInformation
    @classmethod

    def insert_from_feed(cls, source_id, feed_articles):
        # insert all articles into a table
        statement = ArticlesSummary.__table__.insert().prefix_with('IGNORE')

        articles = []

        for article in feed_articles:
            # append attributes to the articles list
            articles.append({
                'title': article['title'],
                'summary': article['summary'],
                'link': article['link'],
                'author': article['author'],
                'date_published': article['published'],
                'guid': article['id'],
                'source_id': source_id,
            })
        
        # insert the articles into the db
        db.engine.execute(statement, articles)