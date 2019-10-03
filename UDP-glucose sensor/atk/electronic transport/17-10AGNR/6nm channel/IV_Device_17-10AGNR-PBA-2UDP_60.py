# -*- coding: utf-8 -*-
#VG=numpy.linspace(-2,2,9)
VG=[-2.0,-1.5,-1.0,0.0,0.5,1.0]
for index_vg, vg in enumerate(VG):
  bias=[]
  current=[]
  iv=nlread('Device_17-10AGNR-PBA-2UDP_60_%s.nc'%vg, IVCurve)[1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[-(i+1)])
    current.append(currents[-(i+1)])
  #bias=iv.biases()
  #current=iv.currents()
  #numpy.savetxt('Device_17-10AGNR-PBA-2UDP_60_%s_IV.txt'%vg,(bias,current))
  iv=nlread('Device_17-10AGNR-PBA-2UDP_60_%s.nc'%vg, IVCurve)[0]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[i])
    current.append(currents[i])
  numpy.savetxt('Device_17-10AGNR-PBA-2UDP_60_%s_IV.txt'%vg,(bias,current))
