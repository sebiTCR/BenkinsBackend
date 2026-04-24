from sqlalchemy import select

from persistance.database import db
from persistance.models import Build, Log


def create_log(build: Build, contents: str):
    log = Log(build_id=build.id, contents=contents)
    db.session.add(log)
    db.session.commit()


def get_logs(build: Build):
    data = db.session.query(Log).filter(Log.build_id == build.id).all()
    return data