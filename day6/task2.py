import math

def read_int():
    return int(input())

def read_float():
    return float(input())

def normal_cdf(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

n_tickets = read_int()
n_students = read_int()
mean = read_float()
std_dev = read_float()

mu = mean * n_students
sigma = math.sqrt(n_students) * std_dev

p = normal_cdf(n_tickets, mu, sigma)
print (f"{p:.4f}")