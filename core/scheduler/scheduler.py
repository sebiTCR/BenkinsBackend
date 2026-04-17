import os
from threading import Thread
from queue import Queue
from core.fs import log
import time

from core.scheduler.task import Task


class Scheduler():
    """
    Schedules tasks to be run in parallel.
    **It should never call outside functions** but be called from outside!
    """

    queue = Queue()
    poll_time = 5
    _worker_thread: Thread = None
    _periodic_tasks: list[object] = []

    def __init__(self):
        log.info("Starting Job scheduler...")
        self._worker_thread = Thread(target=self._worker, daemon=True)
        self._worker_thread.start()


    def register_task(self, task: Task):
        self.queue.put(task)


    def register_independent_task(self, method):
        """
        Runs a method in parallel, without depending on a queue. Perfect for periodic tasks.
        :param method: Function to be run
        """
        th = Thread(target=method, daemon=True)
        self._periodic_tasks.append(th)
        th.start()


    def _worker(self):
        log.debug("Starting worker...")
        while True:
            job = self.queue.get()
            job.start()
            self.queue.task_done()
            time.sleep(self.poll_time)


scheduler: Scheduler = Scheduler()
