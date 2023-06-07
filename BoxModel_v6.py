#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Starting Model
year = 0           #start
step = 1           #step of iterations
time = 6100          #number of years simulated
scene = "Post_S1" #choosing scenario and flux from excel file : Pre_EMT, 1987_1992, 1992_1994, 1994_2002, 2004_2006, Post_2006, Weaker_THC, Weaker_WMS_Stronger_EMS, Stronger_THC, EHOL1, EHOL2, EHOL_KT1, EHOL_KT2, 9k1, 9k2, Post_S1
sec_step = step * (60*60*24*365) #Definition of step in seconds from step in year
Ks = 6.25 * 0.001 #Definition of O2 half concentration saturation µmol/L => Used in O2 consumption equation
KDOC = 4.16 * 0.001 #Definition of DOC half concentration saturation µmol/L => Used in O2 consumption equation #2
KDOCeq = ( KDOC * 172 ) / 122 #Conversion of DOC half saturation to O2 half saturation using molar ration O2:C = 172:122 (Takahashi85)
flux = pd.read_excel(r'boxmodel_flux_input.xlsx')
oxygen = pd.read_excel(r'boxmodel_oxygen_input.xlsx')

FmaxEMIW = 1699 *2 #+ 253.3
FmaxEMDW = 503 *2 #+ 50.3
FmaxWMIW = 749 *2 #+ 111.6
FmaxWMDW = 665 *2 #+ 66.5

Kz1 = 2.3e-4  #EMSIW effective diffusion coeff in m2/s
Kz2 = 1e-7  #EMIDW effective diffusion coeff in m2/s
Kz3 = 1.2e-4  #WMSIW effective diffusion coeff in m2/s
Kz4 = 1e-7  #WMIDW effective diffusion coeff in m2/s

#######################
##Definition of Boxes##
#######################

#Western Mediterranean Basin
WMSS = 815e9 #m2  => WMS surface area
    #Volume
WMSW = 1.63e14 #m3
WMIW = 3.26e14 #m3
WMDW = 9.08e14 #m3
    #Oxygenation
Ox_WMSW = oxygen.iloc[0][scene] #233 * 0.001 #µmol/L to mol/m3 and fixed
Ox_WMIW = oxygen.iloc[1][scene] #0.194980296550192 #195 * 0.001 #µmol/L to mol/m3
Ox_WMDW = oxygen.iloc[2][scene] #0.199000051349724 #199 * 0.001 #µmol/L to mol/m3
Ox_WMIW2 = oxygen.iloc[1][scene] #0.194980296550192 #195 * 0.001 #µmol/L to mol/m3
Ox_WMDW2 = oxygen.iloc[2][scene] #0.199000051349724 #199 * 0.001 #µmol/L to mol/m3
Ox_AdAeg = oxygen.iloc[6][scene] #230 * 0.001 #µmol/L to mol/m3

#Eastern Mediterranean Basin
EMSS = 1336e9 #m2  => WMS surface area
    #Volume
EMSW = 2.8e14 #m3
EMIW = 4e14 #m3
EMIW2 = 4e14 #m3
EMDW = 17e14 #m3
EMDW2 = 17e14 #m3
    #Oxygenation
Ox_EMSW = oxygen.iloc[3][scene] #229 * 0.001 #µmol/L to mol/m3 and fixed
Ox_EMIW = oxygen.iloc[4][scene] #0.19886484905295 #204 * 0.001 #µmol/L to mol/m3
Ox_EMIW2 = oxygen.iloc[4][scene] #0.19886484905295 #204 * 0.001 #µmol/L to mol/m3
Ox_EMDW = oxygen.iloc[5][scene] #0.187212272514579 #187 * 0.001 #µmol/L to mol/m3
Ox_EMDW2 = oxygen.iloc[5][scene] #0.187212272514579 #187 * 0.001 #µmol/L to mol/m3

##############################
##Definition of water fluxes##
##############################

