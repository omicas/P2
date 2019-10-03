# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Two-probe Configuration
# -------------------------------------------------------------

# -------------------------------------------------------------
# Left Electrode
# -------------------------------------------------------------

# Set up lattice
# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [8.23599465363e-16, 13.4504, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.27868]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Copper, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus]

# Define coordinates
left_electrode_coordinates = [[  7.409560932536,   5.8506305553  ,   0.035679186382],
                              [  7.413980561048,   9.300225821137,   0.042690156152],
                              [  7.413308657672,   2.531353055833,   0.129340069489],
                              [  7.41712026044 ,  12.617714059704,   0.133490561344],
                              [  7.309328587736,   7.572992577103,   1.448038272623],
                              [  7.424332051976,   4.231801014969,   1.616830658078],
                              [  7.425833144216,  10.920115487321,   1.623275871782],
                              [  7.415805944816,   0.852808535847,   1.641398001047],
                              [  5.156754452144,   7.574293177909,   2.260656660488],
                              [  5.258566829144,   4.227134318578,   2.288115407083],
                              [  5.26076799464 ,  10.919348398554,   2.290471229148],
                              [  5.254904521568,   0.848320172647,   2.306074023427],
                              [  8.439015750104,   7.535659195777,   3.358269548175],
                              [  5.187102067976,   5.910614112811,   3.775628311139],
                              [  5.20500858716 ,   9.231470166703,   3.777250107284],
                              [  5.23443725144 ,   2.548626745887,   3.79608648499 ],
                              [  5.23868399228 ,  12.598325360104,   3.798098508357],
                              [  7.389239396408,  12.602651021239,   4.492739409687],
                              [  7.383315735392,   2.544594403233,   4.494235455326],
                              [  7.326063331064,   9.158815824505,   4.626959521428],
                              [  7.305138841616,   5.975072338068,   4.641906609096],
                              [  7.371138817352,   0.848192441798,   5.989135187004],
                              [  7.386117603176,  10.947383993737,   6.031399557478],
                              [  7.374800133248,   4.194106075821,   6.041672339738],
                              [  7.21432146164 ,   7.574073604312,   6.209615234561],
                              [  5.20113851408 ,   0.84870255263 ,   6.643655167351],
                              [  5.196895494272,  10.925838138125,   6.670783588633],
                              [  5.186196648656,   4.221621189511,   6.679830095833],
                              [  5.033862955112,   7.5770551652  ,   6.783182879239],
                              [  5.173193299928,  12.624322782011,   8.155026548305],
                              [  5.170314759056,   2.517587599985,   8.159523985088],
                              [  5.121219511208,   9.299721042299,   8.240577445323],
                              [  5.119509698744,   5.855600138437,   8.243005044168]]*Angstrom

# Set up configuration
left_electrode = BulkConfiguration(
    bravais_lattice=left_electrode_lattice,
    elements=left_electrode_elements,
    cartesian_coordinates=left_electrode_coordinates
    )

# -------------------------------------------------------------
# Right Electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [8.23599465363e-16, 13.4504, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.27868]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                            Phosphorus, Phosphorus, Copper, Phosphorus, Phosphorus, Phosphorus,
                            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                            Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                            Phosphorus, Phosphorus]

