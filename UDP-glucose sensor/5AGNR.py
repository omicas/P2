# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 16.1525042761, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5           ,  0.309549523376,  0.666666666667],
                          [ 0.5           ,  0.385729714026,  0.833333333333],
                          [ 0.5           ,  0.309549523376,  0.333333333333],
                          [ 0.5           ,  0.461909904675,  0.666666666667],
                          [ 0.5           ,  0.538090095325,  0.833333333333],
                          [ 0.5           ,  0.385729714026,  0.166666666667],
                          [ 0.5           ,  0.461909904675,  0.333333333333],
                          [ 0.5           ,  0.614270285974,  0.666666666667],
                          [ 0.5           ,  0.538090095325,  0.166666666667],
                          [ 0.5           ,  0.614270285974,  0.333333333333],
                          [ 0.5           ,  0.251108577856,  0.794523495372],
                          [ 0.5           ,  0.251108577856,  0.205476504628],
                          [ 0.5           ,  0.672711231494,  0.794523495372],
                          [ 0.5           ,  0.672711231494,  0.205476504628]]

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
basis_set = [
    GGABasis.Hydrogen_DoubleZetaPolarized,
    GGABasis.Carbon_DoubleZetaPolarized,
    ]

#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = GGA.PBE

k_point_sampling = MonkhorstPackGrid(
    nc=9,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=k_point_sampling,
    )

calculator = LCAOCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('5AGNR.nc', bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['Z', 'G', 'Z'],
    points_per_segment=50,
    bands_above_fermi_level=All
    )
nlsave('5AGNR.nc', bandstructure)