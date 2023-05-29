from dataExport import data_export_times, data_export_conflicts

from Job import Job
from Machine import Machine


def find_job(jobs, id: int):

    for job in jobs:
        if job.id == id:
            return job

    return None


def check_conflicts(jobs, machines):

    conflict_flag = 0

    for job in jobs:
        for conflict in job.conflicts:
            count = 0
            for par_job in machines[job.machine.id].jobs_id:
                if par_job in conflict:
                    count += 1
            if count == len(conflict):
                conflict_flag = 1

    return conflict_flag


def get_jobs_total_time(jobs):
    total_time = 0

    for i in range(len(jobs)):
        total_time += jobs[i].time

    return total_time


def get_ready_data(instance_number: int):
    if instance_number == 1 or instance_number == 2 or instance_number == 3:
        jobs_set = data_export_times(f'data/times{instance_number}.txt')
        conflicted_sets = data_export_conflicts(f'data/conflicts{instance_number}.txt')
    else:
        print('Unavailable instances!')
        return None

    jobs = []

    for i in range(len(jobs_set)):
        job = Job(id=i, time=jobs_set[i])
        job.set_conflicts(conflicted_sets)
        jobs.append(job)

    machines = []
    for i in range(2):
        machine = Machine(i)
        machines.append(machine)

    return jobs, machines, conflicted_sets



