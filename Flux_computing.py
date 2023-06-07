
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

nc_U = NetCDFFile('Data/EHOL/EHOL_ORCM_3D_fields_0061-0090_yearly_ave.nc')
nc_V = NetCDFFile('Data/EHOL/EHOL_ORCM_3D_fields_0061-0090_yearly_ave.nc')

U = nc_U.variables['vozocrtx'][0, :, :, :]  #vozocrtx =>
V = nc_V.variables['vomecrty'][0, :, :, :]  #vomecrty =>    => On utilise celui ci pour calculer les courants horizontaux
print("U.shape = ", U.shape)
###################################################################################

kmin = 20   #EMSW = 0:13 , EMIW = 13:20 , EMDW = 20:43
kmax = 43   #WMSW = 0:12, WMIW = 12:21, WMDW = 21:43

##Transport gib
sec = 'gib'

FV_gib_tot = U[kmin:kmax, 47:70, 58] * e3u[kmin:kmax, 47:70, 58] * e2u_rep[kmin:kmax, 47:70, 58]
FV_gib_tot_in = FV_gib_tot[FV_gib_tot > 0].sum()
FV_gib_tot_out = FV_gib_tot[FV_gib_tot < 0].sum()
print("Gib U tot out : ", FV_gib_tot_out)
print("Gib U tot in : ", FV_gib_tot_in)

###################################################################################
##Transport sictun
sec = 'sictun'

##Méthode une section droite détroit de Sicile

FV_sic_tun_tot = V[kmin:kmax, 66, 192:220] * e3v[kmin:kmax, 66, 192:220] * e1v_rep[kmin:kmax, 66, 192:220] #[k,i,j]
FV_sic_tunV_tot_in = FV_sic_tun_tot[FV_sic_tun_tot < 0].sum()
FV_sic_tunV_tot_out = FV_sic_tun_tot[FV_sic_tun_tot > 0].sum()

print("FV_sic_tun_V_tot_out = " ,FV_sic_tunV_tot_out)
print("FV_sic_tun_V_tot_in = " ,FV_sic_tunV_tot_in)

FV_sic_tun_tot = U[kmin:kmax, 66, 192:220] * e3u[kmin:kmax, 66, 192:220] * e2u_rep[kmin:kmax, 66, 192:220] #[k,i,j]
FV_sic_tunU_tot_in = FV_sic_tun_tot[FV_sic_tun_tot < 0].sum()
FV_sic_tunU_tot_out = FV_sic_tun_tot[FV_sic_tun_tot > 0].sum()

print("FV_sic_tun_U_tot_out = " ,FV_sic_tunU_tot_out)
print("FV_sic_tun_U_tot_in = " ,FV_sic_tunU_tot_in)

###################################################################################
##Méthode une section droite pour la mer Egée
FV_eg_tot = V[kmin:kmax, 63, 280:320] * e3v[kmin:kmax, 63, 280:320] * e1v_rep[kmin:kmax, 63, 280:320] #[k,i,j]
FV_egV_tot_in = FV_eg_tot[FV_eg_tot < 0].sum()
FV_egV_tot_out = FV_eg_tot[FV_eg_tot > 0].sum()

print("FV_eg_V_tot_out = " ,FV_egV_tot_out)
print("FV_eg_V_tot_in = " ,FV_egV_tot_in)

FV_eg_tot = U[kmin:kmax, 63, 280:320] * e3u[kmin:kmax, 63, 280:320] * e2u_rep[kmin:kmax, 63, 280:320] #[k,i,j]
FV_egU_tot_in = FV_eg_tot[FV_eg_tot < 0].sum()
FV_egU_tot_out = FV_eg_tot[FV_eg_tot > 0].sum()

print("FV_eg_U_tot_out = " ,FV_egU_tot_out)
print("FV_eg_U_tot_in = " ,FV_egU_tot_in)

###################################################################################
##Méthode une section droite pour la mer Adriatique
FV_ad_tot = V[kmin:kmax, 96, 252:265] * e3v[kmin:kmax, 96, 252:265] * e1v_rep[kmin:kmax, 96, 252:265] #[k,i,j]
FV_adV_tot_in = FV_ad_tot[FV_ad_tot < 0].sum()
FV_adV_tot_out = FV_ad_tot[FV_ad_tot > 0].sum()

print("FV_ad_V_tot_out = " ,FV_adV_tot_out) # section D pour voir le cascading
print("FV_ad_V_tot_in = " ,FV_adV_tot_in)

