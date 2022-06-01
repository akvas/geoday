import numpy as np 
import datetime as dt 


def mjd2timestamp(mjd):
    """Compute UNIX time stamp from MJD."""
    return int((dt.datetime(1858, 11, 17) + dt.timedelta(days=mjd)).timestamp() * 1000)
    
    
def print_series(timestamps, data, color, label):

    template = """
    {{
        values: {0}
        text: '{1}',
        lineColor: '{2}',
        marker: {{ backgroundColor: '{2}' }}
    }},
    """

    output_string = '['
    for tk, dm in zip(timestamps, data):
        output_string += '[{0:d}, {1:e}], '.format(tk, dm)
    
    print(template.format(output_string[0:-2] + '],', label, color))


colors = """#59C7EB
#E0607E
#0A9086
#FEA090
#3E5496
#EFDC60
#8E2043
#9AA0A7
#077187""".split('\n')

data = np.loadtxt('GIS_GMB_basin.dat')

timestamps = [mjd2timestamp(tk) for tk in data[:, 1]]

for k, region in enumerate(range(2, data.shape[1], 2)):    
    print_series(timestamps, data[:, region] * 1e-12, colors[k], 'Region {0:d}'.format(k + 1))

total_mass =  data[:, -2] * 1e-12
print_series(timestamps, total_mass, colors[-1], 'Gesamt')
