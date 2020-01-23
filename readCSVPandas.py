import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/ashishjhade/Documents/myCode/data/weight-height.csv')
#print(df)

df.plot.scatter(x='Height', y='Weight', c='black')
plt.show()
