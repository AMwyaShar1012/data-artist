import matplotlib.pyplot as plt

def create_pie_chart(labels, sizes, title=None):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(title if title else 'Pie Chart')
    plt.show()

# Take user input for labels and sizes
labels = input("Enter labels separated by commas: ").split(',')
sizes = [float(val) for val in input("Enter corresponding sizes separated by commas: ").split(',')]
title = input("Enter title for the pie chart (press Enter for default title): ")

create_pie_chart(labels, sizes, title)
