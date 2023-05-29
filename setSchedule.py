import copy
from common import find_job, check_conflicts, get_jobs_total_time


def set_schedule_fix(jobs, machines, jobs_order):

    for job_order in jobs_order:
        machines[0].assign_job(jobs[job_order])
        i = 0
        while i < len(jobs[job_order].conflicts):
            conflict = copy.deepcopy(jobs[job_order].conflicts[i])

            count_conflict = 0
            for j in range(len(machines[0].jobs_id)):
                if machines[0].jobs_id[j] in conflict:
                    count_conflict += 1

            if count_conflict + 1 == len(conflict):
                for j in range(len(machines[0].jobs_id)):
                    if machines[0].jobs_id[j] in conflict:
                       conflict.remove(machines[0].jobs_id[j])

                conflicted_job = find_job(jobs, conflict[0])
                machines[1].assign_job(conflicted_job)
            i += 1

    error = check_conflicts(jobs, machines)

    return abs(machines[0].work_time - machines[1].work_time) + error * (machines[0].work_time + machines[1].work_time)


def set_schedule_lb(jobs, machines, jobs_order):

    total_time = get_jobs_total_time(jobs)

    lb = max(max([job.time for job in jobs]), total_time / 2)

    j = 0
    while machines[0].work_time < lb:
        machines[0].assign_job(jobs[jobs_order[j]])
        j += 1

    while j < len(jobs):
        machines[1].assign_job(jobs[jobs_order[j]])
        j += 1

    error = check_conflicts(jobs, machines)

    return abs(machines[0].work_time - machines[1].work_time) + error * (machines[0].work_time + machines[1].work_time)
