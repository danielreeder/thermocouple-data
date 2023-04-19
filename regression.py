import numpy as np

def std_units(x):
    return (x - np.mean(x)) / np.std(x)

def params(x, y):
    r = np.mean(std_units(x) * std_units(y))
    slope = r * np.std(y) / np.std(x)
    intercept = np.mean(y) - (slope * np.mean(x))
    return [slope, intercept]