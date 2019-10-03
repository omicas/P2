# -*- coding: utf-8 -*-
VG=numpy.linspace(-2,2,9)
for index_vg, vg in enumerate(VG):
  bias=[]
  current=[]
  iv=nlread('Device_17-10AGNR-PBA_60_%s.nc'%vg, IVCurve)[1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[-(i+1)])
    current.append(currents[-(i+1)])
  #bias=iv.biases()
  #current=iv.currents()
  #numpy.savetxt('Device_17-10AGNR-PBA_60_%s_IV.txt'%vg,(bias,current))
  iv=nlread('Device_17-10AGNR-PBA_60_%s.nc'%vg, IVCurve)[0]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[i])
    current.append(currents[i])
  numpy.savetxt('Device_17-10AGNR-PBA_60_%s_IV.txt'%vg,(bias,current))

current=[]
for index_vg, vg in enumerate(VG):
  iv=nlread('Device_17-10AGNR-PBA_60_%s.nc'%vg, IVCurve)[0]
  currents=numpy.ravel(iv.currents())
  current.append(currents[5])

dI = numpy.zeros(len(current),numpy.float)
dI[0:-1] = numpy.diff(current)/numpy.diff(VG)
dI[-1] = (current[-1] - current[-2])/(VG[-1] - VG[-2])
numpy.savetxt('Device_17-10AGNR-PBA_60_dIdV.txt',(VG,dI))
