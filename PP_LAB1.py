import json
import re
import os

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

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
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
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

def seleccionar_indice()->int:
    """
    funcion para seleccionar un indice del 1 al 11  
    retorna: int (numero entero)
    """
    indice = input("selecciones el indice del jugador deseado")
    while re.search(r"^(0|1|2|3|4|5|6|7|8|9|10|11)$", indice) == None :
        msg_error("numero incorrecto")
        indice = input("selecciones el indice del jugador deseado")
    indice = int(indice)
    return indice

def mostrar_estadisticas_jugador_por_indice(lista_jugadores : list)-> None:
    """
    mostrar las estadisticas de un jugador segun su indice
    parametro: lista_jugadores:list, lista a trabajar
    devuelve : None
    """
    if lista_jugadores:
        mostrar_jugadores(lista_jugadores)
        indice = seleccionar_indice()
        jugador_seleccionado = lista_jugadores[indice]
        imprimir_datos("el jugador seleccionado es: {0} y sus estadisticas son: {1}".format(
                                                    jugador_seleccionado["nombre"],
                                                    jugador_seleccionado["estadisticas"]))
        
        respuesta = input("deseas guardar la informacion en formato csv? (si/no)")
        if respuesta == "si":
            guardar_jugadores_en_csv(r"C:\Users\arria\OneDrive\Escritorio\PP_lab1_arriagada_kevin-main\datos.csv", jugador_seleccionado)
    else:
        msg_error("lista vacia")

def guardar_jugadores_en_csv(nombre_archivo : str,texto)->str:
    """
    funcion para guardar cadenas de texto en formato csv 
    parametro: nombre_archivo :str 
    """
    if type(nombre_archivo) == str:
        with open(nombre_archivo, "w+") as archivo:
            archivo.write(texto)
        return imprimir_datos("listo!")
    else:
        return msg_error("nombre archivo incorrecto")

def nombre_jugador()-> str:
    """
    toma por input un nombre de jugador
    parametros: None
    retorna: nombre_jugador: str 
    """
    nombre_jugador = input("ingrese nombre del jugador deseado")
    return nombre_jugador.lower()

def buscar_jugador_por_nombre(lista_jugadores : list, nombre_jugador : str):
    if len(lista_jugadores) > 0:
        for jugadores in lista_jugadores:
            if nombre_jugador == jugadores["nombre"].lower() :
                    imprimir_datos("nombre jugador : {0}, logros : {1}".format(jugadores["nombre"], jugadores["logros"]))
                    break
            else:
                msg_error("nombre no encontrado")
    else:  
        msg_error("lista vacia")


def calcular_promedio_estadisticas(lista_jugadores : list, variable1 : str, variable : str)-> int:
    """
    funcion para calcular promedio
    parametros: lista_jugadores : list, lista de jugadores a trabajar
    parametro: variable1 : str, str que sirve para definir la accion
    parametro: variable : srt, str que sirve para definir otra accion
    retorna: promedio_final : int 
    """
    if len(lista_jugadores) > 0:
        acumulador_puntos = 0
        contador_jugadores = 0
        for jugadores in lista_jugadores:
            acumulador_puntos += jugadores[variable1][variable]
            contador_jugadores += 1
        
        promedio_final = acumulador_puntos / contador_jugadores
        return promedio_final
    else:
        msg_error("lista_vacia")


