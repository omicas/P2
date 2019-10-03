# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 40.2049, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5           ,  0.285759795782,  0.666666666667],
                          [ 0.5           ,  0.316365539242,  0.833333333333],
                          [ 0.5           ,  0.285759795782,  0.333333333333],
                          [ 0.5           ,  0.346971282702,  0.666666666667],
                          [ 0.5           ,  0.377577026161,  0.833333333333],
                          [ 0.5           ,  0.316365539242,  0.166666666667],
                          [ 0.5           ,  0.346971282702,  0.333333333333],
                          [ 0.5           ,  0.408182769621,  0.666666666667],
                          [ 0.5           ,  0.438788513081,  0.833333333333],
                          [ 0.5           ,  0.377577026161,  0.166666666667],
                          [ 0.5           ,  0.408182769621,  0.333333333333],
                          [ 0.5           ,  0.46939425654 ,  0.666666666667],
                          [ 0.5           ,  0.5           ,  0.833333333333],
                          [ 0.5           ,  0.438788513081,  0.166666666667],
                          [ 0.5           ,  0.46939425654 ,  0.333333333333],
                          [ 0.5           ,  0.53060574346 ,  0.666666666667],
                          [ 0.5           ,  0.561211486919,  0.833333333333],
                          [ 0.5           ,  0.5           ,  0.166666666667],
                          [ 0.5           ,  0.53060574346 ,  0.333333333333],
                          [ 0.5           ,  0.591817230379,  0.666666666667],
                          [ 0.5           ,  0.622422973839,  0.833333333333],
                          [ 0.5           ,  0.561211486919,  0.166666666667],
                          [ 0.5           ,  0.591817230379,  0.333333333333],
                          [ 0.5           ,  0.653028717298,  0.666666666667],
                          [ 0.5           ,  0.683634460758,  0.833333333333],
                          [ 0.5           ,  0.622422973839,  0.166666666667],
                          [ 0.5           ,  0.653028717298,  0.333333333333],
                          [ 0.5           ,  0.714240204218,  0.666666666667],
                          [ 0.5           ,  0.683634460758,  0.166666666667],
                          [ 0.5           ,  0.714240204218,  0.333333333333],
                          [ 0.5           ,  0.262280875989,  0.794523495372],
                          [ 0.5           ,  0.262280875989,  0.205476504628],
                          [ 0.5           ,  0.737719124011,  0.794523495372],
                          [ 0.5           ,  0.737719124011,  0.205476504628]]

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
nlsave('15AGNR.nc', bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['G', 'Z', 'G'],
    points_per_segment=50,
    bands_above_fermi_level=All
    )
nlsave('15AGNR.nc', bandstructure)