# Define coordinates
right_electrode_coordinates = [[  7.409560932536,   5.8506305553  ,   0.035674955832],
                               [  7.413980561048,   9.300225821137,   0.042685925602],
                               [  7.413308657672,   2.531353055833,   0.129335838939],
                               [  7.41712026044 ,  12.617714059704,   0.133486330794],
                               [  7.309328587736,   7.572992577103,   1.448034042073],
                               [  7.424332051976,   4.231801014969,   1.616826427528],
                               [  7.425833144216,  10.920115487321,   1.623271641232],
                               [  7.415805944816,   0.852808535847,   1.641393770497],
                               [  5.156754452144,   7.574293177909,   2.260652429938],
                               [  5.258566829144,   4.227134318578,   2.288111176533],
                               [  5.26076799464 ,  10.919348398554,   2.290466998598],
                               [  5.254904521568,   0.848320172647,   2.306069792877],
                               [  8.439015750104,   7.535659195777,   3.358265317625],
                               [  5.187102067976,   5.910614112811,   3.775624080589],
                               [  5.20500858716 ,   9.231470166703,   3.777245876734],
                               [  5.23443725144 ,   2.548626745887,   3.79608225444 ],
                               [  5.23868399228 ,  12.598325360104,   3.798094277807],
                               [  7.389239396408,  12.602651021239,   4.492735179137],
                               [  7.383315735392,   2.544594403233,   4.494231224776],
                               [  7.326063331064,   9.158815824505,   4.626955290878],
                               [  7.305138841616,   5.975072338068,   4.641902378546],
                               [  7.371138817352,   0.848192441798,   5.989130956454],
                               [  7.386117603176,  10.947383993737,   6.031395326928],
                               [  7.374800133248,   4.194106075821,   6.041668109188],
                               [  7.21432146164 ,   7.574073604312,   6.209611004011],
                               [  5.20113851408 ,   0.84870255263 ,   6.643650936801],
                               [  5.196895494272,  10.925838138125,   6.670779358083],
                               [  5.186196648656,   4.221621189511,   6.679825865283],
                               [  5.033862955112,   7.5770551652  ,   6.783178648689],
                               [  5.173193299928,  12.624322782011,   8.155022317755],
                               [  5.170314759056,   2.517587599985,   8.159519754538],
                               [  5.121219511208,   9.299721042299,   8.240573214773],
                               [  5.119509698744,   5.855600138437,   8.243000813618]]*Angstrom

# Set up configuration
right_electrode = BulkConfiguration(
    bravais_lattice=right_electrode_lattice,
    elements=right_electrode_elements,
    cartesian_coordinates=right_electrode_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
basis_set = [
    GGABasis.Phosphorus_DoubleZetaPolarized,
    GGABasis.Copper_DoubleZetaPolarized,
    ]

#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = GGA.PBE

#----------------------------------------
# Numerical Accuracy Settings
#----------------------------------------
left_electrode_k_point_sampling = MonkhorstPackGrid(
    nb=3,
    nc=32,
    )
left_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=left_electrode_k_point_sampling,
    )

right_electrode_k_point_sampling = MonkhorstPackGrid(
    nb=3,
    nc=32,
    )
right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=right_electrode_k_point_sampling,
    )

#----------------------------------------
# Iteration Control Settings
#----------------------------------------
left_electrode_iteration_control_parameters = IterationControlParameters(
    max_steps=300,
    tolerance=5e-05,
    number_of_history_steps=30,
    )

right_electrode_iteration_control_parameters = IterationControlParameters(
    max_steps=300,
    tolerance=5e-05,
    number_of_history_steps=30,
    )

#----------------------------------------
# Poisson Solver Settings
#----------------------------------------
left_electrode_poisson_solver = MultigridSolver(
    boundary_conditions=[[PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()]]
    )

right_electrode_poisson_solver = MultigridSolver(
    boundary_conditions=[[PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()],
                         [PeriodicBoundaryCondition(),PeriodicBoundaryCondition()]]
    )

#----------------------------------------
# Electrode Calculators
#----------------------------------------
left_electrode_calculator = LCAOCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=left_electrode_numerical_accuracy_parameters,
    iteration_control_parameters=left_electrode_iteration_control_parameters,
    poisson_solver=left_electrode_poisson_solver,
    )

right_electrode_calculator = LCAOCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=right_electrode_numerical_accuracy_parameters,
    iteration_control_parameters=right_electrode_iteration_control_parameters,
    poisson_solver=right_electrode_poisson_solver,
    )

left_electrode.setCalculator(left_electrode_calculator)
left_electrode.update()
nlsave('E_BP_Cu.nc', left_electrode)

