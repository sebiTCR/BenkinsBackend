from threading import Thread
from queue import Queue
from core.fs import log
import time

from core.scheduler.task import Task


class Scheduler():
    queue = Queue()
    poll_time = 5
    _worker_thread: Thread = None

    def __init__(self):
        log.info("Starting Job scheduler...")
        self._worker_thread = Thread(target=self._worker, daemon=True)
        self._worker_thread.start()


    def register_task(self, task: Task):
        self.queue.put(task)


    def _worker(self):
        log.debug("Starting worker...")
        while True:
            job = self.queue.get()
            job.start()
            self.queue.task_done()
            time.sleep(self.poll_time)


scheduler: Scheduler = Scheduler()
