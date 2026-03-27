import os
from dataclasses import asdict

from flask import request
from sqlalchemy import select, delete, update
from persistance.database import db
from persistance.models import Project, BuildStatus


def get_projects():
    data = []

    for entry in db.session.query(Project).all():
        data.append(asdict(entry))

    return data


def get_project(id):
    data: Project = db.session.get(Project, id)
    if data is None:
        return None

    return data


def get_project_by_name(name: str):
    q = select(Project).where(Project.name == name)
    data = db.session.execute(q).first()

    if data is None:
        return None

    return data


def project_exists(name: str):
    q = select(Project).where(Project.name == name)
    data = db.session.execute(q).first()

    if data is None:
        return False
    return True


def create_project(data: dict):
    if  project_exists(data["name"]):
        return {"status": False, "message": "Project exists!"}

    project_path = os.getenv("REPO_PATH")
    proj = Project(name=data["name"], version=data["version"], status=0, path=project_path)

    db.session.add(proj)
    db.session.commit()
    return {"status": True}


def  update_project_param(param, id, val):
    return "Unimplemented"


def set_project_build_status(id: int, status_code: int):
    """
    Updates the build status of a project
    :param id: Project ID
    :param status_code: Build Code (NONE=0, SUCCESS=1, BUILDING=2, FAILED=3)
    :return:
    """
    q = update(Project).where(Project.id == id).values(status=status_code)
    db.session.execute(q)
    db.session.commit()
    return f"updated Project {id}"


def delete_project(id: int):
    q = delete(Project).where(Project.id == id)
    db.session.execute(q)
    db.session.commit()
    return f"deleted {id}"