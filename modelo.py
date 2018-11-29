# -*- coding: utf-8 -*-
salida ="seleccionaste la opcion: "
separador ="*********************************************************************\n"
# Se definen las opciones que se mostraran
opcion1   = ["Dolor de cabeza", "Alteraciones de la visión", "Mareos", "Alteraciones del oído"]
opcion11  = ["Fiebre", "Problemas de tensión", "Perdida de la conciencia"]
opcion111 = ["Latidos irregulares", "Dificultad para respirar"]
opcion112 = ["Tensión alta", "Tensión baja"]
opcion113 = ["Desmayos", "Dificultad para respirar"]
opcion12   = ["Nauseas", "Molestias en el pecho", "Vértigo"]
opcion121  = ["Sensación de pesadez", "Dolor de cabeza"]
opcion122  = ["Fatiga", "Dolor en el tórax"]
opcion123  = ["Latidos irregulares", "Perdida de la conciencia"]
opcion13   = ["Visión borrosa", "Enrojecimiento de los ojos", "Dilatación de pupilas"]
opcion131  = ["Desmayos", "Dolor de cabeza"]
opcion132  = opcion112
opcion133  = ["Dolor de cabeza", "Problemas de tensión"]
opcion14   = ["Pitidos", "Dolor intenso", "Sordera parcial"]
opcion141  = opcion113
opcion142  = ["Fatiga", "Dolor de cabeza"]
opcion143  = ["Vértigo", "Perdida de la conciencia"]
#Definición de enfermedades
cerebrovascular = (separador+
                  "         Según sus síntomas, usted podría padecer de: Enfermedad cerebrovascular \n\n" +
                  "         En este caso también se encuentran afectados\n" +
                  "         los vasos que irrigan sangre y oxígeno al cerebro. Puede provocar\n" +
                  "         afectaciones permanentes, o bien  momentáneas, en el cerebro\n"+
                  separador+"\n")
insuficienciaCardiaca= (separador+
                  "         Según sus síntomas, usted podría padecer de: Insuficiencia cardiaca \n\n" +
                  "         Está caracterizada por una dificultad de la bomba\n"+
                  "         muscular (el corazón) para bombear sangre de manera regular. También es\n"+
                  "         conocida como insuficiencia cardiaca congestiva\n"+
                  separador+"\n")
hipertensionArterial= (separador+
                  "         Según sus síntomas, usted podría padecer de: Hipertensión arterial \n\n" +
                  "         Conocida también como presión alta, se presenta cuando\n" +
                  "         los niveles de presión marcan un mínimo de 140 mmHg de presión sistólica; o 90 mmHg\n" +
                  "         de presión diastólica. Indicadores de que la sangre no está viajando por los vasos de\n"+
                  "         manera adecuada y fluida, lo que puede provocar un ataque cardiaco.\n"+
                  separador+"\n")
cardiopatiaCoronaria= (separador+
                  "         Según sus síntomas, usted podría padecer de: Cardiopatía coronaria \n\n" +
                  "         En este caso se ven afectados los vasos sanguíneos que se encargan de llevar sangre al corazón.\n"+
                  "         Se caracteriza por un estrechamiento de estos últimos, lo que impide que llegue suficiente\n"+
                  "         sangre y oxígeno a la bomba muscular.\n"+
                  separador+"\n")
cardiopatiaReumatica= (separador+
                  "         Según sus síntomas, usted podría padecer de: Cardiopatía reumática \n\n" +
                  "         Se origina por la inflamación que ocasiona la fiebre reumática\n" +
                  "         (una respuesta patológica del organismo ante infecciones ocasionadas por bacterias estreptocócicas).\n" +
                  "         La principal característica de la cardiopatía reumática es la existencia de una lesión de las válvulas\n"+
                  "         cardiacas y el miocardio.\n"+
                  separador+"\n")
cardiopatiaCongenita= (separador+
                  "         Según sus síntomas, usted podría padecer de: Cardiopatía congénita \n\n" +
                  "         La principal característica es la existencia de malformaciones\n"+
                  "         del corazón que se presentan desde el nacimiento. Puede ser de tipo cianótica o no cianótica,\n"+
                  "         según si se manifiesta también con una falta de oxígeno. Los síntomas de la cardiopatía varían\n"+
                  "         según el desarrollo de la misma patología..\n"+
                  separador+"\n")
#Se genera el encabezado
print("\n\n"+
      separador +
      "           Diagnóstico de Enfermedades Sistema Cardiovascular\n\n" +
      "           Elaborado por: Grupo 45 de Inteligencia Artificial\n\n"+
      separador +
      "¿Qué estas sintiendo ahora?:\n")
#Con un ciclo se pintan las opciones principales en base a la lista opcion1
for i in  range(len(opcion1)):
    print(str(i+1) ,") " + opcion1[i])
sintoma1 = input("\n- Digite el número de acuerdo al sintoma: ")
#Se empieza el manejo de los ciclos de desición
if sintoma1=="1":
    print(salida + opcion1[int(sintoma1)-1] + "\n")
    print(separador + "¿Qué otro sintoma presenta?:\n")
    for i in  range(len(opcion11)):
        print(str(i+1) ,") " + opcion11[i])
    sintoma2 = input("\n- Digite otra opción: ")
    if sintoma2 == "1":
        print(salida + opcion11[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion111)):
            print(str(i+1) ,") " + opcion111[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion111[int(sintoma3)-1]) + "\n")
            print(cerebrovascular)
        elif sintoma3 == "2":
            print(salida + (opcion111[int(sintoma3)-1]) + "\n")
            print(insuficienciaCardiaca)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n")   
    elif sintoma2 == "2":
        print(salida + opcion11[int(sintoma2)-1] + "\n")
        print(separador +"¿Además tiene?:\n" )
        for i in  range(len(opcion112)):
            print(str(i+1) ,") " + opcion112[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion112[int(sintoma3)-1]) + "\n")
            print(hipertensionArterial)
        elif sintoma3 == "2":
            print(salida + (opcion112[int(sintoma3)-1]) + "\n")
            print(cardiopatiaCoronaria)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n")   
    elif sintoma2 == "3":
        print(salida + opcion11[int(sintoma2)-1] + "\n")
        print(separador +"¿Además tiene?:\n" )
        for i in  range(len(opcion113)):
            print(str(i+1) ,") " + opcion113[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion113[int(sintoma3)-1]) + "\n")
            print(cardiopatiaReumatica)
        elif sintoma3 == "2":
            print(salida + (opcion113[int(sintoma3)-1]) + "\n")
            print(cardiopatiaCongenita)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
