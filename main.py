import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from regression import params


def main():
    thermocouple = pd.read_csv('data/data.csv')
    print(thermocouple)  
    thermocouple.plot.scatter(x='Change in T (deg C)', y='Voltage (mV)')
    slope = params(thermocouple['Change in T (deg C)'], thermocouple['Voltage (mV)'])[0]
    intercept = params(thermocouple['Change in T (deg C)'], thermocouple['Voltage (mV)'])[1]
    plt.plot([0, 300], [intercept, slope*300])
    print((slope, intercept))
    plt.show()
    thermocouple.plot.scatter(x='Change in T (deg C)', y='Seebeck Coefficient (mV/deg C)')
    plt.show()
    print("hello world!")

    
if __name__ == '__main__':
    main()