# -*- coding: utf-8 -*-
VG=numpy.linspace(0,1,11)
#systems=['_60','-PBA_60','-PBA-1UDP_60','-PBA-2UDP_60']
#systems=['_60','-PBA_60','-PBA-1UDP_60']
systems=['_60','-PBA_60']
for index_s, s in enumerate(systems):
 current=[]
 for index_vg, vg in enumerate(VG):
  iv=nlread('Device_17-10AGNR%s_%s.nc'%(s,vg), IVCurve)[-1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    current.append(currents[i])
 numpy.savetxt('Device_17-10AGNR%s_IVcomp.txt'%(s),(current))

VG=[0.0,0.1,0.2,0.3,0.399,0.5,0.6,0.7,0.8,0.9,1.0]
systems=['-PBA-1UDP_60']
for index_s, s in enumerate(systems):
 current=[]
 for index_vg, vg in enumerate(VG):
  iv=nlread('Device_17-10AGNR%s_%s.nc'%(s,vg), IVCurve)[-1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    current.append(currents[i])
 numpy.savetxt('Device_17-10AGNR%s_IVcomp.txt'%(s),(current))
VG=[0.0,0.11,0.21,0.31,0.41,0.51,0.61,0.71,0.81,0.9,1.0]
systems=['-PBA-2UDP_60']
for index_s, s in enumerate(systems):
 current=[]
 for index_vg, vg in enumerate(VG):
  iv=nlread('Device_17-10AGNR%s_%s.nc'%(s,vg), IVCurve)[-1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    current.append(currents[i])
 numpy.savetxt('Device_17-10AGNR%s_IVcomp.txt'%(s),(current))

VG=[0.001,0.099,0.199,0.301,0.4,0.5,0.61,0.7,0.8,0.91,1.0]
systems=['-PBA-3UDP_60']
for index_s, s in enumerate(systems):
 current=[]
 for index_vg, vg in enumerate(VG):
  iv=nlread('Device_17-10AGNR%s_%s.nc'%(s,vg), IVCurve)[-1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    current.append(currents[i])
 numpy.savetxt('Device_17-10AGNR%s_IVcomp.txt'%(s),(current))

