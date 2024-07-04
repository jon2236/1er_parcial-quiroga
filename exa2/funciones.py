from random import randint, choice
from os import system

def limpiar_pantalla():
    system("cls")

def pausar():
    system("pause")

def cargar_archivo_csv(nombre_archivo_data:str, lista):
    """_summary_
    
    Args:
        nombre_archivo_data (str): Nombre del archivo de donde se obtendra la info
    """
    try:
        with open(get_path_actual(nombre_archivo_data), "r", encoding="utf-8") as archivo:
            encabezado = archivo.readline().strip("\n").split(",")
        
            for linea in archivo.readlines():
                bicicleta = {}
                linea = linea.strip("\n").split(",")
                id_bike, nombre, tipo, tiempo = linea
                bicicleta["id_bike"] = int(id_bike)
                bicicleta["nombre"] = nombre
                bicicleta["tipo"] = tipo
                bicicleta["tiempo"] = int(tiempo)
                
                lista.append(bicicleta)
    except:
        raise ValueError("no existe el archivo con ese nombre ingresado")

def menu()->str:
    """_summary_

    Returns:
        str: Menu de stark
    """
    limpiar_pantalla()
    print("////////competidores Menu////////")
    print("1-Cargar Archivo.CSV")
    print("2-Imprimir lista")
    print("3-Asignar tiempos")
    print("4-Informar ganador")
    print("5-Filtrar por tipo")
    print("6-Informar promedio por tipo")
    print("7-Mostrar posiciones")
    print("8-Guardar posiciones(Archivo JSON)")
    print("9-Salir")
    return  input("Ingrese opcion: ")



def mostrar_datos_fila(informacion : dict)->str:
    """_summary_

    Args:
        bici_list (dict): lista de datos de bici

    Returns:
        str: Los datos de bici sobre una fila
    """
    print(f"{informacion["id_bike"]} {informacion["nombre"]:<8} {informacion["tipo"]:<10} {informacion["tiempo"]} ")

def mostrar_tabla(lista:list)->None:
    """_summary_

    Args:
        bici (list): Lista de bici

    Raises:
        ValueError: No se habria ingresado ninguna lista
    """
    if isinstance(lista,list):
        cant = len(lista)
        print("                             ***Lista bici***")
        print("  ID BIKE      NOMBRE     TIPO     TIEMPO")
        print("-----------------------------------------------------------------------------------------------------------------------")
        for i in range(cant):
            mostrar_datos_fila(lista[i])
        print()
    else:
        raise ValueError("Eso no es una lista")
    


def get_path_actual(nombre_archivo):
    """_summary_

    Args:
        nombre_archivo (_type_): Nombre del archivo actual

    Returns:
        _type_: la ubicacion del archivo en el que estoy trabajando
    """
    import os
    ubi = os.path.dirname(__file__)
    
    return os.path.join(ubi, nombre_archivo)

def swap_lista(lista:list, valor1, valor2):
    """summary

    Args:
        lista (list): lista a swapear
        valor1 (type): primer valor a swapear
        valor2 (type): segundo valor a swapear
    """
    aux = lista[valor1]
    lista[valor1] = lista[valor2]
    lista[valor2] = aux



def crear_archivo_tipo(lista:list):
    """summary

    Args:
        lista (list): lista con datos para crear archivo
    """
    tipe_bike = input("Ingresar el tipo de bicicleta: ")
    while tipe_bike != "BMX" and tipe_bike != "PLAYERA" and tipe_bike != "MTB" and tipe_bike != "PASEO":
        tipe_bike = input("Ingrese un tipo de bici valido: ")
    lista_tipo = (filtrar_lista(lambda bike: bike["tipo"] == tipe_bike, lista))

    with open(get_path_actual(tipe_bike + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista_tipo)):
            l = ",".join(lista_tipo[i]) + "\n"

        for persona in lista_tipo:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)


