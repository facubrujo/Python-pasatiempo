import os
def limpiarConsola():
    os.system("cls")

#variables
rango = 3
matriz = [ ["-" for _ in range(rango)] for _ in range(rango) ]
defValor = "-"
bandera = False
player1 = True

#tablero inicio
def crearTablero(matriz):
    #print(f'creando matriz de {str(rango)} x {str(rango)}')
    for i in range(rango):
        for j in range(rango):
            matriz[i][j] = f"["+defValor+"]"

def mostrarTablero(matriz):
    for i in matriz:
        print(*i)   

#controles
def jugada(entrada, ficha, bandera):
    if entrada == "7":
        matriz[0][0] = ficha
    if entrada == "8":
        matriz[0][1] = ficha
    if entrada == "9":
        matriz[0][2] = ficha
    if entrada == "4":
        matriz[1][0] = ficha
    if entrada == "5":
        matriz[1][1] = ficha
    if entrada == "6":
        matriz[1][2] = ficha
    if entrada == "1":
        matriz[2][0] = ficha
    if entrada == "2":
        matriz[2][1] = ficha
    if entrada == "3":
        matriz[2][2] = ficha
    if entrada == "0":
        return not bandera



def verificacion2(matriz, ficha):
# [00][01][02]  
# [10][11][12]  
# [20][21][22]  
    chekeador_diagonal_principal = 0
    chekeador_diagonal_secundaria = 0
    chekeadores_filas = [0] * rango
    chekeadores_columnas = [0] * rango
    
    for i in range(rango):
        if matriz[i][i] == ficha:
            chekeador_diagonal_principal += 1
        
        j = rango - 1 - i
        if matriz[i][j] == ficha:
            chekeador_diagonal_secundaria += 1
        
        for k in range(rango):
            if matriz[i][k] == ficha:
                chekeadores_filas[i] += 1
            if matriz[k][i] == ficha:
                chekeadores_columnas[i] += 1
    
    if chekeador_diagonal_principal == rango or chekeador_diagonal_secundaria == rango:
        print("GANADOR: " + ficha)
        mostrarTablero(matriz)
        print("----FIN----")
        input(" Presione enter para cuntinuar")
        return True

    for i in range(rango):
        if chekeadores_filas[i] == rango or chekeadores_columnas[i] == rango:
            print("GANADOR: " + ficha)
            mostrarTablero(matriz)
            print("----FIN----")
            input(" Presione enter para cuntinuar")
            return True
    
    return False

#juego
def juego(bandera, matriz, player1):
    limpiarConsola()
    crearTablero(matriz)
    while bandera == False:
        if player1:
            print(" ---- PLAYER 1 ---- ")
            mostrarTablero(matriz)
            ficha = "[x]"
            entrada = str(input("Jugador "+ficha+" ingrese un numero del 1 al 9 : "))
            bandera = jugada(entrada, ficha, bandera)
            limpiarConsola()        
            bandera = verificacion2(matriz , ficha)
            player1 = not player1
        else:
            print(" ---- PLAYER 2 ----")
            mostrarTablero(matriz)
            ficha = "[o]"
            entrada = str(input(f"Jugador "+ficha+"  ingrese un numero del 1 al 9 : "))
            bandera = jugada(entrada, ficha, bandera)
            limpiarConsola()        
            bandera = verificacion2(matriz, ficha)
            player1 = not player1

#mostrar controles
def mostrarControles():
    print("------------------------------")
    print("Controles del juego")
    print("Utiliza el teclado numerico para ")
    print("ubicar las fichas en las posiciones del tablero")
    print("[7][8][9]")
    print("[4][5][6]")
    print("[1][2][3]")
    print("------------------------------")

# menu
def menu(bandera, matriz, player1):
    while not bandera:
        limpiarConsola()
        print("***********************************")
        print("************ TA TE TI ************")
        print("")
        print("Presione 1 para iniciar el juego")
        print("Presione 2 para ver controles")
        print("Presione cualquier otra tecla para salir")
        opcion = input( "- " )
        if opcion == "1":
            juego(bandera, matriz, player1)
        elif opcion == "2":
            limpiarConsola()
            mostrarControles()
            print("presione  1 para volver al menu")
            volver = input(" - ")
            if volver == "1":
                menu(bandera, matriz, player1)
                break
        else:
            print("Saliendo ... ")
            break

menu(bandera , matriz, player1)
