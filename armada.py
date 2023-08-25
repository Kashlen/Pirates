from the_pirate_ship import Ship


class Armada:

    def __init__(self, number_of_ships=int):
        self.ships = []
        for n in range(1, number_of_ships+1):
            self.ships.append(Ship())
        for ship in self.ships:
            ship.fill_ship()

    def war(self, other_armada):
        """Two armadas engage in war. Returns TRUE if this ship is the winner."""
        # Should work like merge sort.
        # First ship from the first armada battles the first one from the other.
        # The looser ship gets skipped so the next ship comes in play from the loser ship's armada.
        # It starts a battle with the first (not yet defeated) ship from the other armada.
        # Whichever armada gets to the end of its ships loses the war.
        # Returns TRUE if this ship is the winner.
