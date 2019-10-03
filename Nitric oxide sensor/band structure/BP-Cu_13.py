# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [8.23599465363e-16, 13.4504, 0.0]*Angstrom
vector_c = [8.03490764921e-16, 8.03490764921e-16, 13.122]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
            Phosphorus, Phosphorus, Phosphorus, Copper]

# Define coordinates
fractional_coordinates = [[ 0.45086       ,  0.062436804853,  0.191046666666],
                          [ 0.45086       ,  0.312436804853,  0.191046666666],
                          [ 0.45086       ,  0.562436804853,  0.191046666666],
                          [ 0.45086       ,  0.812436804853,  0.191046666666],
                          [ 0.45086       ,  0.062436804853,  0.857713333334],
                          [ 0.45086       ,  0.312436804853,  0.857713333334],
                          [ 0.45086       ,  0.562436804853,  0.857713333334],
                          [ 0.45086       ,  0.812436804853,  0.857713333334],
                          [ 0.45086       ,  0.062436804853,  0.52438       ],
                          [ 0.45086       ,  0.312436804853,  0.52438       ],
                          [ 0.45086       ,  0.562436804853,  0.52438       ],
                          [ 0.45086       ,  0.812436804853,  0.52438       ],
                          [ 0.54213       ,  0.062462082912,  0.142406666666],
                          [ 0.54213       ,  0.312462082912,  0.142406666666],
                          [ 0.54213       ,  0.562462082912,  0.142406666666],
                          [ 0.54213       ,  0.812462082912,  0.142406666666],
                          [ 0.54213       ,  0.062462082912,  0.809073333334],
                          [ 0.54213       ,  0.312462082912,  0.809073333334],
                          [ 0.54213       ,  0.562462082912,  0.809073333334],
                          [ 0.54213       ,  0.812462082912,  0.809073333334],
                          [ 0.54213       ,  0.062462082912,  0.47574       ],
                          [ 0.54213       ,  0.312462082912,  0.47574       ],
                          [ 0.54213       ,  0.562462082912,  0.47574       ],
                          [ 0.54213       ,  0.812462082912,  0.47574       ],
                          [ 0.54274       ,  0.187462082912,  0.024546666666],
                          [ 0.54274       ,  0.437462082912,  0.024546666666],
                          [ 0.54274       ,  0.687462082912,  0.024546666666],
                          [ 0.54274       ,  0.937462082912,  0.024546666666],
                          [ 0.54274       ,  0.187462082912,  0.691213333334],
                          [ 0.54274       ,  0.437462082912,  0.691213333334],
                          [ 0.54274       ,  0.687462082912,  0.691213333334],
                          [ 0.54274       ,  0.937462082912,  0.691213333334],
                          [ 0.54274       ,  0.187462082912,  0.35788       ],
                          [ 0.54274       ,  0.437462082912,  0.35788       ],
                          [ 0.54274       ,  0.687462082912,  0.35788       ],
                          [ 0.54274       ,  0.937462082912,  0.35788       ],
                          [ 0.45131       ,  0.187563195147,  0.309053333334],
                          [ 0.45131       ,  0.437563195147,  0.309053333334],
                          [ 0.45131       ,  0.687563195147,  0.309053333334],
                          [ 0.45131       ,  0.937563195147,  0.309053333334],
                          [ 0.45131       ,  0.187563195147,  0.97572       ],
                          [ 0.45131       ,  0.437563195147,  0.97572       ],
                          [ 0.45131       ,  0.687563195147,  0.97572       ],
                          [ 0.45131       ,  0.937563195147,  0.97572       ],
                          [ 0.45131       ,  0.187563195147,  0.642386666666],
                          [ 0.45131       ,  0.437563195147,  0.642386666666],
                          [ 0.45131       ,  0.687563195147,  0.642386666666],
                          [ 0.45131       ,  0.937563195147,  0.642386666666],
                          [ 0.59192       ,  0.562386248736,  0.619213333333]]


# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add tags
bulk_configuration.addTags('Selection 0', [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                                           13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                                           39, 40, 41, 42, 43, 44, 45, 46, 47])

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
basis_set = [
    GGABasis.Copper_DoubleZetaPolarized,
    GGABasis.Phosphorus_DoubleZetaPolarized,
    ]

#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = GGA.PBE

k_point_sampling = MonkhorstPackGrid(
    nb=3,
    nc=3,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=k_point_sampling,
    )

iteration_control_parameters = IterationControlParameters(
    max_steps=300,
    tolerance=5e-05,
    )

#----------------------------------------
# Grimme DFTD3
#----------------------------------------
correction_extension = GrimmeDFTD3(
    exchange_correlation=GGA.PBE,
    maximum_neighbour_distance=30.0*Ang,
    include_three_body_term=False,
    )

calculator = LCAOCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    iteration_control_parameters=iteration_control_parameters,
    correction_extension=correction_extension,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('BP-Cu_13.nc', bulk_configuration)

# -------------------------------------------------------------
# Optimize Geometry
# -------------------------------------------------------------
fix_atom_indices_0 = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                      13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                      26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                      39, 40, 41, 42, 43, 44, 45, 46, 47]
constraints = [FixAtomConstraints(fix_atom_indices_0)]

bulk_configuration = OptimizeGeometry(
    bulk_configuration,
    max_forces=0.05*eV/Ang,
    max_steps=200,
    max_step_length=0.2*Ang,
#    constraints=constraints,
    trajectory_filename=None,
    disable_stress=True,
    optimizer_method=LBFGS(),
)
nlsave('BP-Cu_13.nc', bulk_configuration)
nlprint(bulk_configuration)

# -------------------------------------------------------------
# Total Energy
# -------------------------------------------------------------
total_energy = TotalEnergy(bulk_configuration)
nlsave('BP-Cu_13.nc', total_energy)
nlprint(total_energy)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['Y', 'G', 'Z'],
    points_per_segment=50,
    bands_above_fermi_level=All
    )
nlsave('BP-Cu_13.nc', bandstructure)