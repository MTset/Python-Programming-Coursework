"""
centipede.py: Demonstrates the use of special methods, attribute use and protection.
"""
class Centipede:
    def __init__(self):
        stomach = [] # list of stomach contents
        legs = [] # list of other attributes
        protected = locals().keys()
        self.__dict__.update(locals())
        
    def __call__(self, *food):
        if food:
            self.stomach.extend(food)
            
    def __setattr__(self, attr, value):
        " Protect internal only attributes. "
        if attr in self.protected:
            raise AttributeError("{0} is for internal use only".format(attr))
        self.legs.append(attr)
        self.__dict__[attr] = value

    def __str__(self):
        return  ",".join(self.stomach)
    
    def __repr__(self):
        return (",".join(self.legs))
    
if __name__ == "__main__":
    ralph = Centipede()
    ralph('cracker', 'jam')
    ralph('coconut')
    print(ralph)
    ralph.friends = ['Steve', 'Daniel', 'Guido']
    ralph.favorite_show = "Monty Python's Flying Circus"
    ralph.age = '31'
    print(repr(ralph))
    print(ralph.__dict__)