from armada import Armada
from random import randint


class WarApp:

    def main(self):
        """Creates two armadas with filled ships which have a war."""
        n = randint(10, 31)
        m = randint(10, 31)
        armada_1 = Armada(n)
        armada_2 = Armada(m)
        print(f"Two armadas were created. First one has {len(armada_1.ships)} ships, second one has {len(armada_2.ships)}.")
        result = armada_1.war(armada_2)
        if result:
            print(f"The first armada won the war.")
        else:
            print(f"The second armada won the war.")
