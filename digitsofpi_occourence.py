
import numpy as np


f = open("millionpi.txt", 'r')

pi_string = f.read()

num_count = np.zeros(10)
for i in pi_string:
    if i == '1':
        num_count[1] += 1
    elif i == '2':
        num_count[2] += 1
    elif i == '3':
        num_count[3] += 1
    elif i == '4':
        num_count[4] += 1
    elif i == '5':
        num_count[5] += 1
    elif i == '6':
        num_count[6] += 1
    elif i == '7':
        num_count[7] += 1
    elif i == '8':
        num_count[8] += 1
    elif i == '9':
        num_count[9] += 1
    elif i == '0':
        num_count[0] += 1

    # print(i, num_count)
    if np.all(num_count == num_count[0]):
        print(i)

print(num_count)
