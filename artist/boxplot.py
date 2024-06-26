import matplotlib.pyplot as plt

def create_box_plot(data, labels=None, title=None, xlabel=None, ylabel=None):
    plt.boxplot(data, labels=labels)
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

def get_multiple_data_sets():
    data_sets = []
    while True:
        data = get_user_input("Enter data values for a dataset separated by commas (or press Enter to finish): ", float)
        if not data:
            break
        data_sets.append(data)
    return data_sets

# Take user input for data and box plot details
data_sets = get_multiple_data_sets()
labels = input("Enter labels for each dataset separated by commas (or press Enter to skip): ").split(',')
if len(labels) == 1 and labels[0] == '':
    labels = None
title = input("Enter title for the box plot: ")
xlabel = input("Enter label for x-axis: ")
ylabel = input("Enter label for y-axis: ")

create_box_plot(data_sets, labels, title, xlabel, ylabel)
