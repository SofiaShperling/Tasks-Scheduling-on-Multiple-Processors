from ortools.linear_solver import pywraplp

from common import get_ready_data


def solver_approach(jobs, machines, conflicts):
    n = len(jobs)
    m = len(machines)
    k = len(conflicts)

    time_limit = 240000

    # [START solver]
    # Create solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    # [END solver]
    solver.SetTimeLimit(time_limit)

    # [START variables]
    p = list(map(lambda i: i.time, jobs))
    y = [[0 for j in range(n)] for l in range(k)]
    for l in range(k):
        for j in range(n):
            if jobs[j].id in conflicts[l]:
                y[l][j] = 1

    x = [[solver.BoolVar('x') for j in range(n)] for i in range(m)]

    c = solver.NumVar(0, solver.infinity(), 'c')

    print('Number of variables =', solver.NumVariables())
    # [END variables]

    # [START constraints]

    solver.Add(sum((p[j]*x[0][j]) for j in range(n)) - sum((p[j]*x[1][j]) for j in range(n)) <= c)
    solver.Add(sum((p[j] * x[1][j]) for j in range(n)) - sum((p[j] * x[0][j]) for j in range(n)) <= c)

    for j in range(n):
        solver.Add(sum(x[i][j] for i in range(m)) <= 1)
        solver.Add(sum(x[i][j] for i in range(m)) >= 1)

    for i in range(m):
        for l in range(k):
            solver.Add(sum(y[l][j]*x[i][j] for j in range(n)) + 1 <= sum(y[l][j] for j in range(n)))

    solver.Add(sum(x[i][j] for j in range(n) for i in range(m)) <= n)
    solver.Add(sum(x[i][j] for j in range(n) for i in range(m)) >= n)

    print('Number of constraints =', solver.NumConstraints())
    # [END constraints]

    # [START objective]
    solver.Minimize(c)
    # [END objective]

    # [START solve]
    status = solver.Solve()
    # [END solve]

    # [START print_solution]
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')
    # [END print_solution]
    print('Solution:', solver.Objective().Value())
    # [START advanced]
    print('\nAdvanced information:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem have a bound', solver.Objective().BestBound())
    # [END advanced]

    rez_x = [[x[i][j].solution_value() for j in range(n)] for i in range(m)]

    return rez_x


def show_solver_solution(instance_number: int):

    jobs, machines, conflicted_sets = get_ready_data(instance_number)

    x = solver_approach(jobs, machines, conflicted_sets)

    for i in range(len(machines)):
        for j in range(len(jobs)):
            if x[i][j] == 1:
                machines[i].assign_job(jobs[j])
    print('________________')
    for machine in machines:
        print(machine.show_schedule())

    return 0