#Gibraltar Strait
FG1 = flux.iloc[1][scene] *1e6*sec_step #0.83 * G_factor *10e6*sec_step   #Sv = 10^6 m^3/s => Entrance
FG2 = flux.iloc[2][scene] *1e6*sec_step #0.47 * G_factor *10e6*sec_step  #Sv = 10^6 m^3/s => WMIW leaving
FG3 = flux.iloc[3][scene] *1e6*sec_step #0.31 * G_factor *10e6*sec_step  #Sv = 10^6 m^3/s => WMDW leaving

#Western Basin
F1E = flux.iloc[0][scene] *1e6*sec_step #0.01 *10e6*sec_step #Evaporation => different from original model to avoid disequilibrium
F14 = flux.iloc[11][scene] *1e6*sec_step #1.14 *10e6*sec_step #WMSW to EMSW
F23 = flux.iloc[9][scene] *1e6*sec_step #0.07 *10e6*sec_step #WMIW to WMDW represents the formation of Tyr deep water
F73 = flux.iloc[8][scene] *1e6*sec_step #0.61 * WMDW_factor *10e6*sec_step #NWM to WMDW

#Eastern Basin
F4E = flux.iloc[13][scene] *1e6*sec_step #0.06 *10e6*sec_step #Evaporation
F45 = flux.iloc[15][scene] *1e6*sec_step #1.10 * EMIW_factor *10e6*sec_step #EMSW to EMIW
F58 = flux.iloc[16][scene] *1e6*sec_step #0.36 *10e6*sec_step #EMIW to Adriatic and Aegean
F84 = flux.iloc[14][scene] *1e6*sec_step #0.02 *10e6*sec_step #Adriatic and Aegean to EMSW
F86 = flux.iloc[18][scene] *1e6*sec_step #0.36 *10e6*sec_step*EMDW_factor #Adriatic and Aegean to EMDW
F65 = F86 #EWDW to EMIW => Offset to maintain water balance
F52 = flux.iloc[12][scene] *1e6*sec_step #1.10 * EMIW_factor *10e6 * sec_step #EMIW to WMIW

    #Deduction of Western flux from others
F17 = flux.iloc[5][scene] *1e6*sec_step #0.38 * F73 #WMSF to NWM as a % of DW formation
F27 = flux.iloc[6][scene] *1e6*sec_step #0.62 * F73 #WMIW to NWM as a % of DW formation
F32 = flux.iloc[10][scene] *1e6*sec_step #F23 + F73 - FG3 #WMDW to WMIW => Upwelling deduced from stationnary state
F21 = flux.iloc[4][scene] *1e6*sec_step #F52 + F32 - F27 - FG2 - F23 #WMIW to WMSW => Upwelling deduced from stationnary state

    #Adding potential future flux
F72 = flux.iloc[7][scene] *1e6*sec_step
F85 = flux.iloc[17][scene] *1e6*sec_step

################################################
##Creation of dataframe and initial conditions##
################################################

initial_conditions = ({
    'Year_simulated':[0],
    'Oxygen_WMSW_molm3': [Ox_WMSW],
    'Oxygen_WMIW_molm3': [Ox_WMIW],
    'Oxygen_WMDW_molm3': [Ox_WMDW],
    'Oxygen_EMSW_molm3': [Ox_EMSW],
    'Oxygen_EMIW_molm3': [Ox_EMIW],
    'Oxygen_EMDW_molm3': [Ox_EMDW],
    'WMSW': [WMSW],
    'WMIW': [WMIW],
    'WMDW': [WMDW],
    'EMSW': [EMSW],
    'EMIW': [EMIW],
    'EMDW': [EMDW],
               })
df = pd.DataFrame(initial_conditions)

#################
##Starting Loop##
#################

year=year+step #Increase to avoid changing initial conditions

