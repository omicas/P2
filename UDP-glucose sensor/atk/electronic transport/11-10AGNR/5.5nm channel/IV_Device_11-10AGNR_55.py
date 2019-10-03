# -*- coding: utf-8 -*-
VG=numpy.linspace(-2,2,9)
for index_vg, vg in enumerate(VG):
  bias=[]
  current=[]
  iv=nlread('Device_11-10AGNR_55_%s.nc'%vg, IVCurve)[1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[-(i+1)])
    current.append(currents[-(i+1)])
  #bias=iv.biases()
  #current=iv.currents()
  #numpy.savetxt('Device_11-10AGNR_55_%s_IV.txt'%vg,(bias,current))
  iv=nlread('Device_11-10AGNR_55_%s.nc'%vg, IVCurve)[0]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[i])
    current.append(currents[i])
  numpy.savetxt('Device_11-10AGNR_55_%s_IV.txt'%vg,(bias,current))