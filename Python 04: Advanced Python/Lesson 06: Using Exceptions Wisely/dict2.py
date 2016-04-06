"""
Dict: Subclass of dict with KeyError handling on missing key
"""
class Dict(dict):
    def __init__(self, default_value):
        super().__init__()
        self.default_value = default_value
        
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            # If the key didn't exist, create it with the default value
            super().__setitem__(key, self.default_value)
            return super().__getitem__(key)