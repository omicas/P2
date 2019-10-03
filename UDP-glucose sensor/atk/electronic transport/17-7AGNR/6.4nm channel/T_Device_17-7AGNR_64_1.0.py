# -*- coding: utf-8 -*-
prefix=["","-PBA-1UDP","-PBA-2UDP","-PBA-3UDP"]
VG=[1.0]
T=numpy.linspace(250,350,3)
G=numpy.zeros((len(prefix),len(T)))
for index_pref, pref in enumerate(prefix):
 for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_17-7AGNR%s_64_%s.nc'%(pref,vg), TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G[index_pref,index_t]=conductance
    if ( processIsMaster() ):
      print "Device_17-7AGNR%s:"%pref
      print "Gate voltage = %s: Conductance = %s at T = %s"%(vg,conductance,temperature)
      print "Gate voltage = %s: Current = %s at T = %s"%(vg,current,temperature)

numpy.savetxt('Device_17-7AGNR_64_G_%s.txt'%VG[0],G)

import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':','-', '--', '-.', ':','-', '--', '-.', ':']
my_xticks = ["0UDP","1UDP","2UDP","3UDP"]
x = numpy.array([0,1,2,3])
plt.xticks(x, my_xticks)

for i, temp in enumerate(T):
  plt.plot(x,G[:,i], linestyle=linestyles[i],linewidth=2, marker='o', label='T = %sK'%temp)
#  plt.semilogy(x,G[:,i], linestyle=linestyles[i],linewidth=2, marker='o', label='T = %sK'%temp)

plt.xlabel('')
plt.ylabel('Conductance (S)')
plt.legend(loc=0)
plt.show()
