#Introducción
print("-----------------")
print("Paises y animales")
print("-----------------")

#Obtención del nombre
nombre = str(input("Ingrese su nombre: "))
print(f"Bienvenido/a al programa {nombre}\n")

print("Indicaciones:\nEscriba la palabra o el numero de cualquiera de las opciones.\n")

#Variables
#Paises
pais1 = "El Salvador"
pais2 = "Guatemala"
pais3 = "Honduras"
pais4 = "Nicaragua"
pais5 = "Costa Rica"
pais6 = "Panamá"
pais7 = "Brasil"
pais8 = "Colombia"
pais9 = "Perú"
pais10 = "Argentina"

#Animales
especie1 = "canina"
especie2 = "felina"
especie3 = "porcina"
especie4 = "bovina"
especie5 = "equina"
especie6 = "ursidae"
especie7 = "accipítridos"
especie8 = "psitácidos"
especie9 = "arácnida"
especie10 = "faisánidos"

#Elegir un tema
x = 1
while x:
    tema = input("""\tElija el tema:\n\t1- Paises\n\t2- Animales\n\nQue tema quiere elegir -> """).lower()
    print()

    if tema == "paises".lower() or tema == "animales".lower() or tema == "1" or tema == "2":

        while tema:
            #Elegir un pais para determinar su gentilicio
            if tema == "paises".lower() or tema == "1":
                print("Elija el pais del que quiera saber su gentilicio:")
                pais = input(f"\tLista de paises:\n\t1- {pais1}\n\t2- {pais2}\n\t3- {pais3}\n\t4- {pais4}\n\t5- {pais5}\n\t6- {pais6}\n\t7- {pais7}\n\t8- {pais8}\n\t9- {pais9}\n\t10- {pais10}\n\nElija un pais -> ").lower()
                print()

                if pais == "el salvador".lower() or pais == "1":
                    print(f"El gentilicio de {pais1} es: Salvadoreño/a\n")
                    break

                elif pais == "guatemala".lower() or pais == "2":
                    print(f"El gentilicio de {pais2} es: Guatemalteco/a\n")
                    break

                elif pais == "honduras".lower() or pais == "3":
                    print(f"El gentilicio de {pais3} es: Hondureño/a\n")
                    break

                elif pais == "nicaragua".lower() or pais == "4":
                    print(f"El gentilicio de {pais4} es: Nicaragüense\n")
                    break

                elif pais == "costa rica".lower() or pais == "5":
                    print(f"El gentilicio de {pais5} es: Costarricense\n")
                    break

                elif pais == "panamá".lower() or pais == "6":
                    print(f"El gentilicio de {pais6} es: Panameño/a\n")
                    break

                elif pais == "brasil".lower() or pais == "7":
                    print(f"El gentilicio de {pais7} es: Brasileño/a\n")
                    break

                elif pais == "colombia".lower() or pais == "8":
                    print(f"El gentilicio de {pais8} es: Colombiano/a\n")
                    break

                elif pais == "perú".lower() or pais == "9":
                    print(f"El gentilicio de {pais9} es: Peruano/a\n")
                    break

                elif pais == "argentina".lower() or pais == "10":
                    print(f"El gentilicio de {pais10} es: Argentino/a\n")
                    break

                else:
                    print("Esa no es una opción válida")
                    break

            #Elegir un animal para determinar su familia
            if tema == "animales".lower() or tema == "2":
                print("Elija el animal del que quiera saber su familia:")
                animal = input(f"\tLista de animales:\n\t1- {especie1}\n\t2- {especie2}\n\t3- {especie3}\n\t4- {especie4}\n\t5- {especie5}\n\t6- {especie6}\n\t7- {especie7}\n\t8- {especie8}\n\t9- {especie9}\n\t10- {especie10}\n\nElija el animal -> ")
                print()

                if animal == "canina".lower() or animal == "1":
                    print(f"Los animales de la familia {especie1} son: perros, lobo, zorro, coyote, chacal, etc.\n")
                    break

                elif animal == "felina".lower() or animal == "2":
                    print(f"Los animales de la familia {especie2} son: gato, tigre, leon, leopardo, etc.\n")
                    break

                elif animal == "porcina".lower() or animal == "3":
                    print(f"Los animales de la familia {especie3} son: cerdo, jabalí.\n")
                    break
                
                elif animal == "bovina".lower() or animal == "4":
                    print(f"Los animales de la familia {especie4} son: vaca, toro, buey, búfalo, ñu, etc.\n")
                    break
                
                elif animal == "equina".lower() or animal == "5":
                    print(f"Los animales de la familia {especie5} son: caballo, mula, asno, macho, etc.\n")
                    break
                
                elif animal == "ursidae".lower() or animal == "6":
                    print(f"Los animales de la familia {especie6} son: oso pardo, oso polar, oso negro, etc.\n")
                    break
                
                elif animal == "accipítridos".lower() or animal == "7":
                    print(f"Los animales de la familia  de {especie7} son: milanos, aguilillas, gavilanes Y águilas, etc.\n")
                    break
                
                elif animal == "psitácidos".lower() or animal == "8":
                    print(f"Los animales de la familia de {especie8} son: guacamayos, cotorras, loros, papagayos,etc.\n")
                    break
                
                elif animal == "arácnida".lower() or animal == "9":
                    print(f"Los animales de la familia {especie9} son: arañas, escorpiones, alacranes, etc.\n")
                    break
                
                elif animal == "faisánidos".lower() or animal == "10":
                    print(f"Los animales de la familia de {especie10} son: gallos, faisanes, meleagris, pavos, perdices, etc.\n")
                    break
                
                else:
                    print("Esa no es una opción válida")
                    break

    else:
        print("\nEsa no es una opción válida")

    #Reinicio del programa a petición del usuario
    reset = input("Desea volver a empezar(si o no) -> ").lower()
            
    if reset == "si".lower():
            print()

    else:
        break

print("\nFin del programa")