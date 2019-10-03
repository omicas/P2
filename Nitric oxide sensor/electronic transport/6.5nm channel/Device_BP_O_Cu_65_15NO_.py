# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Two-probe Configuration
# -------------------------------------------------------------

VG=["-0.5"]
for vg in VG:
  device_configuration=nlread('Device_BP_O_Cu_65_15NO_%s.nc'%vg, DeviceConfiguration)[-1]

# -------------------------------------------------------------
# IV Curve
# -------------------------------------------------------------
  biases = [0.000000, 0.200000, 0.400000, 0.600000, 0.800000, 1.000000,
          1.200000, 1.400000, 1.600000, 1.800000, 2.000000]*Volt

  kpoint_grid = MonkhorstPackGrid()

  iv_curve = IVCurve(
    configuration=device_configuration,
    biases=biases,
    energies=numpy.linspace(-1,1,101)*eV,
    kpoints=kpoint_grid,
    self_energy_calculator=RecursionSelfEnergy(),
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    selfconsistent_configurations_filename_prefix=NoCheckpointHandler,
    log_filename_prefix=None
    )
  nlsave('Device_BP_O_Cu_65_15NO_%s.nc'%vg, iv_curve)
  nlprint(iv_curve)

  biases = [-0.200000, -0.400000, -0.600000, -0.800000, -1.000000,
          -1.200000, -1.400000, -1.600000, -1.800000, -2.000000]*Volt

  kpoint_grid = MonkhorstPackGrid()

  iv_curve = IVCurve(
    configuration=device_configuration,
    biases=biases,
    energies=numpy.linspace(-1,1,101)*eV,
    kpoints=kpoint_grid,
    self_energy_calculator=RecursionSelfEnergy(),
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    selfconsistent_configurations_filename_prefix=NoCheckpointHandler,
    log_filename_prefix=None
    )
  nlsave('Device_BP_O_Cu_65_15NO_%s.nc'%vg, iv_curve)
  nlprint(iv_curve)
