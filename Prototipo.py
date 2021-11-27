"""
Prototipo Grupo: 90169_43
Versión 1.1
Creado por:
    John Wilmer Buitrago
    Juan Sebastián Cubillos
    Álvaro Javier Gutierrez
    Edna Katerine Ruiz
Propósito: Programa para diagnosticar la diabetes de un paciente, usando arboles de decisiones.
"""

# Importar librerias y arbol de deciciones tree, ver archivo: README.md
from sklearn import tree

# Función: diabetes, permite diagnosticar la enfermedad diabetes, por medio de sintomas.


def diabetes():
    # Creación de arbol de decision.
    clf = tree.DecisionTreeClassifier()

    # Creación de un menu guia para el usuario.
    print("INSTITUTO NACIONAL PARA EL DIAGNOSTICO DE LA DIABETES")
    print("Por favor digite los sintomas segun el numero")
    print("1. Aumento de la sed")
    print("2. Aumento del apetito")
    print("3. Fatiga")
    print("4. Vision borrosa")
    print("5. Entumecimiento en manos y pies")
    print("6. Ulceras que no cicatrizan")
    print("7. Perdida de peso sin motivo aparente")
    print("8. Ningun otro sintoma")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(" ")

    # Menu de seleccion de sitomas para el usuario.
    print("Digite los sintomas segun el numero")
    print("Primer Sintoma")
    sint1 = validationValueNumber()
    print("Segundo Sintoma")
    sint2 = validationValueNumber()
    print("Tercer Sintoma")
    sint3 = validationValueNumber()
    diagnostico = [sint1, sint2, sint3]
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Sintomas paciente")
    print("Las opciones escogidas fueron: ")
    print(diagnostico)

    # Alimentación de variables para entrenamiento del modelo.
    x = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 7], [2, 1, 3], [2, 4, 5], [2, 5, 7], [3, 1, 4], [3, 2, 4], [3, 4, 5], [3, 6, 7], [4, 1, 2], [4, 2, 3], [4, 5, 6], [4, 6, 7],
         [5, 1, 2], [5, 2, 3], [5, 4, 6], [5, 6, 7], [6, 1, 2], [6, 3, 4], [6, 5, 7], [
             7, 1, 2], [7, 3, 4], [7, 5, 6], [7, 6, 1], [1, 8, 8], [1, 3, 8], [1, 2, 8], [2, 3, 8],
         [1, 8, 8, ], [2, 8, 8], [3, 8, 8], [4, 8, 8], [5, 8, 8]]

    # Segun los sintomas indicados los resultados se indican con la siguiente variable.
    y = ['Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico',
         'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico',
         'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'Diabetico', 'No Diabetico', 'No Diabetico', 'No Diabetico',
         'No Diabetico', 'No Diabetico', 'No Diabetico', 'No Diabetico', 'No Diabetico', 'No Diabetico']

    # Asignación de datos a variables x + y.
    clf = clf.fit(x, y)

    # Con base a la predicción de los sintomas del modelo se muestra el diagnostico.
    prediccion = clf.predict([diagnostico])

    # Impresion en pantalla del resultado de la predicción.
    print("Diagnostico del paciente")
    print(prediccion)
    main()

# Función: Validar Número, obliga al usuario a digitar un número y solo un número


def validationValueNumber():
    while True:
        try:
            value = int(input("Digite valor "))
            break
        except:
            print("El valor digitado no es un número. Por favor vuelve a intentarlo")
    return value

# Función: Menu principal, permite ejecutar el programa, con menu de selección y opción de salida.


def main():
    print("")
    print("SISTEMA DE DIAGNOSTICO DE ENFERMEDADES")
    print("Desarrollado por: 90169_43")
    print("Opcion 0: Salir")
    print("Opcion 1: Diagnosticar Diabetes")
    print("")
    try:
        option = int(input("Seleccionar opcion "))
    except ValueError:
        print("La opcion seleccionada no es un numero. Por favor vuelve a intentarlo")
        main()
    while option != 0:
        if option == 1:
            diabetes()
        else:
            print("Opcion invalida")
            main()
    print("------------------------------------")
    exit()


main()