while year <=time:  #Modeling "year" until "time" is over

    Ox_EMIW = Ox_EMIW2
    Ox_EMDW = Ox_EMDW2
    Ox_WMIW = Ox_WMIW2
    Ox_WMDW = Ox_WMDW2

    #Calculate new parameters based on last iteration
                #Volumes
    WMSW = WMSW - F1E - F14 - F17 + F21 + FG1
    WMIW = WMIW - F21 - F23 - FG2 - F27 + F32 + F52 + F72
    WMDW = WMDW - F32 - FG3 + F73 + F23
    EMSW = EMSW - F4E - F45 + F84 + F14
    EMIW = EMIW + F45 + F65 - F58 - F52 + F85
    EMDW = EMDW - F65 + F86

               #Oxygen consumption expressed in mol/timestep
    Ox_cons_EMIW =( FmaxEMIW * 1e9 * (Ox_EMIW / (Ox_EMIW + Ks)) )* step #1699e9 * (Ox_EMIW / (Ox_EMIW + Ks)) * step
    Ox_cons_EMDW = FmaxEMDW * 1e9 * (Ox_EMDW / (Ox_EMDW + Ks)) * step #( ((3259e9 * (0.4e-3/((0.4e-3) + KDOCeq))) + 295e9) * (Ox_EMDW / (Ox_EMDW + Ks)) ) * step
    Ox_cons_WMIW =( FmaxWMIW * 1e9 * (Ox_WMIW / (Ox_WMIW + Ks)) )* step #649e9 * (Ox_WMIW / (Ox_WMIW + Ks)) * step
    Ox_cons_WMDW = FmaxWMDW * 1e9 * (Ox_WMDW / (Ox_WMDW + Ks)) * step #( ((1988e9 * (2.09e-3/((2.09e-3) + KDOCeq))) + 144e9) * (Ox_WMDW / (Ox_WMDW + Ks)) ) * step

                #Oxygen flux expressed in mol/time step
    Ox_F52 = Ox_EMIW * F52  #Definition of O2 flux for step : EMIW to WMIW
    Ox_F45 = Ox_EMSW * F45  #Definition of O2 flux for step : EMSW to EMIW
    Ox_F65 = Ox_EMDW * F65  #Definition of O2 flux for step : EMSW to EMIW
    Ox_F58 = Ox_EMIW * F58  #Definition of O2 flux for step : EMSW to EMIW
    Ox_F86 = Ox_AdAeg * F86
    Ox_F32 = Ox_WMDW * F32
    Ox_F23 = Ox_WMIW * F23
    Ox_FG2 = Ox_WMIW * FG2
    Ox_F27 = Ox_WMIW * F27
    Ox_F73 = Ox_WMSW * F73
    Ox_FG3 = Ox_WMDW * FG3
    Ox_F21 = Ox_WMIW * F21
    Ox_F72 = Ox_WMSW * F72
    Ox_F85 = Ox_AdAeg * F85

              #Turbulent oxygen flux expressed in mol/time step
    F45_Turb = Kz1 * ((Ox_EMSW-Ox_EMIW)/250) * EMSS
    F56_Turb = Kz2 * ((Ox_EMIW-Ox_EMDW)/650) * EMSS
    Turb_Mix_EMIW = (-F56_Turb + F45_Turb) * sec_step
    Turb_Mix_EMDW = (F56_Turb) * sec_step

    F12_Turb = Kz3 * ((Ox_WMSW-Ox_WMIW)/300) * WMSS
    F31_Turb = Kz4 * ((Ox_WMDW-Ox_WMIW)/737.5) * WMSS
    Turb_Mix_WMIW = (F12_Turb + F31_Turb) * sec_step
    Turb_Mix_WMDW = (F31_Turb) * sec_step

                #Sum of oxygen flux for each box
    #OxF_WMSW = 0 - Ox_F1E - F14 - F17 + F21 + FG1
    OxF_WMIW = 0 - Ox_F21 - Ox_F23 - Ox_FG2 - Ox_F27 + Ox_F32 + Ox_F52 - Ox_cons_WMIW + Turb_Mix_WMIW + Ox_F72 - Turb_Mix_WMDW
    OxF_WMDW = 0 - Ox_F32 - Ox_FG3 + Ox_F73 + Ox_F23 - Ox_cons_WMDW + Turb_Mix_WMDW
    #OxF_EMSW = 0 - F4E - F45 + F84 + F14
    OxF_EMIW = 0 + Ox_F45 + Ox_F65 - Ox_F58 - Ox_F52 - Ox_cons_EMIW + Turb_Mix_EMIW + Ox_F85
    OxF_EMDW = 0 - Ox_F65 + Ox_F86 - Ox_cons_EMDW + Turb_Mix_EMDW
                #Oxygen concentration
    Ox_EMIW2 = ((Ox_EMIW * EMIW) + OxF_EMIW) / EMIW
    Ox_EMDW2 = ((Ox_EMDW * EMDW) + OxF_EMDW) / EMDW
    Ox_WMIW2 = ((Ox_WMIW * WMIW) + OxF_WMIW) / WMIW
    Ox_WMDW2 = ((Ox_WMDW * WMDW) + OxF_WMDW) / WMDW

    #Create new row using calculated parameters and integrating them to dataframe
    new_row = {'Year_simulated': year,
               'Oxygen_WMSW_molm3': Ox_WMSW,
               'Oxygen_WMIW_molm3': Ox_WMIW2,
               'Oxygen_WMDW_molm3': Ox_WMDW2,
               'Oxygen_EMSW_molm3': Ox_EMSW,
               'Oxygen_EMIW_molm3': Ox_EMIW2,
               'Oxygen_EMDW_molm3': Ox_EMDW2,
               'WMSW': WMSW,
               'WMIW': WMIW,
               'WMDW': WMDW,
               'EMSW': EMSW,
               'EMIW': EMIW,
               'EMDW': EMDW,
               'Ox_cons_EMIW': Ox_cons_EMIW,
               'Ox_cons_EMDW': Ox_cons_EMDW,
               'Ox_cons_WMIW': Ox_cons_WMIW,
               'Ox_cons_WMDW': Ox_cons_WMDW,
               'Turb_Mix_WMIW': Turb_Mix_WMIW,
               'Turb_Mix_WMDW': Turb_Mix_WMDW,
               'Turb_Mix_EMIW': Turb_Mix_EMIW,
               'Turb_Mix_EMDW': Turb_Mix_EMDW,
               'F45_Turb': F45_Turb,
               }
    df = df.append(new_row, ignore_index=True)

    #Print year in console to see the advance
    print(year)
    #Increase simulated year to go to the next
    year=year+step


