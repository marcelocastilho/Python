

class PartyAnimal:
    x = 0
    name = ''
    
    def __init__(self, name):
        self.x = 33
        self.name = name
    
    def party(self):
        self.x = self.x+1
        print(self.name, self.x)
    
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 3
        self.party()
        print(self.name, 'party count:', self.points)     
    
an = PartyAnimal('Cachorro')
an.party()
an.party()
an.party()
an.x = 90
an.party()
# print(type(an))
# print('Dir', dir(an))
PartyAnimal.party(an)

aaa = FootballFan('Gato')
aaa.party()
aaa.touchdown()


