import random


class Pirate:

    def __init__(self):
        self.state = "alive"
        self.intoxication = 0

    def drink_some_rum(self):
        """
        intoxicates the Pirate by one
        """
        if self.state == "dead":
            print("He's dead.")
        else:
            self.intoxication += 1
            return self.intoxication

    def hows_it_going_mate(self):
        """
        When called, the Pirate replies:
        - if drinkSomeRum was called less than 4 times: "Pour me anudder!"
        - else: "Arghh, I'ma Pirate. How d'ya d'ink its goin?" Then the pirate passes out and sleeps it off (gets rid
        of intoxication).
        """
        if self.state == "dead":
            print("He's dead.")
        elif self.intoxication < 4:
            print("Pour me anudder!")
        else:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
            self.intoxication = 0
            return self.intoxication

    def brawl(self, second_pirate):
        """
        Pirate fights another pirate (if both of them are alive):
        - there is 1/3 chance that this dies, the other dies or they both pass out. - die()
        """
        if self.state and second_pirate.state == "alive":
            possible_states = ["This pirate dies.", "The second pirate dies.", "Both pirates passed out."]
            result = random.choice(possible_states)
            print(result)
        else:
            print("He's dead.")
        if result == possible_states[0]:
            return self.die()
        elif result == possible_states[1]:
            return second_pirate.die()
        else:
            return self.die(), second_pirate.die()

    def die(self):
        """This kills off the pirate. When a pirate is dead, every method simply results in 'he's dead'."""
        self.state = "dead"
        return self.state

# TODO: Would it be possible to add "He's dead." to decorator or make it simpler somehow???

