import copy
import random
import time

import numpy as np

from common import get_ready_data, get_jobs_total_time
from setSchedule import set_schedule_fix, set_schedule_lb

from plotVisualization import draw_plot


def swap(permutation, a: int, b: int):

    permutation[a], permutation[b] = permutation[b], permutation[a]

    return permutation


def local_search(jobs, machines, decoding_function: int):
    if decoding_function != 1 and decoding_function != 2:
        print('Unavailable decoding procedure!')

    total_time = get_jobs_total_time(jobs)

    population = []

    initial_permutation = []
    for i in range(len(jobs)):
        initial_permutation.append(i)

    for i in range(10):
        random.shuffle(initial_permutation)
        population.append(initial_permutation)

    record_permutation = initial_permutation
    if decoding_function == 1:
        record_object_value = set_schedule_lb(copy.deepcopy(jobs), copy.deepcopy(machines), record_permutation)
    else:
        record_object_value = set_schedule_fix(copy.deepcopy(jobs), copy.deepcopy(machines), record_permutation)

    while record_object_value > total_time:
        random.shuffle(initial_permutation)
        if decoding_function == 1:
            record_object_value = set_schedule_lb(copy.deepcopy(jobs), copy.deepcopy(machines), record_permutation)
        else:
            record_object_value = set_schedule_fix(copy.deepcopy(jobs), copy.deepcopy(machines), record_permutation)

    plot_data = []
    plot_data_obj_func = []

    for k in range(10):
        stop = False

        best_permutation = population[k]

        if decoding_function == 1:
            best_object_value = set_schedule_lb(copy.deepcopy(jobs), copy.deepcopy(machines), best_permutation)
        else:
            best_object_value = set_schedule_fix(copy.deepcopy(jobs), copy.deepcopy(machines), best_permutation)

        plot_data.append(best_object_value)
        if best_object_value > total_time:
            plot_data_obj_func.append(best_object_value - total_time)
        else:
            plot_data_obj_func.append(best_object_value)

        while not stop:
            stop = True

            for i in range(10):

                a = np.random.randint(0, len(jobs))
                b = np.random.randint(0, len(jobs))
                while a == b:
                    a = np.random.randint(0, len(jobs))
                    b = np.random.randint(0, len(jobs))

                current_permutation = swap(copy.deepcopy(best_permutation), a, b)

                if decoding_function == 1:
                    object_value = set_schedule_lb(copy.deepcopy(jobs), copy.deepcopy(machines), current_permutation)
                else:
                    object_value = set_schedule_fix(copy.deepcopy(jobs), copy.deepcopy(machines), current_permutation)

                plot_data.append(object_value)
                if object_value > total_time:
                    plot_data_obj_func.append(object_value - total_time)
                else:
                    plot_data_obj_func.append(object_value)

                if object_value < best_object_value:
                    stop = False
                    best_object_value = object_value
                    best_permutation = current_permutation

        if best_object_value < record_object_value:
            record_object_value = best_object_value
            record_permutation = best_permutation

    if decoding_function == 1:
        print('Found solution with objective function equals to',
              set_schedule_lb(jobs, machines, record_permutation))
    else:
        print('Found solution with objective function equals to',
              set_schedule_fix(jobs, machines, record_permutation))

    return plot_data, plot_data_obj_func


def show_local_search_solution(instance_number: int, decoding_function: int):

    jobs, machines, conflicted_sets = get_ready_data(instance_number)

    stat_time = time.time()
    plot_data_with_penalty, plot_data_without_penalty = local_search(jobs, machines, decoding_function)
    print("Algorithm works for ", time.time() - stat_time, " seconds")

    print('________________')
    for machine in machines:
        print(machine.show_schedule())

    draw_plot(plot_data_with_penalty, plot_data_without_penalty)

    return 0
