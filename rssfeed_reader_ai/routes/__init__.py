from flask import redirect, request, abort
from app import app
from models.articles_summary import ArticlesSummary
from models.feed_information import FeedInformation

# create a index route
@app.route('/', methods=['GET'])
def get_index():
    return abort(501)

@app.route('/read/<article_id>', methods=['GET'])
def get_read_article(article_id):
    return abort(501)

@app.route('/sources', methods=['GET'])
def get_sources():
    return abort(501)

@app.route('sources', methods=['POST'])
def post_sources():
    return abort(501)
