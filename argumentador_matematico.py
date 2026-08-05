import random
ids = []
nombres = []
descripciones = []
operaciones = []
valores1 = []
valores2 = []
resultados = []
estados = []
observaciones = []
#--------------------------------------------#
#--|menu_principal_argumentador_matematico|--#
#--------------------------------------------#
while True:
    print("menu principal argumentador matematico")
    print("1) registrar argumento")
    print("2) editar argumento")
    print("3) eliminar argumento")
    print("4) buscar argumento")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-------------------------#
    #--|registrar_argumento|--#
    #-------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_argumento = 1
        else:
            id_argumento = ids[-1] + 1
        nombre = input("nombre del cálculo: ")
        descripcion = input("descripción: ")
        operacion = input("tipo de operación (suma, resta, multiplicacion, division, potencia, porcentaje): ").lower()
        valor1 = float(input("primer valor: "))
        valor2 = float(input("segundo valor: "))
        if operacion == "suma":
            resultado = valor1 + valor2
        elif operacion == "resta":
            resultado = valor1 - valor2
        elif operacion == "multiplicacion":
            resultado = valor1 * valor2
        elif operacion == "division":
            if valor2 != 0:
                resultado = valor1 / valor2
            else:
                resultado = 0
        elif operacion == "potencia":
            resultado = valor1 ** valor2
        elif operacion == "porcentaje":
            resultado = valor1 * (valor2 / 100)
        else:
            resultado = 0
        estado = input("estado (correcto o pendiente de revisión): ")
        observacion = input("observación: ")
        ids.append(id_argumento)
        nombres.append(nombre)
        descripciones.append(descripcion)
        operaciones.append(operacion)
        valores1.append(valor1)
        valores2.append(valor2)
        resultados.append(resultado)
        estados.append(estado)
        observaciones.append(observacion)
        print("argumento registrado correctamente.")
        print("id:", id_argumento)
        print("resultado:", format(resultado, ".2f"))
    #----------------------#
    #--|editar_argumento|--#
    #----------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen argumentos registrados.")
        else:
            print("editar argumento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {operaciones[i]} | {resultados[i]:.2f}")
            id_buscar = int(input("ingrese la id del argumento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {operaciones[posicion]}")
                nombres[posicion] = input("nuevo nombre: ")
                descripciones[posicion] = input("nueva descripción: ")
                operaciones[posicion] = input("nueva operación: ").lower()
                valores1[posicion] = float(input("nuevo primer valor: "))
                valores2[posicion] = float(input("nuevo segundo valor: "))
                if operaciones[posicion] == "suma":
                    resultados[posicion] = valores1[posicion] + valores2[posicion]
                elif operaciones[posicion] == "resta":
                    resultados[posicion] = valores1[posicion] - valores2[posicion]
                elif operaciones[posicion] == "multiplicacion":
                    resultados[posicion] = valores1[posicion] * valores2[posicion]
                elif operaciones[posicion] == "division":
                    if valores2[posicion] != 0:
                        resultados[posicion] = valores1[posicion] / valores2[posicion]
                    else:
                        resultados[posicion] = 0
                elif operaciones[posicion] == "potencia":
                    resultados[posicion] = valores1[posicion] ** valores2[posicion]
                elif operaciones[posicion] == "porcentaje":
                    resultados[posicion] = valores1[posicion] * (valores2[posicion] / 100)
                else:
                    resultados[posicion] = 0
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("argumento actualizado correctamente.")
                print("nuevo resultado:", format(resultados[posicion], ".2f"))
            else:
                print("id no encontrada.")
    #------------------------#
    #--|eliminar_argumento|--#
    #------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen argumentos registrados.")
        else:
            print("eliminar argumento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {operaciones[i]}")
            id_buscar = int(input("ingrese la id del argumento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del argumento")
                print(f"{ids[posicion]} | {nombres[posicion]} | {operaciones[posicion]}")
                respuesta = input("¿desea eliminar este argumento? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    descripciones.pop(posicion)
                    operaciones.pop(posicion)
                    valores1.pop(posicion)
                    valores2.pop(posicion)
                    resultados.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("argumento eliminado correctamente.")
                else:
                    print("el argumento no fue eliminado.")
            else:
                print("id no encontrada.")
    #----------------------#
    #--|buscar_argumento|--#
    #----------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen argumentos registrados.")
        else:
            print("buscar argumento")
            id_buscar = int(input("ingrese la id del argumento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("descripción:", descripciones[posicion])
                print("operación:", operaciones[posicion])
                print("primer valor:", valores1[posicion])
                print("segundo valor:", valores2[posicion])
                print("resultado:", format(resultados[posicion], ".2f"))
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen argumentos registrados.")
        else:
            sumas = 0
            restas = 0
            multiplicaciones = 0
            divisiones = 0
            potencias = 0
            porcentajes = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {operaciones[i]} | {resultados[i]:.2f}")
                if operaciones[i] == "suma":
                    sumas += 1
                elif operaciones[i] == "resta":
                    restas += 1
                elif operaciones[i] == "multiplicacion":
                    multiplicaciones += 1
                elif operaciones[i] == "division":
                    divisiones += 1
                elif operaciones[i] == "potencia":
                    potencias += 1
                elif operaciones[i] == "porcentaje":
                    porcentajes += 1
            print("estadísticas argumentador matematico")
            print("cantidad de operaciones:", len(ids))
            print("sumas realizadas:", sumas)
            print("restas realizadas:", restas)
            print("multiplicaciones realizadas:", multiplicaciones)
            print("divisiones realizadas:", divisiones)
            print("potencias realizadas:", potencias)
            print("porcentajes realizados:", porcentajes)
            posicion = random.randint(0, len(ids) - 1)
            print("argumento matematico seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("descripción:", descripciones[posicion])
            print("operación:", operaciones[posicion])
            print("primer valor:", valores1[posicion])
            print("segundo valor:", valores2[posicion])
            print("resultado:", format(resultados[posicion], ".2f"))
            print("estado:", estados[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el argumentador matematico.")
        break
    else:
        print("opción no válida.")