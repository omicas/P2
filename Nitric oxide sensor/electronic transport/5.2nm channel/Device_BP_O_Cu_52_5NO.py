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
vector_c = [4.25117807891e-15, 4.25117807891e-15, 69.4270067398]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [8.23599465363e-16, 13.4504, 0.0]*Angstrom
vector_c = [4.25117807891e-15, 4.25117807891e-15, 69.4270067398]*Angstrom
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
                           Nitrogen, Phosphorus, Phosphorus, Phosphorus, Phosphorus, Oxygen,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Oxygen, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Nitrogen,
                           Phosphorus, Phosphorus, Phosphorus, Oxygen, Phosphorus, Phosphorus,
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
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Nitrogen, Oxygen,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Oxygen, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Nitrogen, Phosphorus, Phosphorus,
                           Phosphorus, Oxygen, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Oxygen, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Nitrogen, Oxygen, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Copper, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus]

# Define coordinates
central_region_coordinates = [[  7.409560932536,   5.8506305553  ,   0.035679186376],
                              [  7.413980561048,   9.300225821137,   0.042690156146],
                              [  7.413308657672,   2.531353055833,   0.129340069482],
                              [  7.41712026044 ,  12.617714059704,   0.133490561338],
                              [  7.309328587736,   7.572992577103,   1.448038272617],
                              [  7.424332051976,   4.231801014969,   1.616830658072],
                              [  7.425833144216,  10.920115487321,   1.623275871776],
                              [  7.415805944816,   0.852808535847,   1.641398001041],
                              [  5.156754452144,   7.574293177909,   2.260656660482],
                              [  5.258566829144,   4.227134318578,   2.288115407077],
                              [  5.26076799464 ,  10.919348398554,   2.290471229141],
                              [  5.254904521568,   0.848320172647,   2.306074023421],
                              [  8.439015750104,   7.535659195777,   3.358269548169],
                              [  5.187102067976,   5.910614112811,   3.775628311133],
                              [  5.20500858716 ,   9.231470166703,   3.777250107278],
                              [  5.23443725144 ,   2.548626745887,   3.796086484984],
                              [  5.23868399228 ,  12.598325360104,   3.798098508351],
                              [  7.389239396408,  12.602651021239,   4.492739409681],
                              [  7.383315735392,   2.544594403233,   4.49423545532 ],
                              [  7.326063331064,   9.158815824505,   4.626959521422],
                              [  7.305138841616,   5.975072338068,   4.64190660909 ],
                              [  7.371138817352,   0.848192441798,   5.989135186998],
                              [  7.386117603176,  10.947383993737,   6.031399557472],
                              [  7.374800133248,   4.194106075821,   6.041672339732],
                              [  7.21432146164 ,   7.574073604312,   6.209615234554],
                              [  5.20113851408 ,   0.84870255263 ,   6.643655167345],
                              [  5.196895494272,  10.925838138125,   6.670783588627],
                              [  5.186196648656,   4.221621189511,   6.679830095827],
                              [  5.033862955112,   7.5770551652  ,   6.783182879233],
                              [  5.173193299928,  12.624322782011,   8.155026548298],
                              [  5.170314759056,   2.517587599985,   8.159523985082],
                              [  5.121219511208,   9.299721042299,   8.240577445317],
                              [  5.119509698744,   5.855600138437,   8.243005044161],
                              [  7.195015138136,   9.247746775485,   8.60012386932 ],
                              [  7.190927966984,   5.870327973619,   8.600438035784],
                              [  7.154511532304,   2.509388230778,   8.601085322275],
                              [  7.156218382352,  12.610669806559,   8.60113055335 ],
                              [  7.169991521024,   7.559953394608,  10.094426003736],
                              [  7.16279943416 ,  10.930967710138,  10.098471176949],
                              [  7.158702218984,   4.189981971485,  10.099404978806],
                              [  7.15527828908 ,   0.835973050706,  10.10521517678 ],
                              [  9.124558645304,  11.075695851368,  10.728275953884],
                              [  5.02027076756 ,   7.562621941594,  10.778975860579],
                              [  5.011311880304,   4.192666856295,  10.790383536299],
                              [  5.016346064816,  10.928800433843,  10.791243949736],
                              [  5.01036209744 ,   0.835602016674,  10.811788618896],
                              [  9.538971890912,  10.268669060195,  11.512592643169],
                              [  5.062636146056,   5.883672544204,  12.286250695898],
                              [  5.066676836384,   9.237250744856,  12.288578383766],
                              [  5.049483673616,  12.599357384843,  12.308370957846],
                              [  5.043543610448,   2.521061776971,  12.30863387424 ],
                              [  7.23849459644 ,   5.837069900004,  12.913527831757],
                              [  7.243016189984,   9.286181689774,  12.919604278694],
                              [  7.217617211   ,  12.609908241912,  12.952732203609],
                              [  7.211739418016,   2.514242067211,  12.953056155975],
                              [  7.060755103736,   7.558034707597,  14.360099381036],
                              [  7.228103709752,   0.837972432921,  14.457581912047],
                              [  7.24092342812 ,   4.1901912969  ,  14.460359862843],
                              [  7.244910616256,  10.936951337318,  14.462131094416],
                              [  5.083088086016,   0.835297021416,  15.163654531355],
                              [  5.097507867368,   4.210209301993,  15.17015276274 ],
                              [  5.101483042088,  10.914141441803,  15.170919800104],
                              [  4.986464688344,   7.562334675133,  15.207393112403],
                              [  8.145737626016,   7.540853955208,  15.428349266178],
                              [  5.085491903648,   2.518805971811,  16.66094795159 ],
                              [  5.088204711416,  12.601695780166,  16.662863105705],
                              [  5.169999831584,   9.248744069529,  16.68382828934 ],
                              [  5.165304320504,   5.873166638278,  16.683952688   ],
                              [  7.317822450248,   5.853495872047,  17.395879787269],
                              [  7.32183396116 ,   9.264903024797,  17.39618878982 ],
                              [  7.217925672872,   2.520186730962,  17.401972619937],
                              [  7.221123066512,  12.600364794745,  17.402346995307],
                              [  7.258982697344,   7.559629407923,  18.886801449682],
                              [  7.1684068856  ,   0.836161537039,  18.893136036002],
                              [  7.16616268196 ,  10.930327332572,  18.911196939291],
                              [  7.161646924568,   4.191128688982,  18.911359049765],
                              [  5.081692339664,   7.56154859927 ,  19.513015018848],
                              [  9.123406135712,   4.335856830212,  19.5411638267  ],
                              [  5.001876514952,   0.835040169807,  19.544215288475],
                              [  5.00379423824 ,  10.924006639539,  19.548752741719],
                              [  4.99997697872 ,   4.196396267803,  19.549721342569],
                              [  9.53781938132 ,   3.528830039039,  20.325480515985],
                              [  5.042020603808,   5.893184313204,  21.031017399948],
                              [  5.046003880928,   9.22725936811 ,  21.031547890207],
                              [  4.998907679456,  12.605939705669,  21.051802871705],
                              [  4.997123316032,   2.511973956415,  21.052695609444],
                              [  7.195015138136,   9.247746775485,  21.72212386932 ],
                              [  7.190927966984,   5.870327973619,  21.722438035784],
                              [  7.154511532304,   2.509388230778,  21.723085322275],
                              [  7.156218382352,  12.610669806559,  21.72313055335 ],
                              [  7.169991521024,   7.559953394608,  23.216426003736],
                              [  7.16279943416 ,  10.930967710138,  23.220471176949],
                              [  7.158702218984,   4.189981971485,  23.221404978806],
                              [  7.15527828908 ,   0.835973050706,  23.22721517678 ],
                              [  5.02027076756 ,   7.562621941594,  23.900975860579],
                              [  5.011311880304,   4.192666856295,  23.912383536299],
                              [  5.016346064816,  10.928800433843,  23.913243949736],
                              [  5.01036209744 ,   0.835602016674,  23.933788618896],
                              [  5.062636146056,   5.883672544204,  25.408250695898],
                              [  5.066676836384,   9.237250744856,  25.410578383766],
                              [  5.049483673616,  12.599357384843,  25.430370957846],
                              [  5.043543610448,   2.521061776971,  25.43063387424 ],
                              [  7.23849459644 ,   5.837069900004,  26.035527831757],
                              [  7.243016189984,   9.286181689774,  26.041604278694],
                              [  7.217617211   ,  12.609908241912,  26.074732203609],
                              [  7.211739418016,   2.514242067211,  26.075056155975],
                              [  7.060755103736,   7.558034707597,  27.482099381036],
                              [  7.228103709752,   0.837972432921,  27.579581912047],
                              [  7.24092342812 ,   4.1901912969  ,  27.582359862843],
                              [  7.244910616256,  10.936951337318,  27.584131094416],
                              [  5.083088086016,   0.835297021416,  28.285654531355],
                              [  5.097507867368,   4.210209301993,  28.29215276274 ],
                              [  5.101483042088,  10.914141441803,  28.292919800104],
                              [  4.986464688344,   7.562334675133,  28.329393112403],
                              [  8.145737626016,   7.540853955208,  28.550349266178],
                              [  5.085491903648,   2.518805971811,  29.78294795159 ],
                              [  5.088204711416,  12.601695780166,  29.784863105705],
                              [  5.169999831584,   9.248744069529,  29.80582828934 ],
                              [  5.165304320504,   5.873166638278,  29.805952688   ],
                              [  7.317822450248,   5.853495872047,  30.517879787269],
                              [  7.32183396116 ,   9.264903024797,  30.51818878982 ],
                              [  7.217925672872,   2.520186730962,  30.523972619937],
                              [  7.221123066512,  12.600364794745,  30.524346995307],
                              [  7.258982697344,   7.559629407923,  32.008801449682],
                              [  7.1684068856  ,   0.836161537039,  32.015136036002],
                              [  7.16616268196 ,  10.930327332572,  32.033196939291],
                              [  7.161646924568,   4.191128688982,  32.033359049765],
                              [  5.081692339664,   7.56154859927 ,  32.635015018848],
                              [  5.001876514952,   0.835040169807,  32.666215288475],
                              [  5.00379423824 ,  10.924006639539,  32.670752741719],
                              [  4.99997697872 ,   4.196396267803,  32.671721342569],
                              [  5.042020603808,   5.893184313204,  34.153017399948],
                              [  5.046003880928,   9.22725936811 ,  34.153547890207],
                              [  4.998907679456,  12.605939705669,  34.173802871705],
                              [  4.997123316032,   2.511973956415,  34.174695609444],
                              [  7.195015138136,   9.247746775485,  34.84412386932 ],
                              [  7.190927966984,   5.870327973619,  34.844438035784],
                              [  7.154511532304,   2.509388230778,  34.845085322275],
                              [  7.156218382352,  12.610669806559,  34.84513055335 ],
                              [  9.15677434928 ,   9.392474916715,  35.473928646255],
                              [  9.571187594888,   8.585448125542,  36.25824533554 ],
                              [  7.169991521024,   7.559953394608,  36.338426003736],
                              [  7.16279943416 ,  10.930967710138,  36.342471176949],
                              [  7.158702218984,   4.189981971485,  36.343404978806],
                              [  7.15527828908 ,   0.835973050706,  36.34921517678 ],
                              [  5.02027076756 ,   7.562621941594,  37.022975860579],
                              [  5.011311880304,   4.192666856295,  37.034383536299],
                              [  5.016346064816,  10.928800433843,  37.035243949736],
                              [  5.01036209744 ,   0.835602016674,  37.055788618896],
                              [  5.062636146056,   5.883672544204,  38.530250695898],
                              [  5.066676836384,   9.237250744856,  38.532578383766],
                              [  5.049483673616,  12.599357384843,  38.552370957846],
                              [  5.043543610448,   2.521061776971,  38.55263387424 ],
                              [  7.23849459644 ,   5.837069900004,  39.157527831757],
                              [  7.243016189984,   9.286181689774,  39.163604278694],
                              [  7.217617211   ,  12.609908241912,  39.196732203609],
                              [  7.211739418016,   2.514242067211,  39.197056155975],
                              [  7.060755103736,   7.558034707597,  40.604099381036],
                              [  7.228103709752,   0.837972432921,  40.701581912047],
                              [  7.24092342812 ,   4.1901912969  ,  40.704359862843],
                              [  7.244910616256,  10.936951337318,  40.706131094416],
                              [  5.083088086016,   0.835297021416,  41.407654531355],
                              [  5.097507867368,   4.210209301993,  41.41415276274 ],
                              [  5.101483042088,  10.914141441803,  41.414919800104],
                              [  4.986464688344,   7.562334675133,  41.451393112403],
                              [  8.145737626016,   7.540853955208,  41.672349266178],
                              [  5.085491903648,   2.518805971811,  42.90494795159 ],
                              [  5.088204711416,  12.601695780166,  42.906863105705],
                              [  5.169999831584,   9.248744069529,  42.92782828934 ],
                              [  5.165304320504,   5.873166638278,  42.927952688   ],
                              [  7.317822450248,   5.853495872047,  43.639879787269],
                              [  7.32183396116 ,   9.264903024797,  43.64018878982 ],
                              [  7.217925672872,   2.520186730962,  43.645972619937],
                              [  7.221123066512,  12.600364794745,  43.646346995307],
                              [  7.258982697344,   7.559629407923,  45.130801449682],
                              [  7.1684068856  ,   0.836161537039,  45.137136036002],
                              [  7.16616268196 ,  10.930327332572,  45.155196939291],
                              [  7.161646924568,   4.191128688982,  45.155359049765],
                              [  5.081692339664,   7.56154859927 ,  45.757015018848],
                              [  9.123406135712,   4.335856830212,  45.7851638267  ],
                              [  5.001876514952,   0.835040169807,  45.788215288475],
                              [  5.00379423824 ,  10.924006639539,  45.792752741719],
                              [  4.99997697872 ,   4.196396267803,  45.793721342569],
                              [  9.53781938132 ,   3.528830039039,  46.569480515985],
                              [  5.042020603808,   5.893184313204,  47.275017399948],
                              [  5.046003880928,   9.22725936811 ,  47.275547890207],
                              [  4.998907679456,  12.605939705669,  47.295802871705],
                              [  4.997123316032,   2.511973956415,  47.296695609444],
                              [  7.23849459644 ,   5.837069900004,  47.81785034099 ],
                              [  7.243016189984,   9.286181689774,  47.823926787927],
                              [  7.217617211   ,  12.609908241912,  47.857054712841],
                              [  7.211739418016,   2.514242067211,  47.857378665208],
                              [  7.060755103736,   7.558034707597,  49.264421890269],
                              [  7.228103709752,   0.837972432921,  49.361904421279],
                              [  7.24092342812 ,   4.1901912969  ,  49.364682372076],
                              [  7.244910616256,  10.936951337318,  49.366453603649],
                              [  5.083088086016,   0.835297021416,  50.067977040587],
                              [  5.097507867368,   4.210209301993,  50.074475271973],
                              [  5.101483042088,  10.914141441803,  50.075242309337],
                              [  4.986464688344,   7.562334675133,  50.111715621635],
                              [  8.145737626016,   7.540853955208,  50.332671775411],
                              [  5.085491903648,   2.518805971811,  51.565270460822],
                              [  5.088204711416,  12.601695780166,  51.567185614938],
                              [  5.169999831584,   9.248744069529,  51.588150798573],
                              [  5.165304320504,   5.873166638278,  51.588275197232],
                              [  7.317822450248,   5.853495872047,  52.300202296502],
                              [  7.32183396116 ,   9.264903024797,  52.300511299053],
                              [  7.217925672872,   2.520186730962,  52.306295129169],
                              [  7.221123066512,  12.600364794745,  52.30666950454 ],
                              [  7.258982697344,   7.559629407923,  53.791123958914],
                              [  7.1684068856  ,   0.836161537039,  53.797458545234],
                              [  7.16616268196 ,  10.930327332572,  53.815519448524],
                              [  7.161646924568,   4.191128688982,  53.815681558998],
                              [  5.081692339664,   7.56154859927 ,  54.417337528081],
                              [  5.001876514952,   0.835040169807,  54.448537797708],
                              [  5.00379423824 ,  10.924006639539,  54.453075250952],
                              [  4.99997697872 ,   4.196396267803,  54.454043851802],
                              [  5.042020603808,   5.893184313204,  55.935339909181],
                              [  5.046003880928,   9.22725936811 ,  55.935870399439],
                              [  4.998907679456,  12.605939705669,  55.956125380937],
                              [  4.997123316032,   2.511973956415,  55.957018118676],
                              [  7.195015138136,   9.247746775485,  56.626446378552],
                              [  7.190927966984,   5.870327973619,  56.626760545017],
                              [  7.154511532304,   2.509388230778,  56.627407831507],
                              [  7.156218382352,  12.610669806559,  56.627453062582],
                              [  9.15677434928 ,   9.392474916715,  57.256251155487],
                              [  9.571187594888,   8.585448125542,  58.040567844772],
                              [  7.169991521024,   7.559953394608,  58.120748512969],
                              [  7.16279943416 ,  10.930967710138,  58.124793686181],
                              [  7.158702218984,   4.189981971485,  58.125727488038],
                              [  7.15527828908 ,   0.835973050706,  58.131537686013],
                              [  5.02027076756 ,   7.562621941594,  58.805298369812],
                              [  5.011311880304,   4.192666856295,  58.816706045531],
                              [  5.016346064816,  10.928800433843,  58.817566458969],
                              [  5.01036209744 ,   0.835602016674,  58.838111128129],
                              [  5.062636146056,   5.883672544204,  60.31257320513 ],
                              [  5.066676836384,   9.237250744856,  60.314900892999],
                              [  5.049483673616,  12.599357384843,  60.334693467079],
                              [  5.043543610448,   2.521061776971,  60.334956383473],
                              [  7.409560932536,   5.8506305553  ,  61.184001695609],
                              [  7.413980561048,   9.300225821137,  61.191012665378],
                              [  7.413308657672,   2.531353055833,  61.277662578715],
                              [  7.41712026044 ,  12.617714059704,  61.28181307057 ],
                              [  7.309328587736,   7.572992577103,  62.596360781849],
                              [  7.424332051976,   4.231801014969,  62.765153167305],
                              [  7.425833144216,  10.920115487321,  62.771598381008],
                              [  7.415805944816,   0.852808535847,  62.789720510273],
                              [  5.156754452144,   7.574293177909,  63.408979169715],
                              [  5.258566829144,   4.227134318578,  63.43643791631 ],
                              [  5.26076799464 ,  10.919348398554,  63.438793738374],
                              [  5.254904521568,   0.848320172647,  63.454396532653],
                              [  8.439015750104,   7.535659195777,  64.506592057401],
                              [  5.187102067976,   5.910614112811,  64.923950820366],
                              [  5.20500858716 ,   9.231470166703,  64.925572616511],
                              [  5.23443725144 ,   2.548626745887,  64.944408994216],
                              [  5.23868399228 ,  12.598325360104,  64.946421017584],
                              [  7.389239396408,  12.602651021239,  65.641061918914],
                              [  7.383315735392,   2.544594403233,  65.642557964552],
                              [  7.326063331064,   9.158815824505,  65.775282030654],
                              [  7.305138841616,   5.975072338068,  65.790229118322],
                              [  7.371138817352,   0.848192441798,  67.13745769623 ],
                              [  7.386117603176,  10.947383993737,  67.179722066705],
                              [  7.374800133248,   4.194106075821,  67.189994848964],
                              [  7.21432146164 ,   7.574073604312,  67.357937743787],
                              [  5.20113851408 ,   0.84870255263 ,  67.791977676577],
                              [  5.196895494272,  10.925838138125,  67.81910609786 ],
                              [  5.186196648656,   4.221621189511,  67.828152605059],
                              [  5.033862955112,   7.5770551652  ,  67.931505388466],
                              [  5.173193299928,  12.624322782011,  69.303349057531],
                              [  5.170314759056,   2.517587599985,  69.307846494315],
                              [  5.121219511208,   9.299721042299,  69.388899954549],
                              [  5.119509698744,   5.855600138437,  69.391327553394]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

VG=numpy.linspace(-1.5,2,8)
for vg in VG:
  # Add metallic region
  metallic_region_0 = BoxRegion(
    vg*Volt,
    xmin = 0.0*Angstrom, xmax = 0.5*Angstrom,
    ymin = 0.0*Angstrom, ymax = 13.4504*Angstrom,
    zmin = 8.33124080877*Angstrom, zmax = 61.095765931*Angstrom,
  )

  metallic_regions = [metallic_region_0]
  central_region.setMetallicRegions(metallic_regions)

  # Add dielectric region
  dielectric_region_0 = BoxRegion(
    3.9,
    xmin = 0.5*Angstrom, xmax = 4.0*Angstrom,
    ymin = 0.0*Angstrom, ymax = 13.4504*Angstrom,
    zmin = 8.33124080877*Angstrom, zmax = 61.095765931*Angstrom,
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
    GGABasis.Nitrogen_DoubleZetaPolarized,
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
  nlsave('Device_BP_O_Cu_52_5NO_%s.nc'%vg, device_configuration)

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
  nlsave('Device_BP_O_Cu_52_5NO_%s.nc'%vg, transmission_spectrum)
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

# # -------------------------------------------------------------
# # IV Curve
# # -------------------------------------------------------------
#   biases = [0.000000, 0.200000, 0.400000, 0.600000, 0.800000, 1.000000,
#           1.200000, 1.400000, 1.600000, 1.800000, 2.000000]*Volt

#   kpoint_grid = MonkhorstPackGrid()

#   iv_curve = IVCurve(
#     configuration=device_configuration,
#     biases=biases,
#     energies=numpy.linspace(-1,1,101)*eV,
#     kpoints=kpoint_grid,
#     self_energy_calculator=RecursionSelfEnergy(),
#     energy_zero_parameter=AverageFermiLevel,
#     infinitesimal=1e-06*eV,
#     selfconsistent_configurations_filename_prefix=NoCheckpointHandler,
#     log_filename_prefix=None
#     )
#   nlsave('Device_BP_O_Cu_52_5NO_%s.nc'%vg, iv_curve)
#   nlprint(iv_curve)

#   biases = [-0.200000, -0.400000, -0.600000, -0.800000, -1.000000,
#           -1.200000, -1.400000, -1.600000, -1.800000, -2.000000]*Volt

#   kpoint_grid = MonkhorstPackGrid()

#   iv_curve = IVCurve(
#     configuration=device_configuration,
#     biases=biases,
#     energies=numpy.linspace(-1,1,101)*eV,
#     kpoints=kpoint_grid,
#     self_energy_calculator=RecursionSelfEnergy(),
#     energy_zero_parameter=AverageFermiLevel,
#     infinitesimal=1e-06*eV,
#     selfconsistent_configurations_filename_prefix=NoCheckpointHandler,
#     log_filename_prefix=None
#     )
#   nlsave('Device_BP_O_Cu_52_5NO_%s.nc'%vg, iv_curve)
#   nlprint(iv_curve)

  # -------------------------------------------------------------
  # Electrostatic Difference Potential
  # -------------------------------------------------------------
  electrostatic_difference_potential = ElectrostaticDifferencePotential(device_configuration)
  nlsave('Device_BP_O_Cu_52_5NO_%s.nc'%vg, electrostatic_difference_potential)

  # -------------------------------------------------------------
  # Projected Local Density Of States
  # -------------------------------------------------------------
  kpoint_grid = MonkhorstPackGrid()

  projected_local_density_of_states = ProjectedLocalDensityOfStates(
    configuration=device_configuration,
    method=LocalDeviceDensityOfStates,
    energies=numpy.linspace(-2, 2, 101)*eV,
    kpoints=kpoint_grid,
    contributions=All,
    self_energy_calculator=RecursionSelfEnergy(),
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    )
  nlsave('Device_BP_O_Cu_52_5NO_%s.nc'%vg, projected_local_density_of_states)

  # -------------------------------------------------------------
  # Device Density Of States
  # -------------------------------------------------------------
  kpoint_grid = MonkhorstPackGrid()

  device_density_of_states = DeviceDensityOfStates(
    configuration=device_configuration,
    energies=numpy.linspace(-2,2,101)*eV,
    kpoints=kpoint_grid,
    contributions=All,
    energy_zero_parameter=AverageFermiLevel,
    infinitesimal=1e-06*eV,
    self_energy_calculator=RecursionSelfEnergy(),
    )
  nlsave('Device_BP_O_Cu_52_5NO_%s.nc'%vg, device_density_of_states)
  nlprint(device_density_of_states)
