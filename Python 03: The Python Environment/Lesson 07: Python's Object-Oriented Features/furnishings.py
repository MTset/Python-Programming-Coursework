"""
furnishings.py: Allows for the creation of a Home object.  Objects of type
Furnishings can be added to the Home object to furnish specified rooms.
Methods:
- add_furnishing: accumulates a list of supplied furnishings for each room.
- map_the_home: provides a list (dict) of furnishings by room.
- furnishings_count: provides a list (dict) of furnishing total counts.

Furnishing classes: Sofa, Bookshelf, Bed, Table, Chair
"""
class Home(object):
    def __init__(self):
        self.furnishings = []
        self.room_furnishings = {}
        
    def add_furnishing(self, furnishing):
        """
        Accumulate a list of furnishing objects
        """
        self.furnishings.append(furnishing)
        
    def map_the_home(self):
        """
        Convert list of furnishing objects into a dict keyed by room.
        
        Within each room create a dict keyed by furnishing, with a value of the
        number of those furnishings within the room.  This is to allow for
        several items of the same furnishing type in the room
        """
        for furnishing in self.furnishings:
            if furnishing.room in self.room_furnishings:
                if furnishing.__class__.__name__ in self.room_furnishings[furnishing.room]:
                    self.room_furnishings[furnishing.room][furnishing.__class__.__name__] += 1
                else:
                    self.room_furnishings[furnishing.room][furnishing.__class__.__name__] = 1
            else:
                # create new dict for the room
                self.room_furnishings[furnishing.room] = {}
                self.room_furnishings[furnishing.room][furnishing.__class__.__name__] = 1

        if __name__ == "__main__":
            for room in sorted(self.room_furnishings):
                print("{0}{1}{2}{3}".format("\n", room, "\n", 15 * "-"))
                for furnishing in sorted(self.room_furnishings[room]):
                    print("{0} {1}: {2}".format(4 * " ", furnishing,
                                     self.room_furnishings[room][furnishing]))
            print("\n\n")
        return(self.room_furnishings)
    
    def furnishings_count(self):
        """
        Provide counts of each furnishing type
        """
        furnishings = {}
        for furnishing in self.furnishings:
            if furnishing.__class__.__name__ in furnishings:
                furnishings[furnishing.__class__.__name__] += 1
            else:
                furnishings[furnishing.__class__.__name__] = 1
        if __name__ == "__main__":
            print("Furnishing Counts\n" + 20 * "-")
            for furnishing in sorted(furnishings):
                print("{0} : {1}".format(furnishing, furnishings[furnishing]))
        return furnishings
        
class Furnishings(object):
    def __init__(self, room=None):
        if type(room) is str and room != "":
            self.room = room
        else:
            raise TypeError("Invalid or no room given")
        
class Sofa(Furnishings):
    def price(self):
        return 1100
    def size(self):
        return 3
    
class Bookshelf(Furnishings):
    def price(self):
        return 800
    
class Bed(Furnishings):
    def price(self):
        return 1500
    def size(self):
        return 2
    
class Table(Furnishings):
    def price(self):
        return 2000
    def size(self):
        return 6
    
class Chair(Furnishings):
    def price(self):
        return 150
    def size(self):
        return 1
    
if __name__ == "__main__":
    home = Home()
    home.add_furnishing(Bed('Bedroom'))
    home.add_furnishing(Table('Bedroom'))
    home.add_furnishing(Chair('Bedroom'))
    home.add_furnishing(Chair('Bedroom'))
    home.add_furnishing(Bookshelf('Bedroom'))
    home.add_furnishing(Table('Dining Room'))
    home.add_furnishing(Chair('Dining Room'))
    home.add_furnishing(Chair('Dining Room'))
    home.add_furnishing(Chair('Dining Room'))
    home.add_furnishing(Chair('Dining Room'))
    home.add_furnishing(Chair('Dining Room'))
    home.add_furnishing(Chair('Dining Room'))
    home.add_furnishing(Sofa('Living Room'))
    home.add_furnishing(Sofa('Living Room'))
    home.add_furnishing(Bookshelf('Living Room'))
    home.add_furnishing(Bookshelf('Living Room'))
    home.map_the_home()
    home.furnishings_count()
    
    