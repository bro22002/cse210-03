class TerminalService():
    """A service that handles terminal operations.

    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def outputText(self, string):
        """Prints a given string to the terminal.

        Args:
            self (TerminalService): An instance of TerminalService.
            string (string): A string to print to the console.
        """
        print(string)

    def playerInput(self, string):
        """Obtains an input from the player based on a prompt.

        Args:
            self (TerminalService): An instance of TerminalService.
            string (string): A string to use as a prompt.
        """
        return input(string).lower()