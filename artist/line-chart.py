import matplotlib.pyplot as plt

def create_line_chart(x_values, y_values, x_head='', y_head='', title=None, xlabel=None, ylabel=None):
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel(xlabel or x_head)
    plt.ylabel(ylabel or y_head)
    plt.title(title or f"{y_head} vs. {x_head}")
    plt.show()

# Take user input for x and y values
x_values = list(map(float, input("Enter x values separated by commas: ").split(',')))
y_values = list(map(float, input("Enter y values separated by commas: ").split(',')))
x_head = input("Enter x axis label: ")
y_head = input("Enter y axis label: ")
title = input("Enter title for the line chart (press Enter for default title): ")
xlabel = input("Enter label for x axis (press Enter for default label): ")
ylabel = input("Enter label for y axis (press Enter for default label): ")

create_line_chart(x_values, y_values, x_head, y_head, title, xlabel, ylabel)
