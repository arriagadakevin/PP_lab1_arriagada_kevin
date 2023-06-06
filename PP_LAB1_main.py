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
    jugadores_salor_fama,
    calcular_max,
    mostrar_mayor_puntos_por_partido,
    mayor_cantidad_logros,
    calcular_mostrar,
    extra,
    mejores_Estadisticas,
    mejor_jugador,
    imprimir_guarda_tabla_jugadores,
    guardar_jugadores_en_csv,
    generar_texto,
    posicion_en_cada_stadistica,
    all_star_ordenamiento,
    all_star_mostrar
    
)










def menu_dream_team():
    while True:
        mostrar_menu()
        respuesta = int(input("    seleccionar punto (1 - 20)"))
        while  respuesta < 1 or respuesta > 27:
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
                jugadores_salor_fama(nombre_jugador(), lista_jugadores)
                clear_console()
            case 7:
                calcular_max(lista_jugadores,"estadisticas" ,"rebotes_totales")
                clear_console()
            case 8:
                calcular_max(lista_jugadores,"estadisticas" ,"porcentaje_tiros_de_campo")
                clear_console()
            case 9:
                calcular_max(lista_jugadores,"estadisticas" ,"asistencias_totales")
                clear_console()
            case 10:
                mostrar_mayor_puntos_por_partido(lista_jugadores, "promedio_puntos_por_partido")
                clear_console()
            case 11:
                mostrar_mayor_puntos_por_partido(lista_jugadores, "promedio_rebotes_por_partido")
                clear_console()
            case 12:
                mostrar_mayor_puntos_por_partido(lista_jugadores, "promedio_asistencias_por_partido")
                clear_console()
            case 13:
                calcular_max(lista_jugadores,"estadisticas","robos_totales")
                clear_console()
            case 14:
                calcular_max(lista_jugadores,"estadisticas","bloqueos_totales")
                clear_console()
            case 15:
                mostrar_mayor_puntos_por_partido(lista_jugadores, "porcentaje_tiros_libres")
                clear_console()
            case 16:
                calcular_mostrar(lista_jugadores)
                clear_console()
            case 17:
                mayor_cantidad_logros(lista_jugadores)
                clear_console()
            case 18:
                mostrar_mayor_puntos_por_partido(lista_jugadores, "porcentaje_tiros_triples")
                clear_console()
            case 19:
                calcular_max(lista_jugadores,"estadisticas","temporadas")
                clear_console()
            case 20:
                mostrar_mayor_puntos_por_partido(lista_jugadores, "porcentaje_tiros_triples" )
                clear_console()
            case 23:
                jugadores_con_estadisticas = posicion_en_cada_stadistica(lista_jugadores)
                nombre_archivo = "informe_jugadores.csv"
                print(jugadores_con_estadisticas)
                texto_generado = generar_texto(jugadores_con_estadisticas)
                guardar_jugadores_en_csv(nombre_archivo, texto_generado)
                imprimir_guarda_tabla_jugadores(jugadores_con_estadisticas)
                clear_console()
            case 24:
                extra()
                clear_console()
            case 25:
                lista = all_star_ordenamiento(lista_jugadores)
                all_star_mostrar(lista)
                clear_console()
            case 26:
                mejores_Estadisticas(lista_jugadores)
                clear_console()
            case 27:
                mejor_jugador(lista_jugadores)
                clear_console()

menu_dream_team()