import math
import time

from flask_006 import db
from flask_006.models import Post


def get_posts():
    posts = Post.query.all()
    if posts:
        return posts
    return []


def database_add_post(title, content):
    pub_date = math.floor(time.time())
    post = Post()
    post.title = title
    post.content = content
    post.pub_date = pub_date
    db.session.add(post)
    db.session.commit()
    return True


def get_post_content(post_id):
    post = Post.query.get(post_id)
    if post:
        return [post.title, post.content]
    return False, False
