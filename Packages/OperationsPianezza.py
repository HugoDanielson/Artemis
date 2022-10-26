from Packages.database import *


def rough_face_thick(Diameter, iDiam, Thickness, Channel):
    d = {'d': iDiam}
    D = {'D': Diameter}
    B = {'B': Thickness}
    Cnl = {'Channel': Channel}

    if Diameter >= 47 and Diameter <= 160:
        thickness_max = 50
        thickness_min = 30
        # Vbe/i
        thick_delta = 10
        # Spe/i
        machine_desig = 'S-SgrFac'
        machine_number = 'S-SgrFac'

    elif Diameter > 160 and Diameter <= 400:

        thickness_max = 70
        thickness_min = 50
        thick_delta = 20

        # Spe/i
        machine_desig = 'S-SgrFac'
        machine_number = 'S-SgrFac'

    elif Diameter > 400 and Diameter <= 600:

        thickness_max = 70
        thickness_min = 50

        # Vbe/i
        thick_delta = 20
        # Spe/i
        machine_desig = 'S-SgrFac'
        machine_number = 'S-SgrFac'

    else:
        pass

    try:

        rough_thickname = {'Measurement': 'Spessore/Parallelismo '}
        B_nom = {'nom': Thickness}
        B_max = {'max': thickness_max}
        B_min = {'min': thickness_min}
        B_delta = {'delta': thick_delta}
        M_desig = {'M_desig': machine_desig}
        M_num = {'M_num': machine_number}

        return [d, D, B, rough_thickname, B_nom, B_min, B_max, B_delta, M_desig, M_num, Cnl]
    except:
        pass
def rough_face_plan(Diameter, iDiam, Thickness, Channel):
    d = {'d': iDiam}
    D = {'D': Diameter}
    B = {'B': Thickness}
    Cnl = {'Channel': Channel}


    if Diameter >= 47 and Diameter <= 160:
        # Vbe/i


        # Spe/i
        planar_delta = 10

        machine_desig = 'S-SgrFac'
        machine_number = 'S-SgrFac'

    elif Diameter > 160 and Diameter <= 400:


        # Spe/i
        planar_delta = 20

        machine_desig = 'S-SgrFac'
        machine_number = 'S-SgrFac'

    elif Diameter > 400 and Diameter <= 600:



        # Spe/i
        planar_delta = 20

        machine_desig = 'S-SgrFac'
        machine_number = 'S-SgrFac'

    else:
        pass

    try:
        rough_plname = {'Measurement': 'Planarità'}
        Pl_nom = {'nom': 0}
        Pl_min = {'min': 0}
        Pl_max = {'max': 0}
        Pl_delta = {'delta': planar_delta}
        M_desig = {'M_desig': machine_desig}
        M_num = {'M_num': machine_number}

        return [d, D, B, rough_plname, Pl_nom, Pl_min, Pl_max, Pl_delta, M_desig, M_num,Cnl]
    except:
        pass
def rough_outer_di(Diameter, iDiam, Thickness, Channel):
    d = {'d': iDiam}
    D = {'D': Diameter}
    B = {'B': Thickness}
    Cnl = {'Channel': Channel}


    if Channel == "Channel 6" and Diameter >160 and Diameter <= 200:
        diam_max = 150
        diam_min = 120
        # vdsp
        diam_delta = 10

        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'


    elif Diameter >= 47 and Diameter < 145:

        diam_max = 100
        diam_min = 80
        # vdsp
        diam_delta = 10
        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'

    elif Diameter >= 145 and Diameter <= 260:

        diam_max = 150
        diam_min = 120
        # vdsp
        diam_delta = 10
        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'
    else:
        pass

    try:
        rough_out_Diam_name = {'Measurement': 'Diametro/Ovalità'}
        D_nom = {'nom': Diameter}
        D_min = {'min': diam_min}
        D_max = {'max': diam_max}
        D_delta = {'delta': diam_delta}
        M_desig = {'M_desig': machine_desig}
        M_num = {'M_num': machine_number}

        return [d, D, B, rough_out_Diam_name, D_nom, D_min, D_max, D_delta, M_desig, M_num,Cnl]
    except:
        return None
def rough_outer_con(Diameter, iDiam, Thickness, Channel):
    d = {'d': iDiam}
    D = {'D': Diameter}
    B = {'B': Thickness}
    Cnl = {'Channel': Channel}


    if Channel == "Channel 6" and Diameter >160 and Diameter <= 200:

        # Vdmp
        conicita = 20


        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'


    elif Diameter >= 47 and Diameter < 145:



        # Vdmp
        conicita = 20


        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'

    elif Diameter >= 145 and Diameter <= 260:


        conicita = 20


        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'
    else:
        pass

    try:
        rough_out_con_name = {'Measurement': 'Conicità'}
        Con_nom = {'nom': Diameter}
        Con_min = {'min': 0}
        Con_max = {'max': 0}
        Con_delta = {'delta': conicita}
        M_desig = {'M_desig': machine_desig}
        M_num = {'M_num': machine_number}

        return [d, D, B, rough_out_con_name, Con_nom, Con_min, Con_max,Con_delta, M_desig, M_num, Cnl]
    except:
        pass
