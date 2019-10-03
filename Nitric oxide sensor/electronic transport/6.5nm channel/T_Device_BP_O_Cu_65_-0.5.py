# -*- coding: utf-8 -*-
#NO
prefix=["","_1NO","_5NO","_10NO","_15NO","_20NO"]
VG=[-0.5]
T=numpy.linspace(250,350,3)
G=numpy.zeros((len(prefix),len(T)))
for index_pref, pref in enumerate(prefix):
 for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_65%s_%s.nc'%(pref,vg), TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G[index_pref,index_t]=conductance
    if ( processIsMaster() ):
      print "Device_BP_O_Cu_65%s:"%pref
      print "Gate voltage = %s: Conductance = %s at T = %s"%(vg,conductance,temperature)
      print "Gate voltage = %s: Current = %s at T = %s"%(vg,current,temperature)

numpy.savetxt('Device_BP_O_Cu_65_G_NO_%s.txt'%VG[0],G)

import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':','-', '--', '-.', ':','-', '--', '-.', ':']
my_xticks = ["0NO","1NO","5NO","10NO","15NO","20NO"]
x = numpy.array([0,1,5,10,15,20])
plt.xticks(x, my_xticks)

for i, temp in enumerate(T):
#  plt.plot(x,G[:,i], linestyle=linestyles[i],linewidth=2, marker='o', label='T = %sK'%temp)
  plt.semilogy(x,G[:,i], linestyle=linestyles[i],linewidth=2, marker='o', label='T = %sK'%temp)

plt.xlabel('')
plt.ylabel('Conductance (S)')
plt.legend(loc=0)

#CO
plt.figure()
prefix=["","_1CO","_10CO","_15CO","_20CO"]
VG=[-0.5]
T=numpy.linspace(250,350,3)
G=numpy.zeros((len(prefix),len(T)))
for index_pref, pref in enumerate(prefix):
 for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_65%s_%s.nc'%(pref,vg), TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G[index_pref,index_t]=conductance
    if ( processIsMaster() ):
      print "Device_BP_O_Cu_65%s:"%pref
      print "Gate voltage = %s: Conductance = %s at T = %s"%(vg,conductance,temperature)
      print "Gate voltage = %s: Current = %s at T = %s"%(vg,current,temperature)

numpy.savetxt('Device_BP_O_Cu_65_G_CO_%s.txt'%VG[0],G)

import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':','-', '--', '-.', ':','-', '--', '-.', ':']
my_xticks = ["0CO","1CO","10CO","15CO","20CO"]
x = numpy.array([0,1,10,15,20])
plt.xticks(x, my_xticks)

for i, temp in enumerate(T):
  plt.semilogy(x,G[:,i], linestyle=linestyles[i],linewidth=2, marker='o', label='T = %sK'%temp)

plt.xlabel('')
plt.ylabel('Conductance (S)')
plt.legend(loc=0)

#OH
plt.figure()
prefix=["","_1OH","_10OH","_15OH","_20OH"]
VG=[-0.5]
T=numpy.linspace(250,350,3)
G=numpy.zeros((len(prefix),len(T)))
for index_pref, pref in enumerate(prefix):
 for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_65%s_%s.nc'%(pref,vg), TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G[index_pref,index_t]=conductance
    if ( processIsMaster() ):
      print "Device_BP_O_Cu_65%s:"%pref
      print "Gate voltage = %s: Conductance = %s at T = %s"%(vg,conductance,temperature)
      print "Gate voltage = %s: Current = %s at T = %s"%(vg,current,temperature)

numpy.savetxt('Device_BP_O_Cu_65_G_OH_%s.txt'%VG[0],G)

import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':','-', '--', '-.', ':','-', '--', '-.', ':']
my_xticks = ["0OH","1OH","10OH","15OH","20OH"]
x = numpy.array([0,1,10,15,20])
plt.xticks(x, my_xticks)

for i, temp in enumerate(T):
  plt.semilogy(x,G[:,i], linestyle=linestyles[i],linewidth=2, marker='o', label='T = %sK'%temp)

plt.xlabel('')
plt.ylabel('Conductance (S)')
plt.legend(loc=0)

plt.show()

