import matplotlib.pyplot as plt
import numpy as np

def create_heatmap(data, row_labels, col_labels, title=None, xlabel=None, ylabel=None):
    fig, ax = plt.subplots()
    cax = ax.matshow(data, cmap='viridis')

    fig.colorbar(cax)
    ax.set_xticks(np.arange(len(col_labels)))
    ax.set_yticks(np.arange(len(row_labels)))
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

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

def get_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = get_user_input(f"Enter {cols} values for row {i + 1} separated by commas: ", float)
        if len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            return get_matrix(rows, cols)
        matrix.append(row)
    return matrix

# Take user input for the heatmap details
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
data = get_matrix(rows, cols)

row_labels = input("Enter row labels separated by commas: ").split(',')
col_labels = input("Enter column labels separated by commas: ").split(',')

if len(row_labels) != rows:
    print(f"Number of row labels must match the number of rows. Defaulting to numerical labels.")
    row_labels = [f"Row {i+1}" for i in range(rows)]
if len(col_labels) != cols:
    print(f"Number of column labels must match the number of columns. Defaulting to numerical labels.")
    col_labels = [f"Col {i+1}" for i in range(cols)]

title = input("Enter title for the heatmap: ")
xlabel = input("Enter label for x-axis: ")
ylabel = input("Enter label for y-axis: ")

create_heatmap(data, row_labels, col_labels, title, xlabel, ylabel)
