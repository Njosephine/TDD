# Liskov's Substitution Principle

class Bird:

  def fly(self):

    print('I am a flying bird')

class Parrot(Bird):

  def fly(self):

    print('I am a Parrot and I can fly')

class Ostrich(Bird):

  def fly(self):

    raise Exception("Ostrich is a flightless bird")

 

def test_liskov(bird: Bird):

  bird.fly()

bird = Ostrich()

test_liskov(bird)