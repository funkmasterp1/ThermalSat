#pip install requests numpy matplotlib


import requests
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the location you are interested in
latitude = 37.422
longitude = -122.084

# Define the time period (start and end date)
start_date = '2022-01-01'
end_date = '2022-01-01'

# Construct the MODIS Thermal data URL
url = f'https://ladsweb.modaps.eosdis.nasa.gov/opendap/hyrax/MOD11C2_L2/{start_date[:4]}.{start_date[5:7]}.{start_date[8:10]}/'

# Request the data for the specified location and time period
response = requests.get(url)
data = response.content

# You will need to parse the data based on the format of the MODIS dataset.
# This might involve some data processing, depending on the specific dataset you are using.

# For example, if the data is in CSV format, you can use numpy to load and process it:
# thermal_data = np.loadtxt(data, delimiter=',', skiprows=1)

# Once you have the thermal data loaded, you can visualize it using matplotlib:
# plt.imshow(thermal_data, cmap='hot')
# plt.colorbar()
# plt.show()

# Note: The exact steps for processing the data depend on the format of the dataset you are working with.
# You might need to adjust the code accordingly based on the dataset's structure.
