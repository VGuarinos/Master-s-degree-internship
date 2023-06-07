
#import os, time
from netCDF4 import Dataset as NetCDFFile
#import netCDF4 as nc
import numpy as np
#import scipy.stats
#import os.path
import numpy.ma as ma
import pandas as pd

df = pd.DataFrame()

mask = NetCDFFile('Data/mesh_mask_briac.nc')
lat = mask.variables['gphiu'][0,:,:]
lon = mask.variables['glamu'][0,:,:]
tmask = mask.variables['tmask'][0,:,:,:]
tmask_masked = ma.masked_values(tmask, 0)
umask = mask.variables['umask'][0,:,:,:]
umask_masked = ma.masked_values(umask, 0)
vmask = mask.variables['vmask'][0,:,:,:]
vmask_masked = ma.masked_values(vmask, 0)
e2u =mask.variables['e2u'][:,:]
e3u =mask.variables['e3u'][0,:,:,:]
e1v =mask.variables['e1v'][:,:]
e3v =mask.variables['e3v'][0,:,:,:]


e2u_rep = np.ones(umask.shape)
e1v_rep = np.ones(vmask.shape)
k = 0
for k in range(0, 43):
    e2u_rep[k, :, :] = e2u_rep[k, :, :] * e2u[:, :]
    e1v_rep[k, :, :] = e1v_rep[k, :, :] * e1v[:, :]

nc_U = NetCDFFile('Data/Control/PICTRL_ORCM_3D_fields_0201-0230_yearly_ave.nc')
nc_V = NetCDFFile('Data/Control/PICTRL_ORCM_3D_fields_0201-0230_yearly_ave.nc')

U = nc_U.variables['vozocrtx'][0, :, :, :]  #vozocrtx =>
V = nc_V.variables['vomecrty'][0, :, :, :]  #vomecrty =>    => On utilise celui ci pour calculer les courants horizontaux
print("U.shape = ", U.shape)


###################################################################################
kmin = 14   #definition of minimum depth (counted)
kmax = 20  #definition of maximum depth (NON-counted) => Give the depth wanted +1
###################################################################################

##Méthode une section droite

FV_sic_tun_tot = V[kmin:kmax, 62, 288] * e3v[kmin:kmax, 62, 288] * e1v_rep[kmin:kmax, 62, 288] #[k,i,j]
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 61, 288] * e3v[kmin:kmax, 61, 288] * e1v_rep[kmin:kmax, 61, 288] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 60, 288] * e3v[kmin:kmax, 60, 288] * e1v_rep[kmin:kmax, 60, 288] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 59, 288] * e3v[kmin:kmax, 59, 288] * e1v_rep[kmin:kmax, 59, 288] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 58, 288] * e3v[kmin:kmax, 58, 288] * e1v_rep[kmin:kmax, 58, 288] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 57, 289] * e3v[kmin:kmax, 57, 289] * e1v_rep[kmin:kmax, 57, 289] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 56, 290] * e3v[kmin:kmax, 56, 290] * e1v_rep[kmin:kmax, 56, 290] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 55, 291] * e3v[kmin:kmax, 55, 291] * e1v_rep[kmin:kmax, 55, 291] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 54, 292] * e3v[kmin:kmax, 54, 292] * e1v_rep[kmin:kmax, 54, 292] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 53, 293] * e3v[kmin:kmax, 53, 293] * e1v_rep[kmin:kmax, 53, 293] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 52, 294] * e3v[kmin:kmax, 52, 294] * e1v_rep[kmin:kmax, 52, 294] )

FV_sic_tun_tot2 = ( V[kmin:kmax, 49, 315] * e3v[kmin:kmax, 49, 315] * e1v_rep[kmin:kmax, 49, 315] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 50, 316] * e3v[kmin:kmax, 50, 316] * e1v_rep[kmin:kmax, 50, 316] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 50, 317] * e3v[kmin:kmax, 50, 317] * e1v_rep[kmin:kmax, 50, 317] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 50, 318] * e3v[kmin:kmax, 50, 318] * e1v_rep[kmin:kmax, 50, 318] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 51, 319] * e3v[kmin:kmax, 51, 319] * e1v_rep[kmin:kmax, 51, 319] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 51, 320] * e3v[kmin:kmax, 51, 320] * e1v_rep[kmin:kmax, 51, 320] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 51, 321] * e3v[kmin:kmax, 51, 321] * e1v_rep[kmin:kmax, 51, 321] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 53, 322] * e3v[kmin:kmax, 53, 322] * e1v_rep[kmin:kmax, 53, 322] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 53, 323] * e3v[kmin:kmax, 53, 323] * e1v_rep[kmin:kmax, 53, 323] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 54, 324] * e3v[kmin:kmax, 54, 324] * e1v_rep[kmin:kmax, 54, 324] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 55, 325] * e3v[kmin:kmax, 55, 325] * e1v_rep[kmin:kmax, 55, 325] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 56, 326] * e3v[kmin:kmax, 56, 326] * e1v_rep[kmin:kmax, 56, 326] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 56, 327] * e3v[kmin:kmax, 56, 327] * e1v_rep[kmin:kmax, 56, 327] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 60, 330] * e3v[kmin:kmax, 60, 330] * e1v_rep[kmin:kmax, 60, 330] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 61, 330] * e3v[kmin:kmax, 61, 330] * e1v_rep[kmin:kmax, 61, 330] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 62, 330] * e3v[kmin:kmax, 62, 330] * e1v_rep[kmin:kmax, 62, 330] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 63, 330] * e3v[kmin:kmax, 63, 330] * e1v_rep[kmin:kmax, 63, 330] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( V[kmin:kmax, 64, 330] * e3v[kmin:kmax, 64, 330] * e1v_rep[kmin:kmax, 64, 330] )



