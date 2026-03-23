from flask import request
from sqlalchemy import select, delete, update
from persistance.database import db
from persistance.models import Project, BuildStatus


def get_project(id):
    data = db.session.get(Project, id)
    if data == None:
        return None

    return {
        "id": data.id,
        "name": data.name,
        "version": data.version,
        "status": data.status
    }


def get_project_by_name(name: str):
    q = select(Project).where(Project.name == name)
    data = db.session.execute(q).first()

    if data is None:
        return None

    return {
        "id": data.id,
        "name": data.name,
        "version": data.version,
        "status": data.status
    }


def project_exists(name: str):
    q = select(Project).where(Project.name == name)
    data = db.session.execute(q).first()

    if data is None:
        return False
    return True


def create_project(data: dict):
    proj = Project()
    if  project_exists(data["name"]):
        return {"status": False, "message": "Project exists!"}

    proj.name = data["name"]
    proj.status = 0
    proj.version = data["version"]

    db.session.add(proj)
    db.session.commit()
    return {"status": True}


def  update_project_param(param, id, val):
    return "Unimplemented"


def set_project_build_status(id: int, status_code: int):
    q = update(Project).where(Project.id == id).values(status=status_code)
    db.session.execute(q)
    db.session.commit()
    return f"updated Project {id}"


def delete_project(id: int):
    q = delete(Project).where(Project.id == id)
    db.session.execute(q)
    db.session.commit()
    return f"deleted {id}"