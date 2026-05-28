class Taxi:
    # 
    # 
    # 
    
    def __init__(self, archivo_matriz):
        """
        Inicializa el taxi leyendo la matriz del archivo.
        """
        self.matriz = self._cargar_matriz(archivo_matriz)
        self.x = 0
        self.y = 0
        self.pasajeros_recogido = 0
        self.pasajeros_totales = 0
        self._inicializar_posicion()
        
    def _cargar_matriz(self, archivo):
        """Carga la matriz desde el archivo."""
        matriz = []
        with open(archivo, "r") as archivo_matriz:
            for linea in archivo_matriz:
                fila = linea.strip().split()
                # Filtra solo los números, ignora el número de línea (ej: "1.", "2.", etc)
                fila = [int(x) for x in fila if x.isdigit()]
                if fila:
                    matriz.append(fila)
        return matriz
    
    def _inicializar_posicion(self):
        """
        Lee la matriz para encontrar:
        - Posición inicial del taxi (valor 2)
        - Cantidad de pasajeros (valores 4 y 3)
        """
        for y in range(len(self.matriz)):
            for x in range(len(self.matriz[y])):
                valor = self.matriz[y][x]
                
                # Encontrar posición inicial del taxi
                if valor == 2:
                    self.x = x
                    self.y = y
                
                # Contar pasajeros
                if valor == 4 :
                    self.pasajeros_totales += 1
    
    def up(self):
        """Mueve el taxi hacia arriba (disminuye y)."""
        if self.y > 0 and self.matriz[self.y - 1 ][self.x] != 1:
            self.y -= 1
            return True
        return False
    
    def down(self):
        """Mueve el taxi hacia abajo (aumenta y)."""
        if self.y < len(self.matriz) - 1 and self.matriz[self.y + 1][self.x] != 1:
            self.y += 1
            return True
        return False
    
    def left(self):
        """Mueve el taxi hacia la izquierda (disminuye x)."""
        if self.x > 0 and self.matriz[self.y][self.x - 1] != 1:
            self.x -= 1
            return True
        return False
    
    def right(self):
        """Mueve el taxi hacia la derecha (aumenta x)."""
        if self.x < len(self.matriz[self.y]) - 1 and self.matriz[self.y][self.x + 1] != 1:
            self.x += 1
            return True
        return False
    
    def recoger_pasajero(self):
        """Recoge un pasajero en la posición actual."""
        valor_actual = self.matriz[self.y][self.x]
        if valor_actual == 4 or valor_actual == 3:
            self.pasajeros_recogido += 1
            self.matriz[self.y][self.x] = 0
            return True
        return False
    
    def get_posicion(self):
        """Retorna la posición actual del taxi como tupla (x, y)."""
        return (self.x, self.y)
    
    def get_estado(self):
        """Retorna el estado actual del taxi."""
        return {
            'x': self.x,
            'y': self.y,
            'pasajeros_recogido': self.pasajeros_recogido,
            'pasajeros_totales': self.pasajeros_totales,
            'matriz': self.matriz
        }