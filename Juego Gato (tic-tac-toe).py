from random import randrange


def pintarTablero(tablero):
	print("+-------" * 3,"+", sep="")
	for fila in range(3):
		print("|       " * 3,"|", sep="")
		for columna in range(3):
			print("|   " + str(tablero[fila][columna]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def jugadaUsuario(tablero):
	valido = False
	while not valido:
		jugada = input("Es tu turno, elige una casilla: ") 
		valido = len(jugada) == 1 and jugada >= '1' and jugada <= '9' # se valida la entrada
		if not valido:
			print("Movimiento invalido, intenta de nuevo: ") # si no es valida
			continue
		jugada = int(jugada) - 1 	# numero de la celda, del 0 al 8
		fila = jugada // 3 	# fila de la celda
		columna = jugada % 3		# columna de la celda
		marca = tablero[fila][columna]	# marca el cuadro elegido
		valido = marca not in ['O','X'] 
		if not valido:	# si está ocupado
			print("¡Cuadro ocupado, ingresa nuevamente!")
			continue
	tablero[fila][columna] = 'O' 	# se pinta en el tablero


def listaDeCasillasVacias(tablero):
	libre = []	# lista vacia
	for fila in range(3): # itera a través de las filas
		for columna in range(3): # itera a través de las columnas
			if tablero[fila][columna] not in ['O','X']: # verifica si está disponible
				libre.append((fila,columna)) # si, agrega una nueva tupla a la lista
	return libre


def ganador(tablero,marca):
	if marca == "X":	# verificar las X
		quien = 'maquina'
	elif marca == "O": # Verificar las O
		quien = 'usuario'
	else:
		quien = None
	cross1 = cross2 = True  # para las diagonales
	for rc in range(3):
		if tablero[rc][0] == marca and tablero[rc][1] == marca and tablero[rc][2] == marca:	# check fila rc
			return quien
		if tablero[0][rc] == marca and tablero[1][rc] == marca and tablero[2][rc] == marca: # check columnaumn rc
			return quien
		if tablero[rc][rc] != marca: # revisar la primer diagonal
			cross1 = False
		if tablero[2 - rc][2 - rc] != marca: # revisar la segunda diagonal
			cross2 = False
	if cross1 or cross2:
		return quien
	return None


def pintarJugada(tablero):
	libre = listaDeCasillasVacias(tablero) # crea una lista de los cuadros vacios o libres
	conteo = len(libre)
	if conteo > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y columnaocarla
		jugada = randrange(conteo)
		fila, columna = libre[jugada]
		tablero[fila][columna] = 'X'


tablero = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
tablero[1][1] = 'X' # columnaocar la primer 'X' en el centro
libre = listaDeCasillasVacias(tablero)
turnoUsuario = True # ¿De quien es turno ahora?
while len(libre):
	pintarTablero(tablero)
	if turnoUsuario:
		jugadaUsuario(tablero)
		vict = ganador(tablero,'O')
	else:	
		pintarJugada(tablero)
		vict = ganador(tablero,'X')
	if vict != None:
		break
	turnoUsuario = not turnoUsuario		
	libre = listaDeCasillasVacias(tablero)

pintarTablero(tablero)
if vict == 'usuario':
	print("¡Has ganado!")
elif vict == 'maquina':
	print("¡He ganado!")
else:
	print("¡Empate!")