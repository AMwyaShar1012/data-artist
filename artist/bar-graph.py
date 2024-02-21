import matplotlib.pyplot as plt

def create_bar_graph(x_values, y_values, x_head='', y_head='', title=None, xlabel=None, ylabel=None):
    plt.bar(x_values, y_values)
    plt.xlabel(xlabel or x_head)
    plt.ylabel(ylabel or y_head)
    plt.title(title or f"{y_head} vs. {x_head}")
    plt.show()

x_values = input("Enter x values separated by commas: ").split(',')
y_values = [int(val) for val in input("Enter y values separated by commas: ").split(',')]
x_head = input("Enter x axis label: ")
y_head = input("Enter y axis label: ")
title = input("Enter title for the graph (press Enter for default title): ")
xlabel = input("Enter label for x axis (press Enter for default label): ")
ylabel = input("Enter label for y axis (press Enter for default label): ")

create_bar_graph(x_values, y_values, x_head, y_head, title, xlabel, ylabel)
