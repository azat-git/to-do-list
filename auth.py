from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import functools
import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    # Registration logic here
    pass

@bp.route('/login', methods=('GET', 'POST'))
def login():
    # Login logic here
    pass

@bp.route('/logout')
def logout():
    # Logout logic here
    pass

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
