# Master-s-degree-internship
Python codes created or adapted during my internship (CEREGE)

Box model v5 reads the flux and initial oxygen concentrations in the provided table.xlsx depending on a chosen experiment. 

  The model computes oxygen concentration in the 4 investigated boxes (WMIW, WMDW, EMIW, EMDW). O2 consumption is calculated using simple kinetic equation depending on O2 concentration.
  Turbulent mixing is also calculated between superimposed boxes. 

  Results of the simulation are ploted at the end of the experiment. The plot also shows the volume of each box to verify the viability of the simulation.
  Then, table containing box volume, oxygen concentration and oxygen consumption is exported as loop.xlsx file.


Flux_computing reads ORCM NEMOMED8 outputs estimates water flux through defined sections.
Flux_computing counting Aegean estimate flux on angled transects. The exported file provides water fluxes but does not take angle into account. It was chosen on purpose to verify the flux.
