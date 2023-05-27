import json
import re

def parce_json(nombre_archivo : str) -> list:
    """
    """
    lista_personaje = []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista_personaje = dict["jugadores"]
    return lista_personaje

lista_jugadores = parce_json(r"dt.json")
    
def imprimir_datos(dato)-> None:
    """
    funcion para imprimir dato 
    parametro: dato, 'dato' a imprimir ingresado
    retorna: dato
    """
    print(dato)

        
def mostrar_jugadores(lista_jugadores:list, mostra_indice : bool) -> list:
    """
    mostrar jugadores en formato(Nombre Jugador - Posición)
    parametro: lista_jugadores : list, lista con todos los jugadores a imprimir
    devulve: lista ordenada con el formato deseado
    """
    if len(lista_jugadores) > 0:
        if mostra_indice == False:
            for jugadores in lista_jugadores:
                imprimir_datos("{0} - {1}".format(jugadores["nombre"], jugadores["posicion"]))
        elif mostra_indice == True:
            indice = 0
            for jugadores in lista_jugadores:  
                imprimir_datos("{0} | {1} | {2}".format(indice, jugadores["nombre"], jugadores["posicion"]))
                indice += 1
    else:
        print("[error]: lista vacia")


def mostrar_estadisticas_jugador_por_indice(lista_jugadores : list):
    mostrar_jugadores(lista_jugadores, True)
    indice = input("selecciones el indice del jugador deseado")
    while re.search(r"^(0|1|2|3|4|5|6|7|8|9|10|11)$", indice) == None :
        print("[error] : numero incorrecto")
        indice = input("selecciones el indice del jugador deseado")

    indice = int(indice)
    jugador_seleccionado = lista_jugadores[indice]
    imprimir_datos("el jugador seleccionado es: {0} y sus estadisticas son: {1}".format(
                                                jugador_seleccionado["nombre"],
                                                jugador_seleccionado["estadisticas"]))





