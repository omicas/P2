# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Analysis from File
# -------------------------------------------------------------
#VG=numpy.linspace(-2,2,9)
VG=[0.5]
for vg in VG:
  path = u'Device_BP_O_Cu_40_%s.nc'%vg
  configuration = nlread(path, object_id='gID000')[0]

  # -------------------------------------------------------------
  # Electrostatic Difference Potential
  # -------------------------------------------------------------
  electrostatic_difference_potential = ElectrostaticDifferencePotential(configuration)
  nlsave('Device_BP_O_Cu_40_%s.nc'%vg, electrostatic_difference_potential)

  # -------------------------------------------------------------
  # Projected Local Density Of States
  # -------------------------------------------------------------
  kpoint_grid = MonkhorstPackGrid()

  projected_local_density_of_states = ProjectedLocalDensityOfStates(
    configuration=configuration,
    method=LocalDeviceDensityOfStates,
    energies=numpy.linspace(-2, 2, 101)*eV,
    kpoints=kpoint_grid,
    contributions=All,
    self_energy_calculator=RecursionSelfEnergy(),
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    )
  nlsave('Device_BP_O_Cu_40_%s.nc'%vg, projected_local_density_of_states)

  # -------------------------------------------------------------
  # Device Density Of States
  # -------------------------------------------------------------
  kpoint_grid = MonkhorstPackGrid()

  device_density_of_states = DeviceDensityOfStates(
    configuration=configuration,
    energies=numpy.linspace(-2,2,101)*eV,
    kpoints=kpoint_grid,
    contributions=All,
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    self_energy_calculator=RecursionSelfEnergy(),
    )
  nlsave('Device_BP_O_Cu_40_%s.nc'%vg, device_density_of_states)
  nlprint(device_density_of_states)
