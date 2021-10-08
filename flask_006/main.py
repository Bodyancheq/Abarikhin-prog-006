from flask import Blueprint, render_template, request, flash, abort
from flask_login import login_required, current_user

from flask_006.services import get_posts, get_post_content, database_add_post

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('index.html',
                           posts=get_posts())


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/add_post', methods=["GET", "POST"])
@login_required
def add_post():
    if request.method == "POST":
        name = request.form["name"]
        post_content = request.form["post"]
        if len(name) > 5 and len(post_content) > 10:
            res = database_add_post(name, post_content)
            if not res:
                flash('Post were not added. Unexpected error', category='error')
            else:
                flash('Success!', category='success')
        else:
            flash('Post name or content too small', category='error')

    return render_template('add_post.html')


@main.route('/post/<int:post_id>')
def post_content(post_id):
    title, content = get_post_content(post_id)
    if not title:
        abort(404)
    return render_template('post.html', title=title, content=content)


@main.errorhandler(404)
def page_not_found(error):
    return "<h1>Ooooops! This post does not exist!</h1>"
