from concurrent.futures import ThreadPoolExecutor

import numpy as np
from definitions import *

if __name__ == "__main__":
    n_intervals = 1e4
    values = np.linspace(round_down(1 / 3), round_up(3), int(n_intervals))
    lower_m, upper_m = [], []

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(calculate_rounded_bounds, values, values[1:]))

    for lower, upper in results:
        lower_m.append(upper)
        upper_m.append(lower)

    print("Upper bound: ", np.max(upper_m))
    print("Lower bound: ", np.min(lower_m))
