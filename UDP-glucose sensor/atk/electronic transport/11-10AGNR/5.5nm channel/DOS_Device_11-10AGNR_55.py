# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Analysis from File
# -------------------------------------------------------------
path = u'/Users/PH1/Documents/Juan/atk/Sensor/Device_11-10AGNR_55_0.0.nc'
configuration = nlread(path, object_id='gID000')[0]

# -------------------------------------------------------------
# Electrostatic Difference Potential
# -------------------------------------------------------------
electrostatic_difference_potential = ElectrostaticDifferencePotential(configuration)
nlsave('Device_11-10AGNR_55_0.0.nc', electrostatic_difference_potential)

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
nlsave('Device_11-10AGNR_55_0.0.nc', projected_local_density_of_states)

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
nlsave('Device_11-10AGNR_55_0.0.nc', device_density_of_states)
nlprint(device_density_of_states)