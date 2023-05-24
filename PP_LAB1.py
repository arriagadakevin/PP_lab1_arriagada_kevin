import json

def parce_json(nombre_archivo : str) -> list:
    """
    """
    lista_personaje = []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista_personaje = dict["jugadores"]
    return lista_personaje

lista_jugadores = parce_json(r"C:\Users\Kevin\Desktop\UTN\1er parcial python\PP_lab1_arriagada_kevin\dt.json")

def mostrar_jugadores(lista_jugadores:list, punto: str) -> list:
    """
    mostrar jugadores en formato(Nombre Jugador - Posición)
    parametro: lista_jugadores : list, lista con todos los jugadores a imprimir
    devulve: lista ordenada con el formato deseado
    """
    if len(lista_jugadores) > 0:
        lista = lista_jugadores[:]
        if punto == "1":
            for jugadores in lista:
                    print("{0} - {1}".format(jugadores["nombre"], jugadores["posicion"]))
        elif punto == "2":
            indice = 0
            for jugadores in lista:  
                print("{0} | {1} | {2}".format(indice, jugadores["nombre"], jugadores["posicion"]))
                indice += 1
    else:
        print("[herror]: lista vacia")


def mostrar_estadisticas_jugador_por_indice(lista_jugadores : list):
    pass




