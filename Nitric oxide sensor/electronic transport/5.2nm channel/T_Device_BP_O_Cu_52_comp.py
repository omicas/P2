import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':','-', '--', '-.', ':','-', '--', '-.', ':']

#VG=numpy.linspace(-2,2,9)
VG=[-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5]
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
VG=[-2.0,-0.5,0.5]
T=numpy.linspace(100,1100,101)
G1NO=numpy.zeros((len(VG),len(T)))
for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_52_1NO_%s.nc'%vg, TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G1NO[index_vg,index_t]=conductance
#  plt.plot(T,G1NO[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)
  plt.semilogy(T,G1NO[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)

numpy.savetxt('Device_BP_O_Cu_52_1NO_G.txt',G1NO)

plt.xlabel('T (K)')
plt.ylabel('G (S)')
plt.legend(loc=0)

plt.figure()
VG=numpy.linspace(-2,2,9)
T=numpy.linspace(100,1100,101)
G5NO=numpy.zeros((len(VG),len(T)))
for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_52_5NO_%s.nc'%vg, TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G5NO[index_vg,index_t]=conductance
#  plt.plot(T,G5NO[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)
  plt.semilogy(T,G5NO[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)

numpy.savetxt('Device_BP_O_Cu_52_5NO_G.txt',G5NO)

plt.xlabel('T (K)')
plt.ylabel('G (S)')
plt.legend(loc=0)

plt.figure()
VG=[-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0]
T=numpy.linspace(100,1100,101)
G10NO=numpy.zeros((len(VG),len(T)))
for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_52_10NO_%s.nc'%vg, TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G10NO[index_vg,index_t]=conductance
#  plt.plot(T,G10NO[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)
  plt.semilogy(T,G10NO[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)

numpy.savetxt('Device_BP_O_Cu_52_10NO_G.txt',G10NO)

plt.xlabel('T (K)')
plt.ylabel('G (S)')
plt.legend(loc=0)
plt.figure()
VG=[-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0]
T=numpy.linspace(100,1100,101)
G15NO=numpy.zeros((len(VG),len(T)))
for index_vg, vg in enumerate(VG):
  transmission_spectrum=nlread('Device_BP_O_Cu_52_15NO_%s.nc'%vg, TransmissionSpectrum)[0]
  for index_t, temp in enumerate(T):
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    G15NO[index_vg,index_t]=conductance
#  plt.plot(T,G15NO[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)
  plt.semilogy(T,G15NO[index_vg,:], linestyle=linestyles[index_vg],linewidth=2, label='V_G = %s V'%vg)

numpy.savetxt('Device_BP_O_Cu_52_15NO_G.txt',G15NO)

plt.xlabel('T (K)')
plt.ylabel('G (S)')
plt.legend(loc=0)

plt.figure()
#plt.semilogy(VG,G[:,15], linestyle=linestyles[0],linewidth=2, label='T = %s K'%T[15])
#plt.semilogy(VG,G[:,20], linestyle=linestyles[1],linewidth=2, label='T = %s K'%T[20])
#plt.semilogy(VG,G[:,25], linestyle=linestyles[2],linewidth=2, label='T = %s K'%T[25])
#plt.semilogy(VG,G[:,20], linestyle=linestyles[0],linewidth=2, label='clean, T = %s K'%T[20])
#plt.semilogy(VG,G1NO[:,20], linestyle=linestyles[1],linewidth=2, label='1NO, T = %s K'%T[20])
plt.semilogy(VG,G5NO[:,20], linestyle=linestyles[1],linewidth=2, label='5NO, T = %s K'%T[20])
plt.semilogy(VG,G10NO[:,20], linestyle=linestyles[1],linewidth=2, label='10NO, T = %s K'%T[20])
plt.semilogy(VG,G15NO[:,20], linestyle=linestyles[1],linewidth=2, label='15NO, T = %s K'%T[20])
plt.xlabel('V_G (V)')
plt.ylabel('G (S)')
plt.legend(loc=0)

plt.show()
