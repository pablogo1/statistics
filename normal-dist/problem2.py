from normal_distribution import normal_cdf

class Problem2:
    mean = 70.0
    std_dev = 10.0

    def run(self, param1, param2):
        pct_larger_than_80 = (1 - normal_cdf(80, self.mean, self.std_dev)) * 100
        pct_larger_equal_than_60 = (1 - normal_cdf(60, self.mean, self.std_dev)) * 100
        pct_less_than_60 = normal_cdf(60, self.mean, self.std_dev) * 100
        print (f"{pct_larger_than_80:.2f}")
        print (f"{pct_larger_equal_than_60:.2f}")
        print (f"{pct_less_than_60:.2f}")
        # p_less_than_p2 = normal_cdf(param2, self.mean, self.std_dev) - normal_cdf(param1, self.mean, self.std_dev)
        # return p_less_than_p2