from common.normal_distribution import normal_cdf

class Problem1:
    mean = 20.0
    std_dev = 2.0

    def run(self, param1, param2, param3):
        p_less_than_p1 = normal_cdf(param1, self.mean, self.std_dev)
        p_between_p2_p3 = normal_cdf(param3, self.mean, self.std_dev) - normal_cdf(param2, self.mean, self.std_dev)
        
        print(f"{p_less_than_p1:.3f}")
        print(f"{p_between_p2_p3:.3f}")