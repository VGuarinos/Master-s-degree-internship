import matplotlib.patches as patches
import os, time
import matplotlib as mpl
from netCDF4 import Dataset as NetCDFFile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import os.path
import numpy.ma as ma
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1 import make_axes_locatable

### Definition of box
kmin = 0   #EMSW = 0:13 , EMIW = 13:20 , EMDW = 20:43
kmax = 1   #WMSW = 0:12, WMIW = 12:21, WMDW = 21:43
###

### Definition of basin of interest
mask = NetCDFFile('Data/Masques/MED8_MASK_ION_LEV.nc').variables['medek_mask'][0,:,:,:] #MED8_MASK_ION_LEV.nc , MED8_MASK_MEDWK.nc
print("mask.shape = ", mask.shape)
### Definition of Temp and Sal variables
Temp = NetCDFFile('Data/Control/MED8_1d_grid_W_picontrol_debiais.nc_0061_0090_avg_year.nc').variables['vovecrtz'][0,:,:,:]
Sal = NetCDFFile('Data/Control/MED8_1d_grid_W_picontrol_debiais.nc_0061_0090_avg_year.nc').variables['vovecrtz'][0,:,:,:]

#Verification
print("Temp.shape = ", Temp.shape)
print("Sal.shape = ", Sal.shape)

### Recover the basin of interest
Temp = Temp[:,:,:] * mask
Sal = Sal[:,:,:] * mask

#Verification
print("Temp.shape = ", Temp.shape)
print("Sal.shape = ", Sal.shape)

##############################################################################

initial_conditions = ({
    'k':[0],
    'temp': [0],
    'sal': [0]
               })

df = pd.DataFrame(initial_conditions)
for k in range(0,43):
    ### Mean of Temp and Sal for each level
    Temp2 = 0
    Temp2 = Temp[k,:,:]
    Temp3 = Temp2[Temp2 < 0.000000000001].mean()
    print("Mean Temperatures in box = ", Temp3, "°C")

    Sal2 = 0
    Sal2 = Sal[k,:,:]
    Sal3 = Sal2[Sal2 > 0.000000000001].mean()
    print("Mean Salinity in box = ", Sal3, "PSU")
    new_row = {'k': k,
               'Vertical+': Temp3,
               'Vertical-': Sal3
               }
    df = df.append(new_row, ignore_index=True)

df.to_excel('export/Temp and sal/vertical_Control_mean_EMS.xlsx', index = False)

#############################################################################################################################

initial_conditions = ({
    'k':[0],
    'temp': [0],
    'sal': [0]
               })

df2 = pd.DataFrame(initial_conditions)

### Definition of Temp and Sal variables
Temp = NetCDFFile('Data/Control/PICTRL_ORCM_3D_fields_0201-0230_yearly_ave.nc').variables['votemper'][0,:,:,:]
Sal = NetCDFFile('Data/Control/PICTRL_ORCM_3D_fields_0201-0230_yearly_ave.nc').variables['vosaline'][0,:,:,:]

for k in range(0,43):
    ### Mean of Temp and Sal for each level
    Temp2 = 0
    Temp2 = Temp[k,:,:]
    Temp3 = Temp2[Temp2 > 1].mean()
    print("Mean Temperatures in box = ", Temp3, "°C")

    Sal2 = 0
    Sal2 = Sal[k,:,:]
    Sal3 = Sal2[Sal2 > 1].mean()
    print("Mean Salinity in box = ", Sal3, "PSU")
    new_row = {'k': k,
               'temp': Temp3,
               'sal': Sal3
               }
    df2 = df2.append(new_row, ignore_index=True)

df2.to_excel('export/Temp and sal/temp&sal_Control_mean_EMS.xlsx', index = False)




### Mean of Temp and Sal
Temp2 = 0
Temp2 = Temp[kmin:kmax,:,:]
Temp3 = Temp2[Temp2 > 1].mean()
print("Mean Temperatures in box = ", Temp3, "°C")

Sal2 = 0
Sal2 = Sal[kmin:kmax,:,:]
Sal3 = Sal2[Sal2 > 1].mean()
print("Mean Salinity in box = ", Sal3, "PSU")
