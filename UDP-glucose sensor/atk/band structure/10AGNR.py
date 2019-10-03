# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 41.0745, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5           ,  0.365189987742,  0.666666666667],
                          [ 0.5           ,  0.395147768244,  0.833333333333],
                          [ 0.5           ,  0.365189987742,  0.333333333333],
                          [ 0.5           ,  0.425105548746,  0.666666666667],
                          [ 0.5           ,  0.455063329247,  0.833333333333],
                          [ 0.5           ,  0.395147768244,  0.166666666667],
                          [ 0.5           ,  0.425105548746,  0.333333333333],
                          [ 0.5           ,  0.485021109749,  0.666666666667],
                          [ 0.5           ,  0.514978890251,  0.833333333333],
                          [ 0.5           ,  0.455063329247,  0.166666666667],
                          [ 0.5           ,  0.485021109749,  0.333333333333],
                          [ 0.5           ,  0.544936670753,  0.666666666667],
                          [ 0.5           ,  0.574894451254,  0.833333333333],
                          [ 0.5           ,  0.514978890251,  0.166666666667],
                          [ 0.5           ,  0.544936670753,  0.333333333333],
                          [ 0.5           ,  0.604852231756,  0.666666666667],
                          [ 0.5           ,  0.634810012258,  0.833333333333],
                          [ 0.5           ,  0.574894451254,  0.166666666667],
                          [ 0.5           ,  0.604852231756,  0.333333333333],
                          [ 0.5           ,  0.634810012258,  0.166666666667],
                          [ 0.5           ,  0.342208146882,  0.794523495372],
                          [ 0.5           ,  0.342208146882,  0.205476504628],
                          [ 0.5           ,  0.657791853118,  0.705476504628],
                          [ 0.5           ,  0.657791853118,  0.294523495372]]


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
nlsave('10AGNR.nc', bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['G', 'Z', 'G'],
    points_per_segment=50,
    bands_above_fermi_level=All
    )
nlsave('10AGNR.nc', bandstructure)