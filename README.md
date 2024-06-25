# Juego-Gato---tic-tac-toe - PROYECTO FINAL PYTHON ESSENTIALS - CISCO NETWORK ACADEMY

## ❌⭕❌⭕ Juego de gato (simplificado) ❌⭕❌⭕
Escenario:

Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

- La maquina (por ejemplo, el programa) jugará utilizando las 'X's;
- El usuario (por ejemplo, tu) jugarás utilizando las 'O's;
- El primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
- Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
- El usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
- El programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
- La maquina responde con su movimiento y se verifica el estado del juego;
- No se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

---

## El ejemplo del programa es el siguiente:

### ❌ Movimiento de la máquina en: 5

![Captura de pantalla 2024-06-25 151622](https://github.com/OC0NER/Juego-Gato---tic-tac-toe/assets/154689355/034c772c-7c85-4ec0-8959-2072d612bd4a)


### ⭕ Ingresa tu movimiento: 1

![Captura de pantalla 2024-06-25 151922](https://github.com/OC0NER/Juego-Gato---tic-tac-toe/assets/154689355/1e9dcddc-8adf-4a24-933c-14b2fb8a51c1)


### ❌ Movimiento de la máquina en: 2

![Captura de pantalla 2024-06-25 152001](https://github.com/OC0NER/Juego-Gato---tic-tac-toe/assets/154689355/8f1ff581-8568-4db1-86b3-3ff0390a0b33)


### ⭕ Ingresa tu movimiento: 8

![Captura de pantalla 2024-06-25 152059](https://github.com/OC0NER/Juego-Gato---tic-tac-toe/assets/154689355/8330576a-2cd3-4972-9984-bdded5af5e00)


### ❌ Movimiento de la máquina en: 6

![Captura de pantalla 2024-06-25 152129](https://github.com/OC0NER/Juego-Gato---tic-tac-toe/assets/154689355/5be619ed-1278-4991-9f0e-59bfd533fdf6)

### ⭕ Ingresa tu movimiento: 4

![Captura de pantalla 2024-06-25 152152](https://github.com/OC0NER/Juego-Gato---tic-tac-toe/assets/154689355/4983877d-508b-491d-956a-052f3771d696)

### ❌ Movimiento de la máquina en: 3

![Captura de pantalla 2024-06-25 152212](https://github.com/OC0NER/Juego-Gato---tic-tac-toe/assets/154689355/3aa7701c-005c-4a9d-895d-676f02004178)

### ⭕ Ingresa tu movimiento: 7

![Captura de pantalla 2024-06-25 152250](https://github.com/OC0NER/Juego-Gato---tic-tac-toe/assets/154689355/dcec3b9f-a41d-4bd6-8bf5-fcebce1f1cc7)


### ⭕⭕⭕ ¡Has Ganado! ⭕⭕⭕

---

## Requerimientos
### Implementa las siguientes características:

- El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

      board[row][column]
 
- Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre)
la apariencia de tablero debe de ser igual a la presentada en el ejemplo.
implementa las funciones definidas para ti en el editor.

- Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

- Nota: la instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.
