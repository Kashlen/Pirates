from the_pirate_ship import Ship


class BattleApp:

    def main(self):
        """Creates two ships, fills them with pirates. Battle starts between them."""
        first_ship = Ship()
        second_ship = Ship()
        first_ship.fill_ship()
        second_ship.fill_ship()
        print(f"\nBATTLE STARTS. SHIPS IN THE BATTLE ARE FOLLOWING:\n")
        print(first_ship)
        print(f"\nvs.\n")
        print(second_ship)
        result = first_ship.battle(second_ship)
        if result:
            print(f"\nFIRST SHIP WON!")
        else:
            print(f"\nSECOND SHIP WON!")


