# -*- coding: utf-8 -*-
VG=numpy.linspace(-2,2,9)
for index_vg, vg in enumerate(VG):
  iv=nlread('Device_11-9AGNR_30_%s.nc'%vg, IVCurve)[0]
  bias=iv.biases()
  current=iv.currents()
  numpy.savetxt('Device_11-9AGNR_30_%s_IV.txt'%vg,(bias,current))
