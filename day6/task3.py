import math

def read_int():
    return int(input())

def read_float():
    return float(input())

def normal_cdf(x, mean, std_dev):
    return 0.5 * (1 + math.erf((x - mean) / (sigma * math.sqrt(2))))

def get_interval(z, mu, sigma):
    u = mu + z * sigma
    l = mu - z * sigma
    return (l, u)

sample_size = read_int()
mean = read_int()
std_dev = read_int()
distribution_pct = read_float()
z_score = read_float()

std_dev = std_dev / math.sqrt(sample_size)
l, u = get_interval(z_score, mean, std_dev)

print (f"{l:.2f}")
print (f"{u:.2f}")