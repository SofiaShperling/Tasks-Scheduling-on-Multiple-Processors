from Job import Job


class Machine:
    def __init__(self, id: int):
        self.id = id
        self.work_time = 0
        self.jobs = []
        self.jobs_id = []

    def assign_job(self, job: Job):
        if job.machine is None:
            self.jobs.append(job)
            self.jobs_id.append(job.id)
            self.work_time += job.time
            job.machine = self
        return 0

    def show_schedule(self):
        return f'Machine({repr(self.id)}, working time: {repr(self.work_time)}, assigned jobs: {repr(self.jobs)})'

    def __repr__(self) -> str:
        return f'Machine({repr(self.id)}, working time: {repr(self.work_time)})'

    def __str__(self) -> str:
        return f'Machine({repr(self.id)}, working time: {repr(self.work_time)})'