def calcular_promedio(lista:list)->float:
    """summary

    Args:
        lista (list): lista a calcular promedio

    Raises:
        ValueError: La lista habria estado vacia
        ValueError: No se habria ingresado una lista

    Returns:
        float: El promedio del total de la lista
    """
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("No esta definido el promedio de una lista vacia")
        return totalizar_lista(lista) / cant
    raise ValueError("Eso no es una lista")


def filtrar_lista(funcion, lista:list)->list:
    """summary

    Args:
        funcion (type): Funcion para filtrar
        lista (list): List a filtrar

    Returns:
        list: Se crea una lista con los datos de la lista despues q se ha filtrados en base a la funcion
    """
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno



def totalizar_lista(lista:list)->int:
    """summary

    Args:
        lista (list): lista a sumar

    Raises:
        ValueError: No se habria ingresado una lista

    Returns:
        int: Suma todos sus elementos
    """
    if isinstance(lista, list):
        total = 0
        for el in lista:
            total += int(el)
        return total
    raise ValueError("Eso no es una lista")


def ordenar_lista_doble(lista, atributo, atributo2):
    if isinstance(lista,list):
            tam = len(lista)
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i][atributo] == lista[j][atributo]:
                        if lista[i][atributo2] > lista[j][atributo2]:
                            swap_lista(lista, i, j)
                    elif lista[i][atributo] > lista[j][atributo]:
                        swap_lista(lista,i,j)
    else:
        raise ValueError("No se ingreso una lista")




def mostrar_dato(lista:list)->str:
    """_summary_

    Args:
        lista (list): Lista con datos

    Raises:
        ValueError: No se habria ingresado un diccionario

    Returns:
        str: Printea los datos por linea
    """
    if isinstance(lista,list):
        for el in lista:
            print(el)
    else:
        raise ValueError("No se ingreso ningun diccionario")


def asignar_tiempo(lista, ini,fin):
    """_summary_

    Args:
        lista (_type_): lista a iterar/recorrer
        ini (_type_): tiempo minimo
        fin (_type_): tiempo maximo

    Returns:
        _type_: _description_
    """
    tiempos = mapear_lista(lambda bici:bici["tiempo"] ,lista)
    for i in range(len(tiempos)):
        tiempos[i] = randint(ini,fin)
    for i in range(len(lista)):
        lista[i]["tiempo"] = tiempos[i]

    return lista




def asignar_ganador(lista:list):
    """_summary_

    Args:
        lista (list): lista a recorrer

    Returns:
        _type_: retorna el/los diccionario/s del ganador/es
    """
    winner = []
    ordenar_campo(lista, "time", True)
    for i in lista:
        if i["tiempo"] == lista[0]["tiempo"]:
            winner.append(i)
    return winner


def mapear_lista(funcion, lista:list)->list:
    """summary

    Args:
        funcion (type): Funcion para mapear
        lista (list): Lista que se va a mapear

    Returns:
        list: Se creara una lista con los datos de la lista que ingresaste y con lo que especifiques en la funcion,
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno


def ordenar_campo(lista:list, campo:str, asc:bool = True):
    """summary

    Args:
        bici (list): Lista de bici
        campo (str): Campo a ordenar
        asc (bool, optional): True = Ascendente, False = Descendente. Defaults to True.

    Raises:
        ValueError: No se habria ingresado ninguna lista
    """
    if isinstance(lista,list):
        atributo = definir_campo(campo)
        tam = len(lista)
        for i in range(tam - 1):
            for j in range(i + 1, tam):
                if lista[i][atributo] > lista[j][atributo] if asc else lista[i][atributo] < lista[j][atributo]:
                    swap_lista(lista, i, j)
    else:
        raise ValueError("No se ingreso ninguna lista")
    


def definir_campo(campo:str)->str:
    """summary

    Args:
        info nombre, id, tipo, tiempo

    Raises:
        ValueError: No se ingreso un valor valido

    Returns:
        str: La palabra completa
    """
    match campo:
        case "n":
            retorno = "nombre"
        case "id":
            retorno = "idbike"
        case "tipe":
            retorno = "tipo"
        case "time":
            retorno = "tiempo"
        case _: raise ValueError("No es un campo valido")
    return retorno


