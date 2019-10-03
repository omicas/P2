import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':','-', '--', '-.', ':','-', '--', '-.', ':']

VG=numpy.linspace(-2,2,9)
#VG=[-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5]
T=numpy.linspace(100,1100,101)
G=numpy.zeros((len(VG),len(T)))
for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_52_%s.nc'%vg, TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G[index_vg,index_t]=conductance
  plt.semilogy(T,G[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)

numpy.savetxt('Device_BP_O_Cu_52_G.txt',G)

plt.xlabel('T (K)')
plt.ylabel('G (S)')
plt.legend(loc=0)

plt.figure()
plt.semilogy(VG,G[:,15], linestyle=linestyles[0],linewidth=2, label='T = %s K'%T[15])
plt.semilogy(VG,G[:,20], linestyle=linestyles[1],linewidth=2, label='T = %s K'%T[20])
plt.semilogy(VG,G[:,25], linestyle=linestyles[2],linewidth=2, label='T = %s K'%T[25])
plt.xlabel('V_G (V)')
plt.ylabel('G (S)')
plt.legend(loc=0)

plt.show()
