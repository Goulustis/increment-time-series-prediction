import numpy as np

def get_data(n_samples:int=1000):
    return np.random.rand(n_samples)

def main():
    series = get_data()
    diffs = np.diff(series)
    diff_signs = np.sign(diffs)

    pred_sign = np.sign(0.5 - series[:-1])
    print((pred_sign == diff_signs).mean())


if __name__ == "__main__":
    main()
