# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.36688, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.46100171044]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5           ,  0.283880706963,  0.25          ],
                          [ 0.5           ,  0.317129828969,  0.75          ],
                          [ 0.5           ,  0.38362807298 ,  0.75          ],
                          [ 0.5           ,  0.416877194986,  0.25          ],
                          [ 0.5           ,  0.483375438997,  0.25          ],
                          [ 0.5           ,  0.516624561003,  0.75          ],
                          [ 0.5           ,  0.583122805014,  0.75          ],
                          [ 0.5           ,  0.61637192702 ,  0.25          ],
                          [ 0.5           ,  0.682870171031,  0.25          ],
                          [ 0.5           ,  0.716119293037,  0.75          ],
                          [ 0.5           ,  0.232867179401,  0.25          ],
                          [ 0.5           ,  0.767132820599,  0.75          ]]

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
nlsave('5ZGNR.nc', bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['Z', 'G', 'Z'],
    points_per_segment=50,
    bands_above_fermi_level=All
    )
nlsave('5ZGNR.nc', bandstructure)