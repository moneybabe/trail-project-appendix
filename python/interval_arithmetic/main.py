from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
from definitions import *
from tqdm import tqdm


def process_interval_chunk(interval_chunk):
    results = []
    for interval in tqdm(interval_chunk):
        a, b = interval
        output = M54_down(a, b)
        results.append((output, a, b))
    return results


def main():
    n_intervals = int(1e7)
    interval = iv.linspace("1/3", "3", n_intervals)
    workers = 8
    interval_chunks = np.array_split(list(zip(interval, interval[1:])), workers)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = executor.map(process_interval_chunk, interval_chunks)

    # Flatten the results
    results = [item for sublist in results for item in sublist]
    m54_down, a, b = zip(*results)
    m54_down = [float(x.a) for x in m54_down]
    a = [float(x.a) for x in a]
    b = [float(x.b) for x in b]
    results_df = pd.DataFrame(
        {
            "a": a,
            "b": b,
            "m54_down": m54_down,
        }
    )
    results_df.to_csv("results.csv", index=False)


if __name__ == "__main__":
    main()
