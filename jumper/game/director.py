from game.terminal_service import TerminalService
from game.puzzler import Puzzler
from game.guesser import Guesser
from game.jumper import Jumper

class Director:
    """A person who directs the game.

    The responsibility of the a Director is to control the  sequence of the play.

    Attributes:
        guesser (Guesser): Guesses letters and keeps track of previous guesses.
        puzzler (Puzzler): Chooses the word to guess.
        isPlaying (boolean): Shows if the game is still running or not.
        terminalService (TerminalService): Gets and displays information on the terminal.
    """

    def __init__(self):
        """
        Constructs a new Director class instance.

        Args:
            self (Director): an instance of Director.
        """
        self._terminalService = TerminalService()
        self._puzzler = Puzzler()
        self._guesser = Guesser()
        self._jumper = Jumper()
        self._isPlaying = True

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        self._puzzler.choose_word()
        self._guesser.update_word(self._puzzler.chosenWord)
        self._do_outputs()

        while self._isPlaying:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        
        if "_" not in self._guesser.wordProgress:
            self._terminalService.outputText("Congratulations, you had a safety jump")
        else:
            self._terminalService.outputText("Game over your are dead!")

    def _get_inputs(self):
        """Checks that it hasn't previously been guessed, and appends it to the appropriate list.

        Args:
            self (Director): An instance of Director.
        """
        repeat = True
        while repeat == True:
            guess = self._terminalService.playerInput("Please guess a letter: ")
            repeat = self._guesser.guess_repeat(guess)
            if repeat == True:
                self._terminalService.outputText("Invalid guess. Please choose another letter.\n")
        
        self._guesser.compare_guess(guess, self._puzzler.chosenWord)

    def _do_updates(self):
        """Updates the amount of the word dicovered and the progress of the jumper.

        Args:
            self (Director): An instance of Director.
        """
        self._guesser.update_word(self._puzzler.chosenWord)
        self._isPlaying = self._guesser.keep_guessing()
    
    def _do_outputs(self):
        """
        Prints the current state of the word to be guessed, and the jumper.

        Args:
            self (Director): An instance of Director.
        """
        self._terminalService.outputText(self._jumper.jump(len(self._guesser._incorrectGuesses)))
        self._terminalService.outputText(self._guesser.wordProgress)