from random import randint
from pirates import Pirate


class Ship:
    """The place for pirates."""

    def __init__(self):
        self.crew = []
        self.captain = None
        self.alive = []

    def __str__(self):
        if self.captain:
            self.alive = [pirate for pirate in self.crew if pirate.state == "alive"]
            return f"Rum consumed by the captain: {self.captain.intoxication},\nState of the captain: {self.captain.state},\nNumber of alive pirates in the crew: {len(self.alive)}"
        else:
            return f"The ship is still empty."

    def fill_ship(self):
        """Fills the ship with a captain and a random (maximum 113) number of pirates. """
        self.captain = Pirate()
        number = randint(2, 114)
        for n in range(0, number):
            self.crew.append(Pirate())
        self.alive = [pirate for pirate in self.crew if pirate.state == "alive"]
        return self.captain, self.crew, self.alive

    def battle(self, other_ship):
        """Returns TRUE if this actual ship wins. The ship having higher calculated score wins.
        Calculation: number of alive pirates in the crew minus number of consumed rum by the captain. The loser crew has
        a random number of deaths. The winning captain and crew has a party: everyone drinks a random number of rum."""
        this_ship_score = len(self.alive) - int(self.captain.intoxication)
        other_ship_score = len(other_ship.alive) - int(other_ship.captain.intoxication)
        if this_ship_score > other_ship_score:
            self.have_party()
            other_ship.defeated()
            return True
        else:
            other_ship.have_party()
            self.defeated()
            return False

    def have_party(self):
        for rum in range(1, randint(0, 5)):
            self.captain.drink_some_rum()
        for pirate in self.crew:
            for rum in range(1, randint(0, 5)):
                pirate.drink_some_rum()
        return self.crew

    def defeated(self):
        for death in range(0, randint(0, len(self.crew))):
            self.crew[death].state = "dead"
        return self.crew
