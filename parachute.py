# Create the class "Parachute"
class Parachute:
    """The image of parachute 

    The responsibility of a Parachute is to show the image of the parachute,
    get current level of the player and reduce the level when the player loses

    Attributes:
    parachute level (int): the level of the user (0-4)
    parachute image (str): a combination of syntax
    """
    """ Create a constructor
    Constructs a new Parachute
    Args:
        self(Parachute): An instance of a parachute
    """

    def __init__(self):
        # Define parachte_level and parachute(dictionary)
        self._parachute_level = 4
        self._parachute = {
            4:
            """
 _____
/_____\ 
\     /
 \   /
   0
  /|\ 
  / \\
^^^^^^^ 
            """,
            3:
            """
/_____\ 
\     /
 \   /
   0
  /|\ 
  / \ 
^^^^^^^
            """,
            2:
            """
\     /
 \   /
   0
  /|\ 
  / \ 
^^^^^^^
            """,
            1:
            """
 \   /
   0
  /|\ 
  / \ 
^^^^^^^
            """,
            0:
            """
   x
  /|\ 
  / \ 
^^^^^^^
            """
        }

    # Define get_parachute
    def get_parachute(self):
        """Gets the current parachute.

        and returns the current index of the parachute
        """
        return self._parachute[self._parachute_level]

    # Define reduce_parachute
    def reduce_parachute(self):
        """Reduces user level and parachute

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._parachute_level -= 1
      
    def get_parachute_level(self):
      """Returns the current parachute level
      """
      return self._parachute_level
