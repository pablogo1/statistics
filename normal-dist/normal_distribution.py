import math

def normal_cdf(x, mean=0, std_dev=1) -> float:
    ''' Returns the normal CDF (cumulative distribution function) of x
        given the mean and standard deviation.
    '''
    return 0.5 * (1 + math.erf((x - mean) / (std_dev * math.sqrt(2))))

