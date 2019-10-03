# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Two-probe Configuration
# -------------------------------------------------------------

left_electrode = nlread("E_BP_Cu.nc")[0]
right_electrode = nlread("E_BP_Cu.nc")[0]

# -------------------------------------------------------------
# Central Region
# -------------------------------------------------------------

vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [8.23599465363e-16, 13.4504, 0.0]*Angstrom
vector_c = [3.42431870917e-15, 3.42431870917e-15, 55.9233684611]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Copper, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus, Oxygen,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Oxygen, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Oxygen, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Copper, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus]

# Define coordinates
central_region_coordinates = [[  7.409560932536,   5.8506305553  ,   0.035679186382],
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
                              [  5.119509698744,   5.855600138437,   8.243005044168],
                              [  7.195015138136,   9.247746775485,   8.600123869326],
                              [  7.190927966984,   5.870327973619,   8.60043803579 ],
                              [  7.154511532304,   2.509388230778,   8.601085322281],
                              [  7.156218382352,  12.610669806559,   8.601130553356],
                              [  7.169991521024,   7.559953394608,  10.094426003742],
                              [  7.16279943416 ,  10.930967710138,  10.098471176955],
                              [  7.158702218984,   4.189981971485,  10.099404978812],
                              [  7.15527828908 ,   0.835973050706,  10.105215176787],
                              [  5.02027076756 ,   7.562621941594,  10.778975860585],
                              [  5.011311880304,   4.192666856295,  10.790383536305],
                              [  5.016346064816,  10.928800433843,  10.791243949742],
                              [  5.01036209744 ,   0.835602016674,  10.811788618902],
                              [  5.062636146056,   5.883672544204,  12.286250695904],
                              [  5.066676836384,   9.237250744856,  12.288578383772],
                              [  5.049483673616,  12.599357384843,  12.308370957852],
                              [  5.043543610448,   2.521061776971,  12.308633874247],
                              [  7.23849459644 ,   5.837069900004,  12.913527831763],
                              [  7.243016189984,   9.286181689774,  12.919604278701],
                              [  7.217617211   ,  12.609908241912,  12.952732203615],
                              [  7.211739418016,   2.514242067211,  12.953056155982],
                              [  7.060755103736,   7.558034707597,  14.360099381043],
                              [  7.228103709752,   0.837972432921,  14.457581912053],
                              [  7.24092342812 ,   4.1901912969  ,  14.460359862849],
                              [  7.244910616256,  10.936951337318,  14.462131094423],
                              [  5.083088086016,   0.835297021416,  15.163654531361],
                              [  5.097507867368,   4.210209301993,  15.170152762746],
                              [  5.101483042088,  10.914141441803,  15.17091980011 ],
                              [  4.986464688344,   7.562334675133,  15.207393112409],
                              [  8.145737626016,   7.540853955208,  15.428349266184],
                              [  5.085491903648,   2.518805971811,  16.660947951596],
                              [  5.088204711416,  12.601695780166,  16.662863105711],
                              [  5.169999831584,   9.248744069529,  16.683828289346],
                              [  5.165304320504,   5.873166638278,  16.683952688006],
                              [  7.317822450248,   5.853495872047,  17.395879787276],
                              [  7.32183396116 ,   9.264903024797,  17.396188789827],
                              [  7.217925672872,   2.520186730962,  17.401972619943],
                              [  7.221123066512,  12.600364794745,  17.402346995314],
                              [  7.258982697344,   7.559629407923,  18.886801449688],
                              [  7.1684068856  ,   0.836161537039,  18.893136036008],
                              [  7.16616268196 ,  10.930327332572,  18.911196939297],
                              [  7.161646924568,   4.191128688982,  18.911359049771],
                              [  5.081692339664,   7.56154859927 ,  19.513015018855],
                              [  5.001876514952,   0.835040169807,  19.544215288481],
                              [  5.00379423824 ,  10.924006639539,  19.548752741725],
                              [  4.99997697872 ,   4.196396267803,  19.549721342575],
                              [  5.042020603808,   5.893184313204,  21.031017399954],
                              [  5.046003880928,   9.22725936811 ,  21.031547890213],
                              [  4.998907679456,  12.605939705669,  21.051802871711],
                              [  4.997123316032,   2.511973956415,  21.05269560945 ],
                              [  7.195015138136,   9.247746775485,  21.722123869326],
                              [  7.190927966984,   5.870327973619,  21.72243803579 ],
                              [  7.154511532304,   2.509388230778,  21.723085322281],
                              [  7.156218382352,  12.610669806559,  21.723130553356],
                              [  7.169991521024,   7.559953394608,  23.216426003742],
                              [  7.16279943416 ,  10.930967710138,  23.220471176955],
                              [  7.158702218984,   4.189981971485,  23.221404978812],
                              [  7.15527828908 ,   0.835973050706,  23.227215176787],
                              [  5.02027076756 ,   7.562621941594,  23.900975860585],
                              [  5.011311880304,   4.192666856295,  23.912383536305],
                              [  5.016346064816,  10.928800433843,  23.913243949742],
                              [  5.01036209744 ,   0.835602016674,  23.933788618902],
                              [  5.062636146056,   5.883672544204,  25.408250695904],
                              [  5.066676836384,   9.237250744856,  25.410578383772],
                              [  5.049483673616,  12.599357384843,  25.430370957852],
                              [  5.043543610448,   2.521061776971,  25.430633874247],
                              [  7.23849459644 ,   5.837069900004,  26.035527831763],
                              [  7.243016189984,   9.286181689774,  26.041604278701],
                              [  7.217617211   ,  12.609908241912,  26.074732203615],
                              [  7.211739418016,   2.514242067211,  26.075056155982],
                              [  7.060755103736,   7.558034707597,  27.482099381043],
                              [  7.228103709752,   0.837972432921,  27.579581912053],
                              [  7.24092342812 ,   4.1901912969  ,  27.582359862849],
                              [  7.244910616256,  10.936951337318,  27.584131094423],
                              [  5.083088086016,   0.835297021416,  28.285654531361],
                              [  5.097507867368,   4.210209301993,  28.292152762746],
                              [  5.101483042088,  10.914141441803,  28.29291980011 ],
                              [  4.986464688344,   7.562334675133,  28.329393112409],
                              [  8.145737626016,   7.540853955208,  28.550349266184],
                              [  5.085491903648,   2.518805971811,  29.782947951596],
                              [  5.088204711416,  12.601695780166,  29.784863105711],
                              [  5.169999831584,   9.248744069529,  29.805828289346],
                              [  5.165304320504,   5.873166638278,  29.805952688006],
                              [  7.317822450248,   5.853495872047,  30.517879787276],
                              [  7.32183396116 ,   9.264903024797,  30.518188789827],
                              [  7.217925672872,   2.520186730962,  30.523972619943],
                              [  7.221123066512,  12.600364794745,  30.524346995314],
                              [  7.258982697344,   7.559629407923,  32.008801449688],
                              [  7.1684068856  ,   0.836161537039,  32.015136036008],
                              [  7.16616268196 ,  10.930327332572,  32.033196939297],
                              [  7.161646924568,   4.191128688982,  32.033359049771],
                              [  5.081692339664,   7.56154859927 ,  32.635015018855],
                              [  5.001876514952,   0.835040169807,  32.666215288481],
                              [  5.00379423824 ,  10.924006639539,  32.670752741725],
                              [  4.99997697872 ,   4.196396267803,  32.671721342575],
                              [  5.042020603808,   5.893184313204,  34.153017399954],
                              [  5.046003880928,   9.22725936811 ,  34.153547890213],
                              [  4.998907679456,  12.605939705669,  34.173802871711],
                              [  4.997123316032,   2.511973956415,  34.17469560945 ],
                              [  7.195015138136,   9.247746775485,  34.844123869326],
                              [  7.190927966984,   5.870327973619,  34.844438035791],
                              [  7.154511532304,   2.509388230778,  34.845085322281],
                              [  7.156218382352,  12.610669806559,  34.845130553356],
                              [  7.169991521024,   7.559953394608,  36.338426003742],
                              [  7.16279943416 ,  10.930967710138,  36.342471176955],
                              [  7.158702218984,   4.189981971485,  36.343404978812],
                              [  7.15527828908 ,   0.835973050706,  36.349215176787],
                              [  5.02027076756 ,   7.562621941594,  37.022975860585],
                              [  5.011311880304,   4.192666856295,  37.034383536305],
                              [  5.016346064816,  10.928800433843,  37.035243949742],
                              [  5.01036209744 ,   0.835602016674,  37.055788618902],
                              [  5.062636146056,   5.883672544204,  38.530250695904],
                              [  5.066676836384,   9.237250744856,  38.532578383772],
                              [  5.049483673616,  12.599357384843,  38.552370957852],
                              [  5.043543610448,   2.521061776971,  38.552633874247],
                              [  7.23849459644 ,   5.837069900004,  39.157527831763],
                              [  7.243016189984,   9.286181689774,  39.163604278701],
                              [  7.217617211   ,  12.609908241912,  39.196732203615],
                              [  7.211739418016,   2.514242067211,  39.197056155982],
                              [  7.060755103736,   7.558034707597,  40.604099381043],
                              [  7.228103709752,   0.837972432921,  40.701581912053],
                              [  7.24092342812 ,   4.1901912969  ,  40.704359862849],
                              [  7.244910616256,  10.936951337318,  40.706131094423],
                              [  5.083088086016,   0.835297021416,  41.407654531361],
                              [  5.097507867368,   4.210209301993,  41.414152762746],
                              [  5.101483042088,  10.914141441803,  41.41491980011 ],
                              [  4.986464688344,   7.562334675133,  41.451393112409],
                              [  8.145737626016,   7.540853955208,  41.672349266184],
                              [  5.085491903648,   2.518805971811,  42.904947951596],
                              [  5.088204711416,  12.601695780166,  42.906863105711],
                              [  5.169999831584,   9.248744069529,  42.927828289346],
                              [  5.165304320504,   5.873166638278,  42.927952688006],
                              [  7.317822450248,   5.853495872047,  43.639879787276],
                              [  7.32183396116 ,   9.264903024797,  43.640188789827],
                              [  7.217925672872,   2.520186730962,  43.645972619943],
                              [  7.221123066512,  12.600364794745,  43.646346995314],
                              [  7.258982697344,   7.559629407923,  45.130801449688],
                              [  7.1684068856  ,   0.836161537039,  45.137136036008],
                              [  7.16616268196 ,  10.930327332572,  45.155196939297],
                              [  7.161646924568,   4.191128688982,  45.155359049771],
                              [  5.081692339664,   7.56154859927 ,  45.757015018855],
                              [  5.001876514952,   0.835040169807,  45.788215288481],
                              [  5.00379423824 ,  10.924006639539,  45.792752741725],
                              [  4.99997697872 ,   4.196396267803,  45.793721342575],
                              [  5.042020603808,   5.893184313204,  47.275017399954],
                              [  5.046003880928,   9.22725936811 ,  47.275547890213],
                              [  4.998907679456,  12.605939705669,  47.295802871711],
                              [  4.997123316032,   2.511973956415,  47.29669560945 ],
                              [  7.409560932536,   5.8506305553  ,  47.680363416932],
                              [  7.413980561048,   9.300225821137,  47.687374386702],
                              [  7.413308657672,   2.531353055833,  47.774024300039],
                              [  7.41712026044 ,  12.617714059704,  47.778174791894],
                              [  7.309328587736,   7.572992577103,  49.092722503173],
                              [  7.424332051976,   4.231801014969,  49.261514888628],
                              [  7.425833144216,  10.920115487321,  49.267960102332],
                              [  7.415805944816,   0.852808535847,  49.286082231597],
                              [  5.156754452144,   7.574293177909,  49.905340891038],
                              [  5.258566829144,   4.227134318578,  49.932799637633],
                              [  5.26076799464 ,  10.919348398554,  49.935155459698],
                              [  5.254904521568,   0.848320172647,  49.950758253977],
                              [  8.439015750104,   7.535659195777,  51.002953778725],
                              [  5.187102067976,   5.910614112811,  51.420312541689],
                              [  5.20500858716 ,   9.231470166703,  51.421934337834],
                              [  5.23443725144 ,   2.548626745887,  51.44077071554 ],
                              [  5.23868399228 ,  12.598325360104,  51.442782738907],
                              [  7.389239396408,  12.602651021239,  52.137423640237],
                              [  7.383315735392,   2.544594403233,  52.138919685876],
                              [  7.326063331064,   9.158815824505,  52.271643751978],
                              [  7.305138841616,   5.975072338068,  52.286590839646],
                              [  7.371138817352,   0.848192441798,  53.633819417554],
                              [  7.386117603176,  10.947383993737,  53.676083788028],
                              [  7.374800133248,   4.194106075821,  53.686356570288],
                              [  7.21432146164 ,   7.574073604312,  53.854299465111],
                              [  5.20113851408 ,   0.84870255263 ,  54.288339397901],
                              [  5.196895494272,  10.925838138125,  54.315467819183],
                              [  5.186196648656,   4.221621189511,  54.324514326383],
                              [  5.033862955112,   7.5770551652  ,  54.427867109789],
                              [  5.173193299928,  12.624322782011,  55.799710778855],
                              [  5.170314759056,   2.517587599985,  55.804208215638],
                              [  5.121219511208,   9.299721042299,  55.885261675873],
                              [  5.119509698744,   5.855600138437,  55.887689274718]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

VG=numpy.linspace(-2,2,9)
for vg in VG:
  # Add metallic region
  metallic_region_0 = BoxRegion(
    vg*Volt,
    xmin = 0.0*Angstrom, xmax = 0.5*Angstrom,
    ymin = 0.0*Angstrom, ymax = 13.4504*Angstrom,
    zmin = 8.38850526916*Angstrom, zmax = 69.984*Angstrom,
  )

  metallic_regions = [metallic_region_0]
  central_region.setMetallicRegions(metallic_regions)

  # Add dielectric region
  dielectric_region_0 = BoxRegion(
    3.9,
    xmin = 0.5*Angstrom, xmax = 4.0*Angstrom,
    ymin = 0.0*Angstrom, ymax = 13.4504*Angstrom,
    zmin = 8.38850526916*Angstrom, zmax = 47.5348631919*Angstrom,
  )

  dielectric_regions = [dielectric_region_0]
  central_region.setDielectricRegions(dielectric_regions)

  device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
  basis_set = [
    GGABasis.Oxygen_DoubleZetaPolarized,
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
  device_k_point_sampling = MonkhorstPackGrid(
    nb=3,
    nc=32,
    )
  device_numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=device_k_point_sampling,
    )

#----------------------------------------
# Iteration Control Settings
#----------------------------------------
  device_iteration_control_parameters = IterationControlParameters(
    max_steps=300,
    tolerance=5e-05,
    number_of_history_steps=30,
    )

#----------------------------------------
# Device Algorithm Settings
#----------------------------------------
  initial_density_type = NeutralAtom(
    electrode_constraint_length=8.27868*Angstrom,
    )

  device_algorithm_parameters = DeviceAlgorithmParameters(
    initial_density_type=initial_density_type,
    )

#----------------------------------------
# Device Calculator
#----------------------------------------
  calculator = DeviceLCAOCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=device_numerical_accuracy_parameters,
    iteration_control_parameters=device_iteration_control_parameters,
    device_algorithm_parameters=device_algorithm_parameters,
#    electrode_calculators=
#        [left_electrode_calculator, right_electrode_calculator],
    )

  device_configuration.setCalculator(calculator)
  device_configuration.update()
  nlsave('Device_BP_O_Cu_40_%s.nc'%vg, device_configuration)

