from flask import Flask, url_for
from blueprints.project import project_bp
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()

app.register_blueprint(project_bp,  url_prefix="/project")

@app.route('/')
def root():
    return "Benkins!"