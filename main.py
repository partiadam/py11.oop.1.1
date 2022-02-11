'''
1.1 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
'''


class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
        

    def terulet(self):
        return self.oldalhossz ** 2

    def kerulet(self):
        return self.oldalhossz * 4 

negyzet = Negyzet(3)
print(f'A négyzet területe: {negyzet.terulet()}, kerülete: {negyzet.kerulet()}')