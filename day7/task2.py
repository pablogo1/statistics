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

def get_ranks(arr):
    hash_table = dict.fromkeys(arr, 0)
    arr.sort()
    for i in range(len(arr)):
        hash_table[arr[i]] = i+1
    return list(hash_table.values())

n = read_int()
X = read_float_arr()
Y = read_float_arr()

rx, ry = get_ranks(X), get_ranks(Y)
sum_di2 = sum(map(lambda x, y: (x - y)**2, rx, ry))
rxy = 1 - (6 * sum_di2 / (n*(n**2 - 1)))

print (f"{rxy:.3f}")