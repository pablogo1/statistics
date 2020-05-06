import math

def read_int():
    return int(input())

def read_float_arr():
    return list(map(float, input().rstrip().split()))

def cov(X, Y, mean_x, mean_y):
    return sum(map(lambda x, y: (x - mean_x) * (y - mean_y), X, Y)) / len(X)

def std_dev(arr, mean):
    return math.sqrt(sum(map(lambda x: (x - mean)**2, arr)) / len(arr))

def mean(arr):
    return sum(arr) / len(arr)

n = read_int()
X = read_float_arr()
Y = read_float_arr()

mean_x, mean_y = mean(X), mean(Y)
std_dev_x, std_dev_y = std_dev(X, mean_x), std_dev(Y, mean_y)
covariance = cov(X, Y, mean_x, mean_y)
p = covariance / (std_dev_x * std_dev_y)

print (f"{p:.3f}")
