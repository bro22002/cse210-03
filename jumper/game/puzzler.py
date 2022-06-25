import random

class Puzzler():
    """
    Chooses the random word that guesser needs to discover.

    Attributes:
        words (list): A list of possible words to choose from.
        selection (string): The randomly chosen word that the guesser needs to discover. 
        chosenWord (list): The randomly chosen word that the guesser needs to discover split into individual characters. 
    """

    def __init__(self):
        """
        Constructs a new Puzzler class instance.

        Args:
            self (Puzzler): An instance of Puzzler.
        """
        self._words = ["helicopter", "triangle", "rhythm", "disaster", "reptile", "revelation"]
        self._selection = ""
        self.chosenWord = []

    def choose_word(self):
        """
        Randomly chooses a word from a list.

        Args:
            self (Puzzler): An instance of Puzzler.
        """
        self._selection = self._words[random.randint(0, len(self._words) - 1)]
        for char in self._selection:
            self.chosenWord.append(char)