def ordenar_una_lista(lista_jugadores : list, parametro: str, parametro_2 : str,flag_orden : bool) -> list:
    """
    funcion que sirve para crear una lista ordenada dependiendo del parametro
    parametro: lista_jugadores : list, lista a trabajar
    parametro: parametro: str, sirve para definir el parametro por el cual ordenar
    parametro: flag_orden : bool, sirve para definir si, de manera ascendente o decendiente se va a ordenar
    retrona: lista : list, lista ordenada 
    """
    if len(lista_jugadores) > 0:
        if parametro_2 is None and parametro != None:
            lista = lista_jugadores
            rango_a = len(lista) - 1
            flag_swap = True
            while(flag_swap):
                flag_swap = False
                for indice_A in range(rango_a):
                    if  (flag_orden == False and lista[indice_A][parametro] < lista[indice_A+1][parametro]) \
                    or (flag_orden == True and lista[indice_A][parametro] > lista[indice_A+1][parametro]):
                        lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                        flag_swap = True
            return lista
        
        elif parametro is None and parametro_2 is None:
            lista = lista_jugadores[:]
            rango_a = len(lista) - 1
            flag_swap = True
            while(flag_swap):
                flag_swap = False
                for indice_A in range(rango_a):
                    if  (flag_orden == False and lista[indice_A] < lista[indice_A+1]) \
                    or (flag_orden == True and lista[indice_A] > lista[indice_A+1]):
                        lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                        flag_swap = True
            return lista
        
        elif parametro != None and parametro_2 != None:
            lista = lista_jugadores[:]
            rango_a = len(lista) - 1
            flag_swap = True
            while(flag_swap):
                flag_swap = False
                for indice_A in range(rango_a):
                    if  (flag_orden == False and lista[indice_A][parametro][parametro_2] < lista[indice_A+1][parametro][parametro_2]) \
                    or (flag_orden == True and lista[indice_A][parametro][parametro_2] > lista[indice_A+1][parametro][parametro_2]):
                        lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                        flag_swap = True
            return lista
        else:
            msg_error("agregar bien los parametros")
    else:
        msg_error("lista_vacia")

def lista_jugadores_ordenada_promediada(lista_jugadores : list)->str:
    """
    funcion para mostrar el pomedio y a su vez ver la lista ordenada
    parametro: lista_personajes: list, lista a trabajar 
    retorna: str
    """
    if len(lista_jugadores) > 0:

        promedios = calcular_promedio_estadisticas(lista_jugadores,"estadisticas","promedio_puntos_por_partido")
        lista_jugadores_ordenada = ordenar_una_lista(lista_jugadores,"nombre",None, False)
        imprimir_datos("*************************************************************")
        imprimir_datos("el promedio del equipo es {0}".format(promedios))
        for jugadores in lista_jugadores_ordenada:
            imprimir_datos("jugador : {0}, promedio de puntos por partido {1}".format(jugadores["nombre"], jugadores["estadisticas"]["promedio_puntos_por_partido"]))
        imprimir_datos("*************************************************************")
    else:
        msg_error("lista vacia")

def jugadores_salor_fama(nombre_jugador: str , lista_jugadores :list):
    """
    sirve para ver los jugadores que pertenecen al salon de la fama
    parametro: nombre_jugador : str, nombre a buscar
    parametro: lista_jugadores : list, lista a trabajar
    """
    for jugadores in lista_jugadores:
        if nombre_jugador == jugadores["nombre"].lower() :
            logros = jugadores["logros"]
            for logro in logros:
                if "Miembro del Salon de la Fama del Baloncesto" == logro:
                    imprimir_datos("el jugador {0} es {1}".format(jugadores["nombre"], logro))

def calcular_max(lista_jugadores : list, parametro_1 :str, parametro_2 : str) -> str:
    """
    funcion que sirve para calcular el jugador que mas puntos tiene en una determinada categoria
    parametro: lista_jugadores : list, lista a trabajar
    parametro: parametro_1 : str ,parametro a trabajar
    parametro: parametro_2 : str , segundo parametro a trabajar
    devuelve: str
    """
    contador_max = 0
    for jugador in lista_jugadores:
        if jugador[parametro_1][parametro_2] > contador_max :
            contador_max = jugador[parametro_1][parametro_2]           
            nombre_jugador_max = jugador["nombre"]
    parametro = parametro_2.replace("_"," ")
    return imprimir_datos("el jugador con mas {0} es : {1}  y la cantidad es {2}".format(parametro,nombre_jugador_max, contador_max))

def calcular_mostrar(lista_jugadores :list ):
    lista = ordenar_una_lista(lista_jugadores, "posicion", False)
    lista = lista[1:]
    promedio =calcular_promedio_estadisticas(lista, "estadisticas", "promedio_puntos_por_partido")
    return imprimir_datos("el promedio de puntos por partido es : {0}".format(promedio))
        


