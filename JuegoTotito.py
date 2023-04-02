import random
import math
import os

#X is max = 1
#O in min = -1

class Programa:
    def __init__(self):
        self.tablero1 = ['-' for _ in range(9)]
        if random.randint(0, 1) == 1:
            self.jugador = 'X'
            self.computadora = "O"
        else:
            self.jugador = "O"
            self.computadora = "X"
    
    #Tablero
    def Tablero(self):
        print("")
        for i in range(3):
            print("  ",self.tablero1[0+(i*3)]," | ",self.tablero1[1+(i*3)]," | ",self.tablero1[2+(i*3)])
            print("")
            
    def tableroLLevo(self,estado):
        return not "-" in estado

    def ganaJugador(self,estado,player):
        if estado[0]==estado[1]==estado[2] == player: return True
        if estado[3]==estado[4]==estado[5] == player: return True
        if estado[6]==estado[7]==estado[8] == player: return True
        if estado[0]==estado[3]==estado[6] == player: return True
        if estado[1]==estado[4]==estado[7] == player: return True
        if estado[2]==estado[5]==estado[8] == player: return True
        if estado[0]==estado[4]==estado[8] == player: return True
        if estado[2]==estado[4]==estado[6] == player: return True

        return False

    def revisarGanador(self):
        if self.ganaJugador(self.tablero1,self.jugador):
            os.system("cls")
            print(f"    {self.jugador} ganaste")
            return True
            
        if self.ganaJugador(self.tablero1,self.computadora):
            os.system("cls")
            print(f"    {self.computadora} perdiste")
            return True

        if self.tableroLLevo(self.tablero1):
            os.system("cls")
            print("   Empate!")
            return True
        return False

    def start(self):
        bot = JugadorComputadora(self.computadora)
        humano = jugador(self.jugador)
        while True:
            os.system("cls")
            print(f"   Turno de {self.jugador} ")
            self.Tablero()
            
            #Humano
            square = humano.movimientoJugador(self.tablero1)
            self.tablero1[square] = self.jugador
            if self.revisarGanador():
                break
            
            #Bot
            square = bot.movimientoComputadora(self.tablero1)
            self.tablero1[square] = self.computadora
            if self.revisarGanador():
                break
       
        print()
        self.Tablero()

class jugador:
    def __init__(self,letter):
        self.letter = letter
    
    def movimientoJugador(self,estado):
        while True:
            square =  int(input("Elija la casilla en la que quiere colocar X del 1-9: "))
            print()
            if estado[square-1] == "-":
                break
        return square-1

class JugadorComputadora(Programa):
    def __init__(self,letter):
        self.computadora = letter
        self.jugador = "X" if letter == "O" else "O"

    def Jugadores(self,estado):
        n = len(estado)
        x = 0
        o = 0
        for i in range(9):
            if(estado[i] == "X"):
                x = x+1
            if(estado[i] == "O"):
                o = o+1
        
        if(self.jugador == "X"):
            return "X" if x==o else "O"
        if(self.jugador == "O"):
            return "O" if x==o else "X"
    
    def Acciones(self,estado):
        return [i for i, x in enumerate(estado) if x == "-"]
    
    def Resultado(self,estado,action):
        nuevoEstado = estado.copy()
        player = self.Jugadores(estado)
        nuevoEstado[action] = player
        return nuevoEstado
    
    def terminal(self,estado):
        if(self.ganaJugador(estado,"X")):
            return True
        if(self.ganaJugador(estado,"O")):
            return True
        return False

    def movimientoComputadora(self,estado):
        square = self.minimax(estado,self.computadora)['posicion']
        return square

    def minimax(self, estado, player):
        max_player = self.jugador  
        otroJugador = 'O' if player == 'X' else 'X'

        if self.terminal(estado):
            return {'posicion': None, 'puntuacion': 1 * (len(self.Acciones(estado)) + 1) if otroJugador == max_player else -1 * (
                        len(self.Acciones(estado)) + 1)}
        elif self.tableroLLevo(estado):
            return {'posicion': None, 'puntuacion': 0}

        if player == max_player:
            best = {'posicion': None, 'puntuacion': -math.inf}  
        else:
            best = {'posicion': None, 'puntuacion': math.inf}  
        for possible_move in self.Acciones(estado):
            nuevoEstado = self.Resultado(estado,possible_move)
            sim_score = self.minimax(nuevoEstado, otroJugador)  

            sim_score['posicion'] = possible_move  

            if player == max_player:
                if sim_score['puntuacion'] > best['puntuacion']:
                    best = sim_score
            else:
                if sim_score['puntuacion'] < best['puntuacion']:
                    best = sim_score
        return best

#Llamar al totito
juego = Programa()
juego.start()