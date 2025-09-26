#primitive data types
#custom types

class Bird:
    def fly(self):
        print("Iam a flying bird")

class Parrot(Bird):
    def fly(self):
        print('Iam a parrort and i can fly')

class Ostrich(Bird):
    def fly(self, artificial_wings):
        print('Ostrich is a flightless bird but with', artificial_wings, 'it can fly')
        # Ways of violating LSP
        # 1.raise Exception("Ostrich is a flightless bird")
        # 2.print("Ostrich is a flightless bird")
        # 3.

def test_liskov(bird: Bird):
    bird.fly()

bird = Ostrich()
# bird = Parrot()
test_liskov(bird)