import matplotlib.pyplot as plt

def create_histogram(data, bins, title=None, xlabel=None, ylabel=None):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def get_user_input(prompt, input_type=float):
    while True:
        user_input = input(prompt)
        try:
            user_input = [input_type(val) for val in user_input.split(',')]
            return user_input
        except ValueError:
            print("Invalid input. Please enter comma-separated values of the correct type.")

# Take user input for data and histogram details
data = get_user_input("Enter data values separated by commas: ")
bins = int(input("Enter the number of bins for the histogram: "))
title = input("Enter title for the histogram: ")
xlabel = input("Enter label for x-axis: ")
ylabel = input("Enter label for y-axis: ")

create_histogram(data, bins, title, xlabel, ylabel)
