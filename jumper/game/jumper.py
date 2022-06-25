class Jumper():
    """
    Returns a picture of a falling jumper based upon the number of incorrect guesses made.

    Attributes:
        jumpers (list): A list of the jumper pictures.
    """

    def __init__(self):
        """
        Constructs a new Jumper class instance.

        Args:
            self (jumper): An instance of jumper.
        """
        self._jumpers = [
"""
  ___
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""
  _ _
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""
     
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""

  ___
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""

  _ _ 
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""


 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""



  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""




   X
  /|\\
  / \\

^^^^^^^
"""]

    def jump(self, jumper):
        """
        Returns the jumper drawing based upon the number of incorrect guesses made.

        Args:
            self (jumper): An instance of Jumper.
            jumper (int): The number of incorrect guesses made.
        """
        return self._jumpers[jumper - 1]