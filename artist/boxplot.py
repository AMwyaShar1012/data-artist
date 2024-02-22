import matplotlib.pyplot as plt

def create_box_plot(data, labels=None, title=None, xlabel=None, ylabel=None):
    plt.boxplot(data, labels=labels)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Take user input for data and box plot details
data = [float(val) for val in input("Enter data values separated by commas: ").split(',')]
labels = input("Enter labels for the box plot separated by commas (press Enter if not applicable): ").split(',')
title = input("Enter title for the box plot: ")
xlabel = input("Enter label for x-axis: ")
ylabel = input("Enter label for y-axis: ")

create_box_plot(data, labels, title, xlabel, ylabel)
