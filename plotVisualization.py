import matplotlib.pyplot as plt


def draw_plot(obj_with_penalty, obj_without_penalty):
    fig, ax = plt.subplots()
    fig.set_size_inches(16, 10)
    ax.plot(obj_with_penalty, linestyle = ':', color = 'black', label = 'objective function with the penalty')
    ax.plot(obj_without_penalty, color = 'blue',  label = 'objective function')
    plt.xlabel('number of iteration', fontsize=20)
    plt.ylabel('value of the function', fontsize=20)

    ax.grid()
    plt.legend(loc='best', frameon=False, prop={'size': 20})

    fig.show()
    fig.savefig("Plot_LocalSearch.png")

    return fig, ax