FV_ad_tot2 = V[kmin:kmax, 68, 224:279] * e3v[kmin:kmax, 68, 224:279] * e1v_rep[kmin:kmax, 68, 224:279] #[k,i,j]
FV_adV_tot_in2 = FV_ad_tot2[FV_ad_tot2 < 0].sum()
FV_adV_tot_out2 = FV_ad_tot2[FV_ad_tot2 > 0].sum()

print("FV_ad_V_tot_out2 = " ,FV_adV_tot_out2) #section E pour quantifier EMDW (cascading + convection
print("FV_ad_V_tot_in2 = " ,FV_adV_tot_in2)

FV_LIW_tot = U[kmin:kmax, 25:68, 279] * e3u[kmin:kmax, 25:68, 279] * e2u_rep[kmin:kmax, 25:68, 279] #[k,i,j]
FV_LIWU_tot_in = FV_LIW_tot[FV_LIW_tot < 0].sum()
FV_LIWU_tot_out = FV_LIW_tot[FV_LIW_tot > 0].sum()  #section F

print("FV_LIW_U_tot_out = " ,FV_LIWU_tot_out)
print("FV_LIW_U_tot_in = " ,FV_LIWU_tot_in)

###################################################################################

##Méthode une section droite pour la NWM  => Pas convaincu...
#FV_nwm_tot = V[kmin:kmax, 105, 108:173] * e3v[kmin:kmax, 105, 108:173] * e1v_rep[kmin:kmax, 105, 108:173] #[k,i,j]
#FV_nwmV_tot_in = FV_nwm_tot[FV_nwm_tot < 0].sum()
#FV_nwmV_tot_out = FV_nwm_tot[FV_nwm_tot > 0].sum()

#print("FV_nwm_V_tot_out = " ,FV_nwmV_tot_out)
#print("FV_nwm_V_tot_in = " ,FV_nwmV_tot_in)

#FV_nwm_tot = V[kmin:kmax, 105, 180:222] * e3v[kmin:kmax, 105, 180:222] * e1v_rep[kmin:kmax, 105, 180:222] #[k,i,j]
#FV_nwmV_tot_in = FV_nwm_tot[FV_nwm_tot < 0].sum()
#FV_nwmV_tot_out = FV_nwm_tot[FV_nwm_tot > 0].sum()

#print("FV_nwm_V_tot_outS2 = " ,FV_nwmV_tot_out)
#print("FV_nwm_V_tot_inS2 = " ,FV_nwmV_tot_in)

FV_nwm_tot = V[kmin:kmax, 110, 100:235] * e3v[kmin:kmax, 110, 100:235] * e1v_rep[kmin:kmax, 110, 100:235] #[k,i,j]
FV_nwmV_tot_in = FV_nwm_tot[FV_nwm_tot < 0].sum()
FV_nwmV_tot_out = FV_nwm_tot[FV_nwm_tot > 0].sum()

print("FV_nwm_V_tot_outS3 = " ,FV_nwmV_tot_out)
print("FV_nwm_V_tot_inS3 = " ,FV_nwmV_tot_in)
##########################################################################
##Méthode une section droite pour Gibraltar => reussi
FV_gib3_tot = V[kmin:kmax, 45:70, 61] * e3v[kmin:kmax, 45:70, 61] * e1v_rep[kmin:kmax, 45:70, 61] #[k,i,j]
FV_gib3V_tot_in = FV_gib3_tot[FV_gib3_tot < 0].sum()
FV_gib3V_tot_out = FV_gib3_tot[FV_gib3_tot > 0].sum()

print("FV_gib3_V_tot_out = " ,FV_gib3V_tot_out)
print("FV_gib3_V_tot_in = " ,FV_gib3V_tot_in)

##Méthode une section droite pour Gibraltar => reussi
FV_gib3_tot = U[kmin:kmax, 45:70, 62] * e3u[kmin:kmax, 45:70, 62] * e2u_rep[kmin:kmax, 45:70, 62] #[k,i,j]
FV_gib3U_tot_in = FV_gib3_tot[FV_gib3_tot < 0].sum()
FV_gib3U_tot_out = FV_gib3_tot[FV_gib3_tot > 0].sum()

print("FV_gib3_U_tot_out = " ,FV_gib3U_tot_out)
print("FV_gib3_U_tot_in = " ,FV_gib3U_tot_in)