elif sintoma1=="2":
    print(salida + opcion1[int(sintoma1)-1] + "\n")
    print(separador + "¿Qué otro sintoma presenta?:\n")
    for i in  range(len(opcion12)):
        print(str(i+1) ,") " + opcion12[i])
    sintoma2 = input("\n- Digite otra opción: ")
    if sintoma2 == "1":
        print(salida + opcion12[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion121)):
            print(str(i+1) ,") " + opcion121[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion121[int(sintoma3)-1]) + "\n")
            print(cardiopatiaReumatica)
        elif sintoma3 == "2":
            print(salida + (opcion121[int(sintoma3)-1]) + "\n")
            print(cerebrovascular)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
    elif sintoma2 == "2":
        print(salida + opcion12[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion122)):
            print(str(i+1) ,") " + opcion122[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion122[int(sintoma3)-1]) + "\n")
            print(cardiopatiaCoronaria)
        elif sintoma3 == "2":
            print(salida + (opcion122[int(sintoma3)-1]) + "\n")
            print(insuficienciaCardiaca)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
    elif sintoma2 == "3":
        print(salida + opcion12[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion123)):
            print(str(i+1) ,") " + opcion123[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion123[int(sintoma3)-1]) + "\n")
            print(hipertensionArterial)
        elif sintoma3 == "2":
            print(salida + (opcion123[int(sintoma3)-1]) + "\n")
            print(cardiopatiaCongenita)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
elif sintoma1=="3":
    print(salida + opcion1[int(sintoma1)-1] + "\n")
    print(separador + "¿Qué otro sintoma presenta?:\n")
    for i in  range(len(opcion13)):
        print(str(i+1) ,") " + opcion13[i])
    sintoma2 = input("\n- Digite otra opción: ")
    if sintoma2 == "1":
        print(salida + opcion13[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion131)):
            print(str(i+1) ,") " + opcion131[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion131[int(sintoma3)-1]) + "\n")
            print(cardiopatiaCoronaria)
        elif sintoma3 == "2":
            print(salida + (opcion131[int(sintoma3)-1]) + "\n")
            print(cerebrovascular)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
    elif sintoma2 == "2":
        print(salida + opcion13[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion132)):
            print(str(i+1) ,") " + opcion132[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion132[int(sintoma3)-1]) + "\n")
            print(hipertensionArterial)
        elif sintoma3 == "2":
            print(salida + (opcion132[int(sintoma3)-1]) + "\n")
            print(insuficienciaCardiaca)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
    elif sintoma2 == "3":
        print(salida + opcion13[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion133)):
            print(str(i+1) ,") " + opcion133[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion133[int(sintoma3)-1]) + "\n")
            print(cardiopatiaCongenita)
        elif sintoma3 == "2":
            print(salida + (opcion133[int(sintoma3)-1]) + "\n")
            print(cardiopatiaReumatica)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n")               
elif sintoma1=="4":
    print(salida + opcion1[int(sintoma1)-1] + "\n")
    print(separador + "¿Qué otro sintoma presenta?:\n")
    for i in  range(len(opcion14)):
        print(str(i+1) ,") " + opcion14[i])
    sintoma2 = input("\n- Digite otra opción: ")
    if sintoma2 == "1":
        print(salida + opcion14[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion141)):
            print(str(i+1) ,") " + opcion141[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion141[int(sintoma3)-1]) + "\n")
            print(cardiopatiaCongenita)
        elif sintoma3 == "2":
            print(salida + (opcion141[int(sintoma3)-1]) + "\n")
            print(insuficienciaCardiaca)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
    elif sintoma2 == "2":
        print(salida + opcion14[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion142)):
            print(str(i+1) ,") " + opcion142[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion142[int(sintoma3)-1]) + "\n")
            print(hipertensionArterial)
        elif sintoma3 == "2":
            print(salida + (opcion142[int(sintoma3)-1]) + "\n")
            print(cerebrovascular)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
    elif sintoma2 == "3":
        print(salida + opcion14[int(sintoma2)-1] + "\n")
        print(separador +"¿Además siente?:\n" )
        for i in  range(len(opcion143)):
            print(str(i+1) ,") " + opcion143[i])
        sintoma3 = input("\n- Digite una opción:")
        if sintoma3 == "1":
            print(salida + (opcion143[int(sintoma3)-1]) + "\n")
            print(cardiopatiaReumatica)
        elif sintoma3 == "2":
            print(salida + (opcion143[int(sintoma3)-1]) + "\n")
            print(cardiopatiaCoronaria)
        else:
            print(separador+
                  "         La Opción " +sintoma3 +", no es valida \n" +
                  separador+"\n") 
    else:
        print(separador+
              "         La Opción " +sintoma2 +", no es valida \n" +
              separador+"\n") 
else:
    print(separador+
            "         La Opción " +sintoma1 +", no es valida \n" +
            separador+"\n") 
