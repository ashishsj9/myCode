import csv
import numpy as np
import matplotlib.pyplot as plt

with open ('/Users/ashishjhade/Documents/myCode/data/weight-height.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

# Create data
N = 500
x = csv_reader.row['first_name']
y = csv_reader.row['first_name']
colors = (0,0,0)
area = np.pi*3

# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
