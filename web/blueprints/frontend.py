from flask import Blueprint, render_template

from web.controllers.project_controller import get_projects

frontend_bp = Blueprint('frontend_bp', __name__)


@frontend_bp.route('/projects')
def home():
    return render_template('projects.html', projects=get_projects())

@frontend_bp.route('/')
def root():
    return render_template("index.html")

