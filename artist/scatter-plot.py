import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, x_head='', y_head='', title=None, xlabel=None, ylabel=None):
    plt.scatter(x_values, y_values)
    plt.xlabel(xlabel or x_head)
    plt.ylabel(ylabel or y_head)
    plt.title(title or f"{y_head} vs. {x_head}")
    plt.show()

# Take user input for x and y values
x_values = list(map(float, input("Enter x values separated by commas: ").split(',')))
y_values = list(map(float, input("Enter y values separated by commas: ").split(',')))
x_head = input("Enter x axis label: ")
y_head = input("Enter y axis label: ")
title = input("Enter title for the scatter plot (press Enter for default title): ")
xlabel = input("Enter label for x axis (press Enter for default label): ")
ylabel = input("Enter label for y axis (press Enter for default label): ")

create_scatter_plot(x_values, y_values, x_head, y_head, title, xlabel, ylabel)
