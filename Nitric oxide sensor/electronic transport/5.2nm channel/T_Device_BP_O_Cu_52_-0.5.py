# -*- coding: utf-8 -*-
prefix=["","_1NO","_5NO","_10NO","_15NO"]
VG=[-0.5]
T=numpy.linspace(250,350,3)
G=numpy.zeros((len(prefix),len(T)))
for index_pref, pref in enumerate(prefix):
 for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_52%s_%s.nc'%(pref,vg), TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G[index_pref,index_t]=conductance
    if ( processIsMaster() ):
      print "Device_BP_O_Cu_52%s:"%pref
      print "Gate voltage = %s: Conductance = %s at T = %s"%(vg,conductance,temperature)
      print "Gate voltage = %s: Current = %s at T = %s"%(vg,current,temperature)

numpy.savetxt('Device_BP_O_Cu_52_G_%s.txt'%VG[0],G)

import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':','-', '--', '-.', ':','-', '--', '-.', ':']
my_xticks = ["0NO","1NO","5NO","10NO","15NO"]
x = numpy.array([0,1,5,10,15])
plt.xticks(x, my_xticks)

for i, temp in enumerate(T):
#  plt.plot(x,G[:,i], linestyle=linestyles[i],linewidth=2, marker='o', label='T = %sK'%temp)
  plt.semilogy(x,G[:,i], linestyle=linestyles[i],linewidth=2, marker='o', label='T = %sK'%temp)

plt.xlabel('')
plt.ylabel('Conductance (S)')
plt.legend(loc=0)
plt.show()
