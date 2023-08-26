from the_pirate_ship import Ship


class Armada:

    def __init__(self, number_of_ships=int):
        self.ships = []
        for n in range(1, number_of_ships+1):
            self.ships.append(Ship())
        for ship in self.ships:
            ship.fill_ship()

    def war(self, other_armada):
        """
        Two armadas engage in war. Returns TRUE if this ship is the winner.
        Whichever armada gets to the end of its ships loses the war.
        """
        this_armada_index = 0
        other_armada_index = 0
        while this_armada_index < len(self.ships) and other_armada_index < len(other_armada.ships):
            result = self.ships[this_armada_index].battle(other_armada.ships[other_armada_index])
            if result:
                other_armada_index += 1
            else:
                this_armada_index += 1
        if this_armada_index == len(self.ships):
            return False
        if other_armada_index == len(other_armada.ships):
            return True
