class Cuenta():
    def __init__(self, nombre, poder_adquisitivo):
        self.nombre = nombre
        self.poder_adquisitivo = poder_adquisitivo

    def ingreso(self):
        ingresos = self.poder_adquisitivo + 300
        return ingresos

    def reintegro(self):
        bonus = self.poder_adquisitivo * 0.2
        return bonus

    def transferencia(self):
        
