from abc import ABC, abstractmethod

class Racional(ABC):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.simplificar()

    def simplificar(self):
        gcd_val = self.gcd(self.p, self.q)
        self.p //= gcd_val
        self.q //= gcd_val

    @abstractmethod
    def gcd(self, a, b):
        pass

    @abstractmethod
    def operar(self, otro):
        pass

    def __str__(self):
        return f"{self.p}/{self.q}"

class RacionalDecimal(Racional):
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def operar(self, otro):
        nuevo_p = self.p * otro.q + otro.p * self.q
        nuevo_q = self.q * otro.q
        return RacionalDecimal(nuevo_p, nuevo_q)

num1 = input("Ingrese el primer número racional (p/q): ")
num2 = input("Ingrese el segundo número racional (p/q): ")

p1, q1 = map(int, num1.split('/'))
p2, q2 = map(int, num2.split('/'))

racional1 = RacionalDecimal(p1, q1)
racional2 = RacionalDecimal(p2, q2)

resultado = racional1.operar(racional2)
print("Resultado:", resultado)