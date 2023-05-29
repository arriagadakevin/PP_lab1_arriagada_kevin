import json
import re


def imprimir_datos(dato)-> None:
    """
    funcion para imprimir dato 
    parametro: dato, 'dato' a imprimir ingresado
    retorna: dato
    """
    print(dato)

def msg_error(tipo_error : str)->str:
    """
    genera un mensaje de error
    parametros: tipo error : str
    devuelve : str
    """
    return imprimir_datos(" ¡[error]! {0}". format(tipo_error))

def parce_json(nombre_archivo : str) -> list:
    """
    """
    lista_personaje = []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista_personaje = dict["jugadores"]
    return lista_personaje

lista_jugadores = parce_json(r"dt.json")

def mostrar_menu()->None:
    imprimir_datos("""
    1. Mostrar la lista de todos los jugadores del Dream Team con su posición.
    2. Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas.
    3. Permitir al usuario guardar las estadísticas de un jugador seleccionado en un archivo CSV.
    4. Permitir al usuario buscar un jugador por su nombre y mostrar sus logros.
    5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre.
    6. Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
    7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
    8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
    9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
    10. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
    11. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.
    12. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.
    13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.
    14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
    15. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
    16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
    17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.
    18. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
    19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.
    20. Permitir al usuario ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
        """)


def mostrar_jugadores(lista_jugadores:list) -> None:
    """
    mostrar jugadores en formato(indice - Nombre Jugador - Posición)
    parametro: lista_jugadores : list, lista con todos los jugadores a imprimir
    devulve: none
    """
    if len(lista_jugadores) > 0:
        for indice in range(len(lista_jugadores)):
            jugador = lista_jugadores[indice]
            imprimir_datos("{0} | {1} | {2} |".format(
                                                    indice, 
                                                    jugador["nombre"], 
                                                    jugador["posicion"]
                                                    ))
        
    else:
        msg_error("Lista vacia")


def mostrar_estadisticas_jugador_por_indice(lista_jugadores : list):
    if lista_jugadores:
        mostrar_jugadores(lista_jugadores)
        indice = input("selecciones el indice del jugador deseado")
        while re.search(r"^(0|1|2|3|4|5|6|7|8|9|10|11)$", indice) == None :
            imprimir_datos("[error] : numero incorrecto")
            indice = input("selecciones el indice del jugador deseado")

        indice = int(indice)
        jugador_seleccionado = lista_jugadores[indice]
        imprimir_datos("el jugador seleccionado es: {0} y sus estadisticas son: {1}".format(
                                                    jugador_seleccionado["nombre"],
                                                    jugador_seleccionado["estadisticas"]))
        
        respuesta = input("deseas guardar la informacion en formato csv? (si/no)")
        if respuesta == "si":
            guardar_jugadores_en_csv(r"C:\Users\arria\OneDrive\Escritorio\UTN\1er parcial python\PP_lab1_arriagada_kevin\datos.csv", jugador_seleccionado)
    else:
        msg_error("lista vacia")

def guardar_jugadores_en_csv(nombre_archivo : str,jugador : list)->None:
    if len(jugador) > 0 and type(nombre_archivo) == str:
        with open(nombre_archivo, "w") as archivo:
            texto = "el jugador seleccionado es: {0} y sus estadisticas son: {1}".format(
                                                    jugador["nombre"],
                                                    jugador["estadisticas"])
            archivo.write(texto)
    else:
        msg_error("lista vacia")


def buscar_jugador_por_nombre(lista_jugadores : list):
    if len(lista_jugadores) > 0:
        nombre_jugador = input("ingrese nombre del jugador deseado")
        for jugadores in lista_jugadores:
            if nombre_jugador.lower() == jugadores["nombre"].lower() :
                imprimir_datos("nombre jugador : {0}, logros : {1}".format(jugadores["nombre"], jugadores["logros"]))
    else:
        msg_error("lista vacia")
        
def ordenar_una_lista():

buscar_jugador_por_nombre(lista_jugadores)