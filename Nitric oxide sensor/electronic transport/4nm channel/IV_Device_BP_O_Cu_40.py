# -*- coding: utf-8 -*-
VG=[-2.0,0.5]
for index_vg, vg in enumerate(VG):
  bias=[]
  current=[]
  iv=nlread('Device_BP_O_Cu_40_%s.nc'%vg, IVCurve)[1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[-(i+1)])
    current.append(currents[-(i+1)])
  iv=nlread('Device_BP_O_Cu_40_%s.nc'%vg, IVCurve)[0]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[i])
    current.append(currents[i])
  numpy.savetxt('Device_BP_O_Cu_40_%s_IV.txt'%vg,(bias,current))

#VG=[0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.4,1.5]
#current=[]
#for index_vg, vg in enumerate(VG):
#  iv=nlread('Device_BP_O_Cu_40_%s.nc'%vg, IVCurve)[-1]
#  current.append(numpy.ravel(iv.currents()))
#numpy.savetxt('Device_BP_O_Cu_40_IV.txt',(VG,current))

