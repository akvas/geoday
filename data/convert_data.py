import numpy as np 
import datetime as dt 


def mjd2timestamp(mjd):
    """Compute UNIX time stamp from MJD."""
    return int((dt.datetime(1858, 11, 17) + dt.timedelta(days=mjd)).timestamp() * 1000)
    
    
def print_series(timestamps, data):

    output_string = '['
    for tk, dm in zip(timestamps, data):
        output_string += '[{0:d}, {1:e}], '.format(tk, dm)
    
    print(output_string[0:-2] + '],')

data = np.loadtxt('GIS_GMB_basin.dat')

timestamps = [mjd2timestamp(tk) for tk in data[:, 1]]
total_mass = list(np.sum(data[:, 2:-1:2], axis=1) * 1e-12)
print_series(timestamps, total_mass)

# for region in range(2, data.shape[1], 2):
#     print("----------------------------")
#     print_series(timestamps, data[:, region] * 1e-12)
