import pandas as pd
import matplotlib.pyplot as plt


def modeler2D(filename, x_column, y_column):
    # Read file
    df = pd.read_excel(filename)

    # convert column data to lists
    xRaw = df[x_column]
    x = list(xRaw)
    yRaw = df[y_column]
    y = list(yRaw)

    # Plotting
    plt.scatter(x, y, color='blue', marker='*', s=15)

    # ***BOUNDS***
    # plt.xlim([.8e10, 1.2e10])
    # plt.ylim([-1, 4])

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f' {y_column} vs. {x_column}')

    # ***INVERT AXES***
    # plt.gca().invert_xaxis()
    # plt.gca().invert_yaxis()

    plt.show()


modeler2D('summary2.xlsx', 'age (years)', 'Central hydrogen mass fraction [Xc]')
