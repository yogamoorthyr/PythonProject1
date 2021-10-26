

x=[1,4,10, 12,2,8,10,12]
print(x)

x=(1,4,10,9,5,7)
print (x)
import numpy as np

print (x)

new_x = np.array(x)
x+x
print (x+x)

import matplotlib.pyplot as plt


import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index=row_labels
print(cars)
print (cars.index)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))