from threading import Thread
from persistance.models import Project

class Task(Thread):
    """
    Represents a multithreaded task, operated on a project
    """

    _project: Project = None

    def __init__(self, project):
        Thread.__init__(self)
        self._project = project


    def get_project(self) -> Project:
        return self._project
