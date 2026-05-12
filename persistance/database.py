import os

from sqlalchemy import *
from sqlalchemy.orm import Session

from persistance.models import Base


from dotenv import load_dotenv
from alembic.config import Config
from alembic import command

load_dotenv()

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

class Database:
    engine = None
    session = None

    def __init__(self):
        db_url = os.getenv("DB_URL")
        if not db_url:
             raise ValueError("DB_URL environment variable is not set")
        self.engine = create_engine(db_url)
        self.session = Session(self.engine)
        # Base.metadata.create_all(self.engine)  # Use migrations instead: alembic upgrade head

db = Database()