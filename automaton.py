import numpy as np

rule = 220


def to_bin(x):
    tmp = bin(x).replace("b", "")
    difference = 0

    if len(tmp) < 8:
        difference = 8-len(tmp)

    zeros = ""
    for i in range(0,difference):
        zeros += "0"

    tmp = zeros+tmp
    if len(tmp) > 8:
        tmp = tmp[1:len(tmp)]
    return tmp


def to_reversed_array(bin_string):
    bin_array = np.zeros((1, 8), int)[0]
    i = 0
    for x in bin_string:
        bin_array[7 - i] = int(x)
        i += 1
    return bin_array


def set_cell(string_number, sample):
    number = int(string_number, 2)
    if sample[number] == 1:
        return 1
    else:
        return 0


sample = to_reversed_array(to_bin(rule))  # array of reversed binary number

# ****************CREATING TAB****************
rows = 16
columns = 31

automat = np.zeros((rows, columns), int)
automat[0][int(columns / 2)] = 1
# ********************************************

for i in range(1, rows):
    for j in range(0, columns):
        if j == 0:
            tmp = str(automat[i - 1][columns - 1]) + str(automat[i - 1][j]) + str(automat[i - 1][j + 1])
            automat[i][j] = set_cell(tmp, sample)
        elif j == columns - 1:
            tmp = str(automat[i - 1][j - 1]) + str(automat[i - 1][j]) + str(automat[i - 1][0])
            automat[i][j] = set_cell(tmp, sample)
        else:
            tmp = str(automat[i-1][j-1]) + str(automat[i-1][j]) + str(automat[i-1][j+1])
            automat[i][j] = set_cell(tmp, sample)
