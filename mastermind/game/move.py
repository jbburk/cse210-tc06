class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _pile (integer): The pile to remove from.
        _stones (integer): The number of stones to remove.
    """
    def __init__(self, stones, pile):
        self._pile = pile
        self._stones = stones

    def get_pile(self):
        return self._pile

    def get_stones(self):
        return self._stones