#df['age'] = df.Year_simulated * 2 #adding column with calculated values

#Exportation of dataframe XLSX format
print(df)
df.to_excel('loop.xlsx', index = False)

print(flux)
flux.to_excel('fluxout.xlsx', index = True)
print(F32, FG3)

#############################
##Plot parameters to verify##
#############################

figure, (ax1, ax2) = plt.subplots(2, 1)
figure.suptitle('Intermediate and deep Mediterranean basins volume (m3) \n and respective oxygen concentration (mol/m3) \n Scenario : ' + scene )

ax1.plot(df.Year_simulated, df.WMIW, label = "WMIW")
ax1.plot(df.Year_simulated, df.WMDW, label = "WMDW")
ax1.plot(df.Year_simulated, df.EMIW, label = "EMIW")
ax1.plot(df.Year_simulated, df.EMDW, label = "EMDW")
ax1.set_ylabel('Volume (m3)')
ax1.legend()

ax2.plot(df.Year_simulated, df.Oxygen_WMIW_molm3, label = "Oxygen_WMIW_mol/m3")
ax2.plot(df.Year_simulated, df.Oxygen_WMDW_molm3, label = "Oxygen_WMDW_mol/m3")
ax2.plot(df.Year_simulated, df.Oxygen_EMIW_molm3, label = "Oxygen_EMIW_mol/m3")
ax2.plot(df.Year_simulated, df.Oxygen_EMDW_molm3, label = "Oxygen_EMDW_mol/m3")
ax2.set_ylabel('Oxygen concentration \n (mol/m3)')
plt.xlabel('Years modeled (nb)')
ax2.legend()

plt.show()