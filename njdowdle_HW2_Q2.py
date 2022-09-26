import numpy as np
import csv
import matplotlib.pyplot as plt
import random

# read in data to np array

path = open('/Users/nolandowdle/Desktop/CSC533/HW2/HW2/IL_employee_salary.csv')
array = np.loadtxt(path, delimiter=',', dtype=str, skiprows=1)

num_rows, num_cols = array.shape
i = 0
while i < num_rows:
    i += 1

# count number of employees in each salary range
lessThanFiftyCounter = 0
fiftyCounter = 0 # count number of employees from 50-60k
sixtyCounter = 0 # count number of employees from 60-70k
seventyCounter = 0 # count number of employees from 70-80k
eightyCounter = 0 # count number of employees from 80-90k
nintyCounter = 0 # count number of employees above 90k
greaterThanOneHundredCounter = 0

newArray = [None] * num_rows
i = 0
while i < num_rows:
    if (array[i][3].astype(float) < 50000):
        lessThanFiftyCounter += 1
    if (array[i][3].astype(float) > 50000 and array[i][3].astype(float) < 60000):
        fiftyCounter += 1
    if (array[i][3].astype(float) > 60000 and array[i][3].astype(float) < 70000):
        sixtyCounter += 1
    if (array[i][3].astype(float) > 70000 and array[i][3].astype(float) < 80000):
        seventyCounter += 1
    if (array[i][3].astype(float) > 80000 and array[i][3].astype(float) < 90000):
        eightyCounter += 1
    if (array[i][3].astype(float) > 90000 and array[i][3].astype(float) < 100000):
        nintyCounter += 1
    if (array[i][3].astype(float) > 100000):
        greaterThanOneHundredCounter += 1
    newArray[i] = array[i][3].astype(float)
    i += 1

# set width for bars in histogram
barWidth = 0.2
# create histogram without the epsilon-differential privacy
data = {'50k':fiftyCounter, '60k':sixtyCounter,
         '70k':seventyCounter, '80k':eightyCounter, '90k':nintyCounter}

ranges = list(data.keys())
values = list(data.values())

bar1 = plt.bar(np.arange(len(ranges)) - 0.4, values, color ='r', width = barWidth, label='unperturbed')

# histogram with epsilon = 0.05
loc = 0
scale = 1 / 0.05 # known as lambda
noise, noise1, noise2, noise3, noise4 = np.random.laplace(loc, scale, 5)

fiftyCounter0 = fiftyCounter
sixtyCounter0 = sixtyCounter
seventyCounter0 = seventyCounter
eightyCounter0 = eightyCounter
nintyCounter0 = nintyCounter

fiftyCounter0 += noise
sixtyCounter0 += noise1
seventyCounter0 += noise2
eightyCounter0 += noise3
nintyCounter0 += noise4


# create histogram without the epsilon-differential privacy
data = {'50k':fiftyCounter0, '60k':sixtyCounter0,
         '70k':seventyCounter0, '80k':eightyCounter0, '90k':nintyCounter0}

ranges = list(data.keys())
values = list(data.values())

bar2 = plt.bar(np.arange(len(ranges)) - 0.2, values, width=barWidth, label='0.05')



# create histogram for epsilon = 0.1
loc = 0
scale = 1 / 0.1 # known as lambda
noise, noise1, noise2, noise3, noise4 = np.random.laplace(loc, scale, 5)

fiftyCounter1 = fiftyCounter
sixtyCounter1 = sixtyCounter
seventyCounter1 = seventyCounter
eightyCounter1 = eightyCounter
nintyCounter1 = nintyCounter

fiftyCounter1 += noise
sixtyCounter1 += noise1
seventyCounter1 += noise2
eightyCounter1 += noise3
nintyCounter1 += noise4


# create histogram without the epsilon-differential privacy
data = {'50k':fiftyCounter1, '60k':sixtyCounter1,
         '70k':seventyCounter1, '80k':eightyCounter1, '90k':nintyCounter1}

ranges = list(data.keys())
values = list(data.values())

bar3 = plt.bar(np.arange(len(ranges)), values,  width=barWidth, label='0.1')

# create histogram for epsilon = 5.0
loc = 0
scale = 1 / 5.0 # known as lambda
noise, noise1, noise2, noise3, noise4 = np.random.laplace(loc, scale, 5)

fiftyCounter2 = fiftyCounter
sixtyCounter2 = sixtyCounter
seventyCounter2 = seventyCounter
eightyCounter2 = eightyCounter
nintyCounter2 = nintyCounter

fiftyCounter2 += noise
sixtyCounter2 += noise1
seventyCounter2 += noise2
eightyCounter2 += noise3
nintyCounter2 += noise4


# create histogram without the epsilon-differential privacy
data = {'50k':fiftyCounter2, '60k':sixtyCounter2,
         '70k':seventyCounter2, '80k':eightyCounter2, '90k':nintyCounter2}

ranges = list(data.keys())
values = list(data.values())

bar4 = plt.bar(np.arange(len(ranges)) + 0.2, values, width=barWidth, label='5.0')


plt.xlabel("Salary Ranges")
plt.ylabel("Number of Employees")
plt.title("Salary Brackets")
plt.legend()
plt.show()