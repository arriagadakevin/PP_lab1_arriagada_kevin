from PP_LAB1 import (
    imprimir_datos,
    mostrar_menu,
    mostrar_estadisticas_jugador_por_indice,
    lista_jugadores,
    mostrar_jugadores,
    buscar_jugador_por_nombre,
    lista_jugadores_ordenada_promediada,
    clear_console,
    nombre_jugador,
    jugadores_salor_fama
)










def menu_dream_team():
    while True:
        mostrar_menu()
        respuesta = int(input("    seleccionar punto (1 - 20)"))
        while  respuesta < 1 or respuesta > 20:
            imprimir_datos("[error] : numero invalido")
            respuesta = int(input("seleccionar punto (1 - 20)"))
        match respuesta:
            case 1:
                mostrar_jugadores(lista_jugadores)
                clear_console()
            case 2:
                mostrar_estadisticas_jugador_por_indice(lista_jugadores)
                clear_console()
            case 3:
                mostrar_estadisticas_jugador_por_indice(lista_jugadores)
                clear_console() 
            case 4:
                buscar_jugador_por_nombre(lista_jugadores, nombre_jugador())
                clear_console()
            case 5:
                lista_jugadores_ordenada_promediada(lista_jugadores)
                clear_console()
            case 6:
                buscar_jugador_por_nombre(lista_jugadores)
                clear_console()
            case 7:
                jugadores_salor_fama(nombre_jugador(), lista_jugadores)
                clear_console()
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                pass
            case 16:
                pass
            case 17:
                pass
            case 18:
                pass
            case 19:
                pass
            case 20:
                pass

menu_dream_team()