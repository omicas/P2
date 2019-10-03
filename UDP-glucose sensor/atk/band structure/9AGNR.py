# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 35.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258000006]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.246272727058,  0.394528498124,  0.166666666663],
                          [ 0.246272727058,  0.464842832707,  0.166666666663],
                          [ 0.246272727058,  0.535157167293,  0.166666666663],
                          [ 0.246272727058,  0.605471501876,  0.166666666663],
                          [ 0.246272727058,  0.332400827334,  0.205476504614],
                          [ 0.246272727058,  0.667599172666,  0.205476504614],
                          [ 0.246272727058,  0.359371330832,  0.333333333323],
                          [ 0.246272727058,  0.429685665416,  0.333333333323],
                          [ 0.246272727058,  0.500000000001,  0.333333333323],
                          [ 0.246272727058,  0.570314334584,  0.333333333323],
                          [ 0.246272727058,  0.640628669168,  0.333333333323],
                          [ 0.246272727058,  0.359371330832,  0.666666666644],
                          [ 0.246272727058,  0.429685665416,  0.666666666644],
                          [ 0.246272727058,  0.500000000001,  0.666666666644],
                          [ 0.246272727058,  0.570314334584,  0.666666666644],
                          [ 0.246272727058,  0.640628669168,  0.666666666644],
                          [ 0.246272727058,  0.332400827334,  0.794523495386],
                          [ 0.246272727058,  0.667599172666,  0.794523495386],
                          [ 0.246272727058,  0.394528498124,  0.833333333337],
                          [ 0.246272727058,  0.464842832707,  0.833333333337],
                          [ 0.246272727058,  0.535157167293,  0.833333333337],
                          [ 0.246272727058,  0.605471501876,  0.833333333337]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
basis_set = DFTBDirectory("cp2k/scc/")

#----------------------------------------
# Pair Potentials
#----------------------------------------
pair_potentials = DFTBDirectory("cp2k/scc/")

k_point_sampling = MonkhorstPackGrid(
    nc=101,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=k_point_sampling,
    )

iteration_control_parameters = IterationControlParameters()

calculator = SlaterKosterCalculator(
    basis_set=basis_set,
    pair_potentials=pair_potentials,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('9AGNR.nc', bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['G', 'Z', 'G'],
    points_per_segment=50,
    bands_above_fermi_level=All
    )
nlsave('9AGNR.nc', bandstructure)