def mayor_cantidad_logros(lista_jugadores: list)-> str:
    """
    busca al jugador con mayor cantidad de logros 
    parametro: lista_jugadores : list, lista a trabajar 
    retorna: str
    """
    contador_max = 0
    for jugadores in lista_jugadores:
        if len(jugadores["logros"]) > contador_max:
            contador_max = len(jugadores["logros"])
            nombre_jugador_max = jugadores["nombre"]
    return imprimir_datos("el jugador con mayor cantidad de logros es : {0} con {1} logros".format(nombre_jugador_max, contador_max))

def mostrar_mayor_puntos_por_partido(lista_jugadores : list, parametro_1 : str):
    numero = int(input("ingrese un numero"))
    lista_jugadores_ordenada = ordenar_una_lista(lista_jugadores, "posicion", True)
    jugadores_max = []
    for jugadores in lista_jugadores_ordenada:
        if numero < jugadores["estadisticas"][parametro_1]:
            jugadores_max.append(jugadores["nombre"])
        else:
            imprimir_datos("ningun jugador promedio mas que eso ")
    imprimir_datos("los jugadores que tienen promedio mas alto que {0} son : {1}".format(numero, jugadores_max))


def extra():
    keys = ["Pivot", "Escolta" , "Base" , "Ala-Pivot", "Alero"]
    diccionario_jugadores = {"Pivot" : 0, "Escolta": 0,
                              "Base" : 0,"Ala-Pivot" : 0, 
                              "Alero": 0}

    for keys in keys:
        for jugadores in lista_jugadores:
            if jugadores["posicion"] == keys:
                diccionario_jugadores[keys] += 1
                
    print(diccionario_jugadores)



def mejores_Estadisticas(lista_jugadores :list):
    if len(lista_jugadores) > 0 :
        for jugador in lista_jugadores:
            for estadisticas in jugador["estadisticas"]:
                calcular_max(lista_jugadores, "estadisticas", estadisticas)
            break
    else:
        msg_error("lista vacia")   

def mejor_jugador(lista_jugadores :list):
    
    if lista_jugadores:
        jugador_max = None
        puntaje_max = 0

        for jugador in lista_jugadores:
            estadistica_jugador = 0
            for estadistica in jugador["estadisticas"].values():
                estadistica_jugador += estadistica
            if jugador_max is None or estadistica_jugador > puntaje_max:
                jugador_max = jugador
                puntaje_max = estadistica_jugador

        print("jugador tiene las mejores estadísticas : {0}".format(jugador_max["nombre"]))
    else:
        msg_error("lista vacia")


def posicion_en_cada_stadistica(lista_jugadores : list):
    keys = ["rebotes_totales", "asistencias_totales", "robos_totales", "puntos_totales"]
    jugadores_segun_estadistica = []
    contador = 0
    for claves in keys:
        lista_ordenada = ordenar_una_lista(lista_jugadores, "estadisticas", claves , False)
        for i in range(len(lista_ordenada)):
            jugador = lista_ordenada[i]
            nombre = jugador["nombre"]
            jugador["estadisticas"][claves] = i + 1
            jugador_modificado = {
                "nombre": nombre,
                "estadisticas": jugador["estadisticas"]
            }
            jugadores_segun_estadistica.append(jugador_modificado)
            contador += 1
            if contador > 11:
                return jugadores_segun_estadistica
    
