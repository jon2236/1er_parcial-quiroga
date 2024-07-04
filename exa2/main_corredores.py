from funciones import *
import json
from random import randint

competidores = []
archivo_cargado = False
tiempos_asignados = False

while True:
    opcion = menu()
    match opcion:
        case "1":
            limpiar_pantalla()
            archivo = input("Ingrese el nombre del archivo: ")
            try:
                cargar_archivo_csv(f"{archivo}.csv", competidores)
                print("archivo importado con exito!")
                archivo_cargado = True
            except:
                print(f"no se encontro el archivo {archivo}")
        case "2":
            limpiar_pantalla()
            if archivo_cargado:
                mostrar_tabla(competidores)
            else:
                print("primero debe cargar un archivo CSV.")
        case "3":
            limpiar_pantalla()
            if archivo_cargado and not tiempos_asignados:
                mostrar_tabla(asignar_tiempo(competidores, 50, 120))
                tiempos_asignados = True
            else:
                print("primero debe cargar un archivo CSV y asignar tiempos.")
        case "4":
            limpiar_pantalla()
            if archivo_cargado:
                print("el/los ganador/es de la carrera es/son:")
                mostrar_dato(asignar_ganador(competidores))
            else:
                print("primero debe cargar un archivo CSV.")
        case "5":
            limpiar_pantalla()
            if archivo_cargado:
                crear_archivo_tipo(competidores)
                print("archivo CSV creado con exito.")
            else:
                print("primero debe cargar un archivo CSV.")
        case "6":
            limpiar_pantalla()
            if archivo_cargado:
                tipos_bicicletas = ["BMX", "PASEO", "MTB", "PLAYERA"]
                for tipo in tipos_bicicletas:
                    bicis_tipo = filtrar_lista(lambda bici: bici["tipo"] == tipo, competidores)
                    promedio = calcular_promedio(mapear_lista(lambda bici: bici["tiempo"], bicis_tipo))
                    print(f"el promedio de las bicicletas {tipo} es: {promedio}")
            else:
                print("primero debe cargar un archivo CSV.")
        case "7":
            limpiar_pantalla()
            if archivo_cargado:
                ordenar_lista_doble(competidores, "tipo", "tiempo")
                mostrar_dato(competidores)
            else:
                print("primero debe cargar un archivo CSV.")
        case "8":
            limpiar_pantalla()
            if archivo_cargado:
                with open(get_path_actual("posiciones_tipo_bicicleta.json"), "w", encoding="utf-8") as archivo_json:
                    json.dump(competidores, archivo_json, indent=4)
                print("archivo JSON creado con exito.")
            else:
                print("primero debe cargar un archivo CSV.")
        case "9":
            limpiar_pantalla()
            print("nos vemos!")
            break
        case _:
            limpiar_pantalla()
            print("debe ingresar una opcion valida.")

    pausar()