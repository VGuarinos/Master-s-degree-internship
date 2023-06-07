
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
e2u =mask.variables['e2u'][:,:] # Taille de la case selon I (m)
e3u =mask.variables['e3u'][0,:,:,:] # Epaisseur de la couche k (m)
e1v =mask.variables['e1v'][:,:] # Taille case selon J(m)
e3v =mask.variables['e3v'][0,:,:,:] # Epaisseur de la couche k (m)


e2u_rep = np.ones(umask.shape)
e1v_rep = np.ones(vmask.shape)
k = 0
for k in range(0, 43):
    e2u_rep[k, :, :] = e2u_rep[k, :, :] * e2u[:, :]
    e1v_rep[k, :, :] = e1v_rep[k, :, :] * e1v[:, :]

nc_U = NetCDFFile('Data/EHOL/EHOL_ORCM_3D_fields_0061-0090_yearly_ave.nc')
nc_V = NetCDFFile('Data/EHOL/EHOL_ORCM_3D_fields_0061-0090_yearly_ave.nc')

U = nc_U.variables['vozocrtx'][0, :, :, :]  #vozocrtx =>
V = nc_V.variables['vomecrty'][0, :, :, :]  #vomecrty =>    => On utilise celui ci pour calculer les courants horizontaux
print("U.shape = ", U.shape)
###################################################################################
kmin = 14   #definition of minimum depth (counted)
kmax = 20  #definition of maximum depth (NON-counted) => Give the depth wanted +1
#EMSW = 0:13 , EMIW = 13:20 , EMDW = 20:43
#WMSW = 0:12, WMIW = 12:21, WMDW = 21:43
###################################################################################
##Transport sictun
sec = 'sictun'

##Méthode une section droite détroit de Sicile

FV_sic_tun_tot = V[kmin:kmax, 100, 252] * e3v[kmin:kmax, 100, 252] * e1v_rep[kmin:kmax, 100, 252] #[k,i,j]
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 100, 253] * e3v[kmin:kmax, 100, 253] * e1v_rep[kmin:kmax, 100, 253] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 100, 254] * e3v[kmin:kmax, 100, 254] * e1v_rep[kmin:kmax, 100, 254] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 100, 255] * e3v[kmin:kmax, 100, 255] * e1v_rep[kmin:kmax, 100, 255] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 101, 256] * e3v[kmin:kmax, 101, 256] * e1v_rep[kmin:kmax, 101, 256] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 101, 257] * e3v[kmin:kmax, 101, 257] * e1v_rep[kmin:kmax, 101, 257] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 101, 258] * e3v[kmin:kmax, 101, 258] * e1v_rep[kmin:kmax, 101, 258] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 101, 259] * e3v[kmin:kmax, 101, 259] * e1v_rep[kmin:kmax, 101, 259] )
FV_sic_tun_tot = FV_sic_tun_tot + ( V[kmin:kmax, 101, 260] * e3v[kmin:kmax, 101, 260] * e1v_rep[kmin:kmax, 101, 260] )




FV_sic_tunV_tot_in = FV_sic_tun_tot[FV_sic_tun_tot < 0].sum()
FV_sic_tunV_tot_out = FV_sic_tun_tot[FV_sic_tun_tot > 0].sum()

print("FV_Ad_V_tot_out = " ,FV_sic_tunV_tot_out)
print("FV_Ad_V_tot_in = " ,FV_sic_tunV_tot_in)

#FV_sic_tun_tot = U[:, 66, 190:226] * e3u[:, 66, 190:226] * e2u_rep[:, 66, 190:226] #[k,i,j]


FV_sic_tun_tot = U[kmin:kmax, 100, 252] * e3u[kmin:kmax, 100, 252] * e2u_rep[kmin:kmax, 100, 252] #[k,i,j]
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 100, 253] * e3u[kmin:kmax, 100, 253] * e2u_rep[kmin:kmax, 100, 253] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 100, 254] * e3u[kmin:kmax, 100, 254] * e2u_rep[kmin:kmax, 100, 254] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 100, 255] * e3u[kmin:kmax, 100, 255] * e2u_rep[kmin:kmax, 100, 255] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 101, 256] * e3u[kmin:kmax, 101, 256] * e2u_rep[kmin:kmax, 101, 256] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 101, 257] * e3u[kmin:kmax, 101, 257] * e2u_rep[kmin:kmax, 101, 257] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 101, 258] * e3u[kmin:kmax, 101, 258] * e2u_rep[kmin:kmax, 101, 258] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 101, 259] * e3u[kmin:kmax, 101, 259] * e2u_rep[kmin:kmax, 101, 259] )
FV_sic_tun_tot = FV_sic_tun_tot + ( U[kmin:kmax, 101, 260] * e3u[kmin:kmax, 101, 260] * e2u_rep[kmin:kmax, 101, 260] )


FV_sic_tunU_tot_in = FV_sic_tun_tot[FV_sic_tun_tot < 0].sum()
FV_sic_tunU_tot_out = FV_sic_tun_tot[FV_sic_tun_tot > 0].sum()

print("FV_Ad_U_tot_out = " ,FV_sic_tunU_tot_out)
print("FV_Ad_U_tot_in = " ,FV_sic_tunU_tot_in)
