import math

def read_int():
    return int(input())

def normal_cdf(x, mean=0, std_dev=1) -> float:
    ''' Returns the normal CDF (cumulative distribution function) of x
        given the mean and standard deviation.
    '''
    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))

max_weight = read_int()
n_boxes = read_int()
mean_weight = read_int()
std_dev = read_int()

p = normal_cdf(max_weight, mean, std_dev)
print (f"{p:.4f}")