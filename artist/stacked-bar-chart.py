import matplotlib.pyplot as plt

def create_stacked_bar_chart(labels, data, categories, title=None, xlabel=None, ylabel=None):
    # Initialize the bottom position to zero for stacking
    bottom = [0] * len(labels)
    
    for i, category_data in enumerate(data):
        plt.bar(labels, category_data, bottom=bottom, label=categories[i])
        bottom = [sum(x) for x in zip(bottom, category_data)]  # Update bottom for the next stack
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

def get_user_input(prompt, input_type=float):
    while True:
        user_input = input(prompt)
        try:
            user_input = [input_type(val) for val in user_input.split(',')]
            return user_input
        except ValueError:
            print("Invalid input. Please enter comma-separated values of the correct type.")

def get_multiple_data_sets(num_sets, num_bars):
    data_sets = []
    for i in range(num_sets):
        data = get_user_input(f"Enter values for {num_bars} bars in category {i + 1} separated by commas: ", float)
        if len(data) != num_bars:
            print(f"Please enter exactly {num_bars} values.")
            return get_multiple_data_sets(num_sets, num_bars)
        data_sets.append(data)
    return data_sets

# Get user input for stacked bar chart details
labels = input("Enter labels for bars separated by commas: ").split(',')
num_categories = int(input("Enter the number of categories: "))

categories = input("Enter names of the categories separated by commas: ").split(',')
if len(categories) != num_categories:
    print(f"Number of categories doesn't match. Please provide {num_categories} category names.")
    categories = input("Enter names of the categories again separated by commas: ").split(',')

data = get_multiple_data_sets(num_categories, len(labels))

title = input("Enter title for the stacked bar chart: ")
xlabel = input("Enter label for x-axis: ")
ylabel = input("Enter label for y-axis: ")

create_stacked_bar_chart(labels, data, categories, title, xlabel, ylabel)