def generar_texto(data)-> str:

    """
    La función genera una representación de texto de los datos del jugador de baloncesto en formato de
    lista o de diccionario, dependiendo del tipo de dato, Si data es una lista de diccionarios, la
    función devuelve una cadena con valores separados por comas para cada diccionario de la lista, Si
    data es un diccionario, la función devuelve una cadena con valores separados por comas para las
    claves y valores en el diccionario
    
    parametro: data: Los datos de entrada que pueden ser un diccionario o una lista de diccionarios que
    contienen información sobre los jugadores de baloncesto y sus estadísticas

    retorna: devuelve una cadena que contiene datos en un formato específico.
    """

    if isinstance(data, list):
        lista_claves = ["nombre", "posicion", "puntos_totales", "rebotes_totales", "robos_totales"]
        filas = []

        for jugador in data:
            valores = [str(jugador["nombre"]),
                       str(jugador["estadisticas"]["puntos_totales"]),
                       str(jugador["estadisticas"]["rebotes_totales"]),
                       str(jugador["estadisticas"]["robos_totales"])]
            fila = ",".join(valores)
            filas.append(fila)

        claves_str = ",".join(lista_claves)
        datos = "{0}\n{1}".format(claves_str, "\n".join(filas))

        return datos

    elif isinstance(data, dict):
        lista_claves = ["nombre", "posicion"]
        lista_valores = []

        jugador_estadisticas = data["estadisticas"]
        nombre_posicion = "{0}, {1}".format(data["nombre"], data["posicion"])

        for clave, valor in jugador_estadisticas.items():
            lista_claves.append(clave)
            lista_valores.append(str(valor))

        claves_str = ",".join(lista_claves)
        valores_str = ",".join(lista_valores)

        datos_str = "{0}\n{1},{2}".format(claves_str, nombre_posicion, valores_str)
        return datos_str

    else:
        msg_error("El tipo de entrada no es compatible")
    
    
def imprimir_tabla_jugadores(lista_jugadores: list)-> None:
    """
    funcion para imprimir lista_jugadores formateada
    parametro: (lista_jugadores : list)
    devuelve : None
    """
    if len(lista_jugadores) > 0:
        imprimir_datos("---------------------------------------------------------------------------")
        imprimir_datos("|     Jugador          |    Puntos  |   Rebotes |  Asistencias  |  Robos  |")
        imprimir_datos("---------------------------------------------------------------------------")
        for jugador in lista_jugadores:
            imprimir_datos("|  {:19s} | {:^10d} | {:^9d} | {:^13d} | {:^7d} |".format(
                jugador["nombre"],
                jugador["estadisticas"]["puntos_totales"],
                jugador["estadisticas"]["rebotes_totales"],
                jugador["estadisticas"]["asistencias_totales"],
                jugador["estadisticas"]["robos_totales"])
            )
        imprimir_datos("---------------------------------------------------------------------------")
    else:
        msg_error("lista vacia")



def all_star_ordenamiento(lista_jugadores : list )->list:
    """
    funcion para ordenar los jugadores segun la cantidad de all star
    parametro : (lista_jugadores : list), lista a trabajar 
    devuelve: (lista_ordenada : list) lista ordenada 
    """
    if len(lista_jugadores) > 0:
        diccionario = []
        for jugadores in lista_jugadores:
            diccionario_jugador = {}
            nombre = jugadores["nombre"]
            for logros in jugadores["logros"]:
                if re.search(r"^[0-9]+ veces All-Star", logros):
                    dato = re.split(" ", logros)
                    dato[0] = int(dato[0])
                    diccionario_jugador['nombre'] = nombre
                    diccionario_jugador["all_star"] = dato[0]

                    diccionario.append(diccionario_jugador)
                    
        lista_ordenada = ordenar_una_lista(diccionario, "all_star", None, True)
        return(lista_ordenada)
    else:
        msg_error("lista vacia")

def all_star_mostrar(lista_jugadores : list)-> None:
    """
    funcion para imprimir en pantalla los resultados de all_star_ordenamiento()
    parametro : lista_jugadores :list , lista ordenada segun all star
    devuelve: None
    """
    if len(lista_jugadores) > 0:
        imprimir_datos("---------------------------------------")
        imprimir_datos("|     Jugador          |    all star  |")
        imprimir_datos("---------------------------------------")
        for jugadores in lista_jugadores:
            imprimir_datos("|  {:19s} |  {:^10d}  |".format(
                jugadores["nombre"],
                jugadores["all_star"],
                ))
        imprimir_datos("---------------------------------------")
    else:
        msg_error("lista vacia")

lista = all_star_ordenamiento(lista_jugadores)
all_star_mostrar(lista)

