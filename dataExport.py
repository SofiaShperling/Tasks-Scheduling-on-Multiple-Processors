

def data_export_times(path: str):

    f = open(path, 'r')

    jobs = f.read().splitlines()

    f.close()

    for i in range(len(jobs)):
        jobs[i] = int(jobs[i])

    return jobs


def data_export_conflicts(path: str):

    f = open(path, 'r')

    conflicts = f.read().splitlines()

    f.close()

    conflicted_sets = []

    for i in range(len(conflicts)):
        conf_jobs = (conflicts[i].split(' '))
        if '' in conf_jobs:
            conf_jobs.remove('')
        for j in range(len(conf_jobs)):
            conf_jobs[j] = int(conf_jobs[j])
        conflicted_sets.append(conf_jobs)

    return conflicted_sets
