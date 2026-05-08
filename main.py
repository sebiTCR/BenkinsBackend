import os
from flask import Flask, url_for, render_template
from flask_cors import CORS
from jinjax import jinjax, Catalog

from web.blueprints.project import project_bp
from dotenv import load_dotenv
from web.blueprints.frontend import frontend_bp
from web.blueprints.build import build_bp
import web.components.renderer as renderer
from web.controllers import project_controller

app = Flask(__name__, template_folder='./web/templates', static_folder='./web/static')
CORS(app, resources={r"/project/*": {"origins": ["http://localhost:3000", "http://localhost:5000"]}})
# app.register_blueprint(frontend_bp)
load_dotenv()

app.register_blueprint(project_bp,  url_prefix="/project")
app.register_blueprint(build_bp, url_prefix="/build")
app.register_blueprint(frontend_bp, url_prefix="/app")

if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    project_controller.initialize()

@app.route('/')
def root():
    print(renderer.catalog)
    return renderer.catalog.render("home")


if __name__ == "__main__":
    renderer.catalog = Catalog(jinja_env=app.jinja_env)
    renderer.catalog.add_folder("./web/components")
    app.run(host="0.0.0.0", port=5000, debug=True)