FV_sic_tunV_tot_in = FV_sic_tun_tot[FV_sic_tun_tot < 0].sum()
FV_sic_tunV_tot_out = FV_sic_tun_tot[FV_sic_tun_tot > 0].sum()
FV_sic_tunV_tot_in2 = FV_sic_tun_tot2[FV_sic_tun_tot2 < 0].sum()
FV_sic_tunV_tot_out2 = FV_sic_tun_tot2[FV_sic_tun_tot2 > 0].sum()

print("Aegean_V_West_in = " ,FV_sic_tunV_tot_out)
print("Aegean_V_West_out = " ,FV_sic_tunV_tot_in)
print("Aegean_V_East_in = " ,FV_sic_tunV_tot_out2)
print("Aegean_V_East_out = " ,FV_sic_tunV_tot_in2)

FV_sic_tun_tot = U[kmin:kmax, 66, 190:226] * e3u[kmin:kmax, 66, 190:226] * e2u_rep[kmin:kmax, 66, 190:226] #[k,i,j]


FV_sic_tun_tot = U[kmin:kmax, 62, 288] * e3u[kmin:kmax, 62, 288] * e2u_rep[kmin:kmax, 62, 288] #[k,i,j]
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 61, 288] * e3u[kmin:kmax, 61, 288] * e2u_rep[kmin:kmax, 61, 288] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 60, 288] * e3u[kmin:kmax, 60, 288] * e2u_rep[kmin:kmax, 60, 288] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 59, 288] * e3u[kmin:kmax, 59, 288] * e2u_rep[kmin:kmax, 59, 288] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 58, 288] * e3u[kmin:kmax, 58, 288] * e2u_rep[kmin:kmax, 58, 288] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 57, 289] * e3u[kmin:kmax, 57, 289] * e2u_rep[kmin:kmax, 57, 289] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 56, 290] * e3u[kmin:kmax, 56, 290] * e2u_rep[kmin:kmax, 56, 290] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 55, 291] * e3u[kmin:kmax, 55, 291] * e2u_rep[kmin:kmax, 55, 291] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 54, 292] * e3u[kmin:kmax, 54, 292] * e2u_rep[kmin:kmax, 54, 292] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 53, 293] * e3u[kmin:kmax, 53, 293] * e2u_rep[kmin:kmax, 53, 293] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 52, 294] * e3u[kmin:kmax, 52, 294] * e2u_rep[kmin:kmax, 52, 294] )


FV_sic_tun_tot2 = ( U[kmin:kmax, 49, 315] * e3u[kmin:kmax, 49, 315] * e2u_rep[kmin:kmax, 49, 315] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 50, 316] * e3u[kmin:kmax, 50, 316] * e2u_rep[kmin:kmax, 50, 316] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 50, 317] * e3u[kmin:kmax, 50, 317] * e2u_rep[kmin:kmax, 50, 317] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 50, 318] * e3u[kmin:kmax, 50, 318] * e2u_rep[kmin:kmax, 50, 318] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 51, 319] * e3u[kmin:kmax, 51, 319] * e2u_rep[kmin:kmax, 51, 319] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 51, 320] * e3u[kmin:kmax, 51, 320] * e2u_rep[kmin:kmax, 51, 320] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 51, 321] * e3u[kmin:kmax, 51, 321] * e2u_rep[kmin:kmax, 51, 321] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 53, 322] * e3u[kmin:kmax, 53, 322] * e2u_rep[kmin:kmax, 53, 322] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 53, 323] * e3u[kmin:kmax, 53, 323] * e2u_rep[kmin:kmax, 53, 323] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 54, 324] * e3u[kmin:kmax, 54, 324] * e2u_rep[kmin:kmax, 54, 324] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 55, 325] * e3u[kmin:kmax, 55, 325] * e2u_rep[kmin:kmax, 55, 325] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 56, 326] * e3u[kmin:kmax, 56, 326] * e2u_rep[kmin:kmax, 56, 326] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 56, 327] * e3u[kmin:kmax, 56, 327] * e2u_rep[kmin:kmax, 56, 327] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 60, 330] * e3u[kmin:kmax, 60, 330] * e2u_rep[kmin:kmax, 60, 330] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 61, 330] * e3u[kmin:kmax, 61, 330] * e2u_rep[kmin:kmax, 61, 330] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 62, 330] * e3u[kmin:kmax, 62, 330] * e2u_rep[kmin:kmax, 62, 330] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 63, 330] * e3u[kmin:kmax, 63, 330] * e2u_rep[kmin:kmax, 63, 330] )
FV_sic_tun_tot2 = FV_sic_tun_tot2 + ( U[kmin:kmax, 64, 330] * e3u[kmin:kmax, 64, 330] * e2u_rep[kmin:kmax, 64, 330] )


FV_sic_tunU_tot_in = FV_sic_tun_tot[FV_sic_tun_tot < 0].sum()
FV_sic_tunU_tot_out = FV_sic_tun_tot[FV_sic_tun_tot > 0].sum()
FV_sic_tunU_tot_in2 = FV_sic_tun_tot2[FV_sic_tun_tot2 < 0].sum()
FV_sic_tunU_tot_out2 = FV_sic_tun_tot2[FV_sic_tun_tot2 > 0].sum()

print("Aegean_U_West_in = " ,FV_sic_tunU_tot_out)
print("Aegean_U_West_out = " ,FV_sic_tunU_tot_in)
print("Aegean_U_East_in = " ,FV_sic_tunU_tot_in2)
print("Aegean_U_East_out = " ,FV_sic_tunU_tot_out2)