FV_ad_tot3 = V[kmin:kmax, 68, 224:279] * e3v[kmin:kmax, 68, 224:279] * e1v_rep[kmin:kmax, 68, 224:279] #[k,i,j]
FV_adV_tot_in3 = FV_ad_tot3[FV_ad_tot3 < 0].sum()
FV_adV_tot_out3 = FV_ad_tot3[FV_ad_tot3 > 0].sum()

print("FV_EMDW_V_tot_out3 = " ,FV_adV_tot_out3) #section E pour quantifier EMDW (cascading + convection
print("FV_EMDW_V_tot_in3 = " ,FV_adV_tot_in3)



FV_ad_tot3 = V[kmin:kmax, 54, 219:279] * e3v[kmin:kmax, 54, 219:279] * e1v_rep[kmin:kmax, 54, 219:279] #[k,i,j]
FV_adV_tot_in3 = FV_ad_tot3[FV_ad_tot3 < 0].sum()
FV_adV_tot_out3 = FV_ad_tot3[FV_ad_tot3 > 0].sum()

print("FV_EMDW_V_tot_out4 = " ,FV_adV_tot_out3) #section E pour quantifier EMDW (cascading + convection
print("FV_EMDW_V_tot_in4 = " ,FV_adV_tot_in3)

###################################################################################
#### Calcul moyenne U et V SF
###################################################################################
print("Gib U tot out : ", FV_gib_tot_out, "Gib U tot in : ", FV_gib_tot_in)
Gib1row = {'Section':"Gibraltar1",
           'Total_In':FV_gib_tot_in,
           'Total_Out':FV_gib_tot_out,
           'Unit':"m3/s"
           }
df = df.append(Gib1row, ignore_index=True)

m_gib3_out = FV_gib3U_tot_out
m_gib3_in = FV_gib3U_tot_in

print("Gib_Out : ",m_gib3_out,"- Gib_In : ",m_gib3_in)
Gib2row = {'Section':"Gibraltar2",
           'Total_In':m_gib3_in,
           'Total_Out':m_gib3_out,
           'Unit':"m3/s"
           }
df = df.append(Gib2row, ignore_index=True)

m_NWM_out = FV_nwmV_tot_out
m_NWM_in = FV_nwmV_tot_in

print("NWM_Out : ",m_NWM_out,"- NWM_In : ",m_NWM_in, " Currently not usable") #=> moyenne ok mais pas calculé au bon endroit
NWMrow = {'Section':"NWM section A&C",
           'Total_In':m_NWM_in,
           'Total_Out':m_NWM_out,
           'Unit':"m3/s"
           }
df = df.append(NWMrow, ignore_index=True)

m_Sic_out = FV_sic_tunV_tot_out
m_Sic_in = FV_sic_tunV_tot_in

print("Sic_Out : ",m_Sic_out,"- Sic_In : ",m_Sic_in)
Sicrow = {'Section':"Sicily strait",
           'Total_In':m_Sic_in,
           'Total_Out':m_Sic_out,
           'Unit':"m3/s"
           }
df = df.append(Sicrow, ignore_index=True)

m_eg_out = FV_egV_tot_out
m_eg_in = FV_egV_tot_in

print("Aegean_Out : ",m_eg_out,"- Aegean_In : ",m_eg_in)
Agrow = {'Section':"Aegean",
           'Total_In':m_eg_in,
           'Total_Out':m_eg_out,
           'Unit':"m3/s"
           }
df = df.append(Agrow, ignore_index=True)

m_ad_out = FV_adV_tot_out
m_ad_in = FV_adV_tot_in

print("Ad_Out : ",m_ad_out,"- Ad_In : ",m_ad_in)
Adrow = {'Section':"Adriatic",
           'Total_In':m_ad_in,
           'Total_Out':m_ad_out,
           'Unit':"m3/s"
           }
df = df.append(Adrow, ignore_index=True)
print("Ad_Out : ",FV_adV_tot_out2,"- Ad_In : ",FV_adV_tot_in2)
Adrow = {'Section':"AdriaticEMDW quantif",
           'Total_In':FV_adV_tot_in2,
           'Total_Out':FV_adV_tot_out2,
           'Unit':"m3/s"
           }
df = df.append(Adrow, ignore_index=True)

LIWrow = {'Section':"LIW quantif",
           'Total_In':FV_LIWU_tot_in,
           'Total_Out':FV_LIWU_tot_out,
           'Unit':"m3/s"
           }
df = df.append(LIWrow, ignore_index=True)

df.to_excel('Flux_computing.xlsx', index = False)
