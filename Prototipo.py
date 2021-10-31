def diabetes():
    from sklearn import tree
    #importar librerias y arbol de deciciones tree
    #creacion de arbol de decision
    clf=tree.DecisionTreeClassifier()
    #creacion de un menu guia para el usuario
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

    #menu de seleccion de sitomas para el usuario
    print("Digite los sintomas segun el numero")
    sint1=input("Primer Sintoma ")
    sint2=input("Segundo Sintoma ")
    sint3=input("Tercer Sintoma ")
    diagnostico=[sint1,sint2,sint3]
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Sintomas paciente")
    print("Las opciones escogidas fueron: ")
    print(diagnostico)

    #alimentacion de variables para entrenamiento del modelo
    x=[[1,2,3],[1,2,4],[1,2,5],[1,2,7],[2,1,3],[2,4,5],[2,5,7],[3,1,4],[3,2,4],[3,4,5],[3,6,7],[4,1,2],[4,2,3],[4,5,6],[4,6,7],
    [5,1,2],[5,2,3],[5,4,6],[5,6,7],[6,1,2],[6,3,4],[6,5,7],[7,1,2],[7,3,4],[7,5,6],[7,6,1],[1,8,8],[1,3,8],[1,2,8],[2,3,8],
    [1,8,8,],[2,8,8],[3,8,8],[4,8,8],[5,8,8]]
    #segun los sintomas indicados los resultados se indican con la siguiente variable
    y=['Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico',
    'Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico',
    'Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','Diabetico','No Diabetico','No Diabetico','No Diabetico',
    'No Diabetico','No Diabetico','No Diabetico','No Diabetico','No Diabetico','No Diabetico']

    #asignacion de datos a variables x y y
    clf=clf.fit(x,y)

    #en base a la prediccion de los sintomas del modelo se muestra el diagnostico
    prediccion=clf.predict([diagnostico])

    #sub-menu que imprime el resultado en pantalla
    print("Diagnostico del paciente")
    print(prediccion)
    main()

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
        print("La opcion seleccionada no es un numero, Por favor vuelve a intentarlo")
        main()
    while option != 0:
        if option == 1:
            diabetes()
        else:
            print("Opcion invalida")
    print("------------------------------------")
    exit()
main()