# -------------------------------------------------------------
# Transmission Spectrum
# -------------------------------------------------------------
  kpoint_grid = MonkhorstPackGrid()

  transmission_spectrum = TransmissionSpectrum(
    configuration=device_configuration,
    energies=numpy.linspace(-1,1,101)*eV,
    kpoints=kpoint_grid,
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    self_energy_calculator=RecursionSelfEnergy(),
    )
  nlsave('Device_BP_O_Cu_40_%s.nc'%vg, transmission_spectrum)
  nlprint(transmission_spectrum)

  T=[300]
#  T=numpy.linspace(250,350,11)
  for temp in T:
    temperature=temp*Kelvin
    conductance=transmission_spectrum.conductance(electrode_temperatures=(temperature,temperature))
    current=transmission_spectrum.current(electrode_temperatures=(temperature,temperature))
    if ( processIsMaster() ):
      print "Gate voltage = %s: Conductance = %s at T = %s"%(vg,conductance,temperature)
      print "Gate voltage = %s: Current = %s at T = %s"%(vg,current,temperature)

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
  nlsave('Device_BP_O_Cu_40_%s.nc'%vg, iv_curve)
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
  nlsave('Device_BP_O_Cu_40_%s.nc'%vg, iv_curve)
  nlprint(iv_curve)
