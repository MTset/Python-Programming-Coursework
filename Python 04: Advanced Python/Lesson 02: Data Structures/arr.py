"""
Class-based dict allowing tuple subscripting and sparse data
"""
from collections import defaultdict

class array:

    def __init__(self, X, Y, Z):
        "Create an defaultdict subscripted to represent a 3D matrix."
        self._data = defaultdict(int)
        self._x = X
        self._y = Y
        self._z = Z

    def __getitem__(self, key):
        "Returns the appropriate element."
        return self._data[self._validate_key(key)]
    
    def __setitem__(self, key, value):
        "Sets the appropriate element."
        self._data[self._validate_key(key)] = value
    
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        x, y, z = key
        if (x in range(self._x) and
            y in range(self._y) and
            z in range(self._z)):
            return key
        raise KeyError("Subscript out of range")