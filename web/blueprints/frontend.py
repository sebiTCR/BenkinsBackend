from flask import Blueprint, render_template

import web.components.renderer as renderer
from web.controllers.project_controller import get_projects

frontend_bp = Blueprint('frontend_bp', __name__)


@frontend_bp.route('/projects')
def home():
    return renderer.catalog.render('project.base', projects=get_projects())

@frontend_bp.route('/')
def root():
    return renderer.render_component("home", renderer=renderer)

