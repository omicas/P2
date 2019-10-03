# -*- coding: utf-8 -*-
VG=numpy.linspace(-2,2,9)
T=numpy.linspace(0,2000,100)
G=numpy.zeros((len(VG),len(T)))
for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_11-9AGNR_64_%s.nc'%vg, TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G[index_vg,index_t]=conductance
    if ( processIsMaster() ):
      print "Gate voltage = %s: Conductance = %s at T = %s"%(vg,conductance,temperature)
      print "Gate voltage = %s: Current = %s at T = %s"%(vg,current,temperature)

numpy.savetxt('Device_11-9AGNR_64_G_.txt',G)
