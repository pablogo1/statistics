import math

def normal_cdf(x, mean=0, std_dev=1) -> float:
    ''' Returns the normal CDF (cumulative distribution function) of x
        given the mean and standard deviation.
    '''
    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))

def normal_pdf(x, mean, std_dev):
    ''' Returns the normal PDF (probability density function) of normal distribution
        given the mean and standard deviation.
    '''
    return math.exp(-0.5 * ((x - mean) / std_dev)**2) / (std_dev * math.sqrt(2 * math.pi))
