# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 42.6659, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5           ,  0.269276943841,  0.666666666667],
                          [ 0.5           ,  0.298117325861,  0.833333333333],
                          [ 0.5           ,  0.269276943841,  0.333333333333],
                          [ 0.5           ,  0.326957707881,  0.666666666667],
                          [ 0.5           ,  0.355798089901,  0.833333333333],
                          [ 0.5           ,  0.298117325861,  0.166666666667],
                          [ 0.5           ,  0.326957707881,  0.333333333333],
                          [ 0.5           ,  0.384638471921,  0.666666666667],
                          [ 0.5           ,  0.41347885394 ,  0.833333333333],
                          [ 0.5           ,  0.355798089901,  0.166666666667],
                          [ 0.5           ,  0.384638471921,  0.333333333333],
                          [ 0.5           ,  0.44231923596 ,  0.666666666667],
                          [ 0.5           ,  0.47115961798 ,  0.833333333333],
                          [ 0.5           ,  0.41347885394 ,  0.166666666667],
                          [ 0.5           ,  0.44231923596 ,  0.333333333333],
                          [ 0.5           ,  0.5           ,  0.666666666667],
                          [ 0.5           ,  0.52884038202 ,  0.833333333333],
                          [ 0.5           ,  0.47115961798 ,  0.166666666667],
                          [ 0.5           ,  0.5           ,  0.333333333333],
                          [ 0.5           ,  0.55768076404 ,  0.666666666667],
                          [ 0.5           ,  0.58652114606 ,  0.833333333333],
                          [ 0.5           ,  0.52884038202 ,  0.166666666667],
                          [ 0.5           ,  0.55768076404 ,  0.333333333333],
                          [ 0.5           ,  0.615361528079,  0.666666666667],
                          [ 0.5           ,  0.644201910099,  0.833333333333],
                          [ 0.5           ,  0.58652114606 ,  0.166666666667],
                          [ 0.5           ,  0.615361528079,  0.333333333333],
                          [ 0.5           ,  0.673042292119,  0.666666666667],
                          [ 0.5           ,  0.701882674139,  0.833333333333],
                          [ 0.5           ,  0.644201910099,  0.166666666667],
                          [ 0.5           ,  0.673042292119,  0.333333333333],
                          [ 0.5           ,  0.730723056159,  0.666666666667],
                          [ 0.5           ,  0.701882674139,  0.166666666667],
                          [ 0.5           ,  0.730723056159,  0.333333333333],
                          [ 0.5           ,  0.247152305139,  0.794523495372],
                          [ 0.5           ,  0.247152305139,  0.205476504628],
                          [ 0.5           ,  0.752847694861,  0.794523495372],
                          [ 0.5           ,  0.752847694861,  0.205476504628]]

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
nlsave('17AGNR.nc', bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['G', 'Z', 'G'],
    points_per_segment=50,
    bands_above_fermi_level=All
    )
nlsave('17AGNR.nc', bandstructure)
