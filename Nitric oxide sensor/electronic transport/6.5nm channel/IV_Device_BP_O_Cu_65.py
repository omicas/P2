# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':','-', '--', '-.', ':','-', '--', '-.', ':']

VG=[-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5]
for index_vg, vg in enumerate(VG):
  bias=[]
  current=[]
  iv=nlread('Device_BP_O_Cu_65_%s.nc'%vg, IVCurve)[1]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[-(i+1)])
    current.append(currents[-(i+1)])
  iv=nlread('Device_BP_O_Cu_65_%s.nc'%vg, IVCurve)[0]
  biases=numpy.ravel(iv.biases())
  currents=numpy.ravel(iv.currents())
  for i,b in enumerate(biases):
    bias.append(biases[i])
    current.append(currents[i])
  numpy.savetxt('Device_BP_O_Cu_65_%s_IV.txt'%vg,(bias,current))
  plt.plot(bias,current, linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)

plt.xlabel('V_DS (V)')
plt.ylabel('I_DS (A)')
#plt.xlim([-1.8,1.8])
plt.legend(loc=0)
plt.show()

#VG=[0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.4,1.5]
#current=[]
#for index_vg, vg in enumerate(VG):
#  iv=nlread('Device_BP_O_Cu_40_%s.nc'%vg, IVCurve)[-1]
#  current.append(numpy.ravel(iv.currents()))
#numpy.savetxt('Device_BP_O_Cu_40_IV.txt',(VG,current))

