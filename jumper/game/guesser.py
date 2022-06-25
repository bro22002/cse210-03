class Guesser():
    """Guesses letters and keeps track of previous guesses.

    Attributes:
        correctGuesses (list): A list of the correct guesses that the player has guessed.
        incorrectGuesses (list): A list of the incorrect guesses that the player has guessed.
        wordProgress (string): The word that needs to be guessed, with all yet undiscovered letters replaced by "_".
    """

    def __init__(self):
        """Constructs a new Guesser class instance.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self._correctGuesses = [""]
        self._incorrectGuesses = [""]
        self.wordProgress = ""

    def guess_repeat(self, guess):
        if guess in self._correctGuesses or guess in self._incorrectGuesses:
            return True
        elif len(guess) > 1:
            return True
        elif not guess.isalpha():
            return True
        else:
            return False

    def compare_guess(self, guess, chosenWord):
        """
        Checks if the guessed letter is in the word to guess. If it is, appends it to the correct guesses list. Otherwise,
        appends it to the incorrect guesses list.

        Args:
            self (Guesser): An instance of Guesser.
            guess (string): A letter guessed by the player.
            chosenWord (string): The randomly chosen word that the player needs to guess.
        """
        if guess in chosenWord:
            self._correctGuesses.append(guess)
        else:
            self._incorrectGuesses.append(guess)

    def update_word(self, chosenWord):
        """Runs through the letters in the word to guess. If they are not in the correct guesses list, replace them with "_".

        Args:
            self (Guesser): An instance of Guesser.
            chosenWord (string): The randomly chosen word that the player needs to guess.
        """
        wordChars = []
        for char in chosenWord:
            if char in self._correctGuesses:
                wordChars.append(char)
            else:
                wordChars.append("_")

        self.wordProgress = "".join(wordChars)

    def keep_guessing(self):
        """
        """
        if len(self._incorrectGuesses) == 8 or "_" not in self.wordProgress:
            return False
        else:
            return True