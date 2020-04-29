import math
from common.normal_distribution import normal_cdf

def read_int():
    return int(input())

def parse_input():
    max_weight = read_int()
    n_boxes = read_int()
    mean_weight = read_int()
    std_dev = read_int()

    return max_weight, n_boxes, mean_weight, std_dev

max_weight, n_boxes, mean_weight, std_dev = parse_input()
print (f"max_weight = {max_weight}")