def rough_outer_poly(Diameter, iDiam, Thickness, Channel):
    d = {'d': iDiam}
    D = {'D': Diameter}
    B = {'B': Thickness}
    Cnl = {'Channel': Channel}


    if Channel == 'Channel 6' and Diameter >160 and Diameter <= 200:

        # V3d
        poligonarita = 10

        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'


    elif Diameter >= 47 and Diameter < 145:


        # V3d
        poligonarita = 10

        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'

    elif Diameter >= 145 and Diameter <= 260:

        #V3d
        poligonarita = 10

        machine_desig = 'SgrossDiam'
        machine_number = 'S-SgrDiam'

    else:
        pass

    try:
        rough_out_pol_name = {'Measurement': 'Poligonalità'}
        Pol_nom = {'nom': 0}
        Pol_min = {'min': 0}
        Pol_max = {'max': 0}
        Pol_delta = {'delta': poligonarita}
        M_desig = {'M_desig': machine_desig}
        M_num = {'M_num': machine_number}

        return [d, D, B, rough_out_pol_name, Pol_nom, Pol_min, Pol_max, Pol_delta, M_desig, M_num, Cnl]
    except:
        pass
def seal_turn_tol ():
    pass
def finish_face_thick(Diameter, iDiam, Thickness, Channel):
    d = {'d': iDiam}
    D = {'D': Diameter}
    B = {'B': Thickness}
    Cnl = {'Channel': Channel}

    thickness_max = -10
    thickness_min = -15
    thick_delta = 2
    machine_desig = 'Face Finish Group'
    machine_number = 'S-FaceF'

    try:

        rough_thickname = {'Measurement': 'Spessore'}
        B_nom = {'nom': Thickness}
        B_max = {'max': thickness_max}
        B_min = {'min': thickness_min}
        B_delta = {'delta': thick_delta}
        M_desig = {'M_desig': machine_desig}
        M_num = {'M_num': machine_number}

        return [d, D, B, rough_thickname, B_nom, B_min, B_max, B_delta, M_desig, M_num, Cnl]
    except:
        pass
def finish_face_plan(Diameter, iDiam, Thickness, Channel,Spe):
    d = {'d': iDiam}
    D = {'D': Diameter}
    B = {'B': Thickness}
    Cnl = {'Channel': Channel}
    machine_desig = 'Face Finish Group'
    machine_number = 'S-FaceF'


    try:
        rough_plname = {'Measurement': 'Planarità'}
        Pl_nom = {'nom': 0}
        Pl_min = {'min': 0}
        Pl_max = {'max': 0}
        Pl_delta = {'delta': Spe}
        M_desig = {'M_desig': machine_desig}
        M_num = {'M_num': machine_number}

        return [d, D, B, rough_plname, Pl_nom, Pl_min, Pl_max, Pl_delta, M_desig, M_num,Cnl]
    except:
        pass
def finish_face_paral(Diameter, iDiam, Thickness, Channel,Vbe):
    d = {'d': iDiam}
    D = {'D': Diameter}
    B = {'B': Thickness}
    Cnl = {'Channel': Channel}
    machine_desig = 'Face Finish Group'
    machine_number = 'S-FaceF'



    try:
        rough_plname = {'Measurement': 'Parallelismo'}
        Pl_nom = {'nom': 0}
        Pl_min = {'min': 0}
        Pl_max = {'max': 0}
        Pl_delta = {'delta': Vbe}
        M_desig = {'M_desig': machine_desig}
        M_num = {'M_num': machine_number}

        return [d, D, B, rough_plname, Pl_nom, Pl_min, Pl_max, Pl_delta, M_desig, M_num,Cnl]
    except:
        pass
def saveTolerances(workbook,longname =None, shortname=None):
    bearing_data = {}
    bearing_data_long = {}

    if longname == None and shortname != None:
        longname = shortname + "long"
    elif shortname == None and longname != None:
        shortname= longname +"short"
    elif longname == None and shortname == None:
        shortname = "Data/BearingData2.p"
        longname = "Data/BearingData1.p"

    for indx in range(len(workbook['Tipo'])):

        tipo = workbook['Tipo'].loc[indx]


        dd = workbook['d'].loc[indx]

        DD = workbook['D'].loc[indx]

        BB = workbook['B'].loc[indx]

        CC = workbook['Channel'].loc[indx]


        FFspe = workbook['Spe'].loc[indx]
        FFvbe = workbook['Vbe'].loc[indx]



        if DD < 47:
            pass
        elif CC == 'Channel 7' or CC == 'Channel 4B':
            RoughFace1 = rough_face_thick(DD, dd, BB, CC)
            RoughFace2 = rough_face_plan(DD, dd, BB, CC)

            FaceFinish1 = finish_face_thick(DD, dd, BB, CC)
            FaceFinish2 = finish_face_plan(DD, dd, BB, CC, FFspe)
            FaceFinish3 = finish_face_paral(DD, dd, BB, CC, FFvbe)

            bearing_data[str(tipo)] = RoughFace1, RoughFace2, FaceFinish1, FaceFinish2, FaceFinish3

        else:
            RoughFace1 = rough_face_thick(DD, dd, BB, CC)
            RoughFace2 = rough_face_plan(DD, dd, BB, CC)

            RoughOuter1 = rough_outer_di(DD, dd, BB, CC)
            RoughOuter2 = rough_outer_con(DD, dd, BB, CC)
            RoughOuter3 = rough_outer_poly(DD, dd, BB, CC)

            FaceFinish1 = finish_face_thick(DD, dd, BB, CC)
            FaceFinish2 = finish_face_plan(DD, dd, BB, CC, FFspe)
            FaceFinish3 = finish_face_paral(DD, dd, BB, CC, FFvbe)

            bearing_data_long[
                str(tipo)] = RoughFace1, RoughFace2, RoughOuter1, RoughOuter2, RoughOuter3, FaceFinish1, FaceFinish2, FaceFinish3


        try:
            print(bearing_data[str(tipo)])
        except:
            print('No Data Dump')

    print("Data Saved in", longname, "and", shortname)

    save(path=shortname, data=bearing_data)
    save(path=longname, data=bearing_data_long)


