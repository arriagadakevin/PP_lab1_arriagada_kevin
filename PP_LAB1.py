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

def mostrar_jugadores(lista_jugadores:list) -> list:
    """
    mostrar jugadores en formato(Nombre Jugador - Posición)
    parametro: lista_jugadores : list, lista con todos los jugadores a imprimir
    devulve: lista ordenada con el formato deseado
    """
    if len(lista_jugadores) > 0:
        lista = lista_jugadores[:]
        lista_ordenada = []
        for jugadores in lista:
            lista_ordenada.append([jugadores["nombre"], jugadores["posicion"]])
    else:
        print("[herror]: lista vacia")
    

    return lista_ordenada


