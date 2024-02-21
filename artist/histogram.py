import matplotlib.pyplot as plt

def create_histogram(data, bins, title=None, xlabel=None, ylabel=None):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Take user input for data and histogram details
data = [float(val) for val in input("Enter data values separated by commas: ").split(',')]
bins = int(input("Enter the number of bins for the histogram: "))
title = input("Enter title for the histogram: ")
xlabel = input("Enter label for x-axis: ")
ylabel = input("Enter label for y-axis: ")

create_histogram(data, bins, title, xlabel, ylabel)
