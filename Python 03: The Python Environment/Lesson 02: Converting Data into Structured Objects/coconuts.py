"""
Inventory Class: Coconuts of the world.
Tracks number and weight of coconuts in storage by type.
Input: Coconut (object) name, quantity
Methods: Add Coconut, Remove Coconut, Display Inventory
Output: Number of coconuts by type, Weight of coconuts by type, Total weight and count
"""
class Coconut(object):
    weight = 0
    
class South_Asian(Coconut):
    weight = 3
    
class Middle_Eastern(Coconut):
    weight = 2.5
    
class American(Coconut):
    weight = 3.5    
    
class Inventory(object):
    coconut_counts = {}
    
    def add_coconut(self, coconut=None, number=0):
        """
        Add n coconuts to inventory
        """
        try:
            coconut_id = coconut.__class__.__name__ + "_" + str(coconut.weight)
            if isinstance(coconut, Coconut):
                if coconut_id in self.coconut_counts:
                    self.coconut_counts[coconut_id] += number
                else:
                    self.coconut_counts[coconut_id] = number
            else:
                raise AttributeError("Object to be added is not a Coconut")
        except AttributeError:
            return

    def remove_coconut(self, coconut=None, number=0):
        """
        Remove n coconuts from inventory
        """
        try:
            coconut_id = coconut.__class__.__name__ + "_" + str(coconut.weight)
            if isinstance(coconut, Coconut):
                if coconut_id in self.coconut_counts:
                    if number <= self.coconut_counts[coconut_id]:
                        self.coconut_counts[coconut_id] -= number
                    else:
                        self.coconut_counts[coconut_id] = 0
            else:
                raise AttributeError("Object to be removed is not a Coconut")
        except AttributeError:
            return

    def display_inventory(self):
        """
        Display inventory summary or return raw values and totals
        """
        inventory_to_screen = []
        line = "NUT INVENTORY\n" + "-" * 13 + "\n"
        inventory_to_screen.append(line)
        coconut_type_weight = 0
        coconut_total_weight = 0
        coconut_total_number = sum(self.coconut_counts.values())
        for key in sorted(self.coconut_counts.keys()):
            coconut_name = key.split('_')
            coconut_weight = float(coconut_name.pop(-1))
            coconut_name = ' '.join(coconut_name)
            coconut_type_weight = self.coconut_counts[key] * coconut_weight
            coconut_total_weight += coconut_type_weight
            line = "{0} {1} (nuts: {2}  nett: {3})".format("=" * self.coconut_counts[key],
                    coconut_name, self.coconut_counts[key], coconut_type_weight)
            inventory_to_screen.append(line)
        line = "\nTOTAL NUMBER OF COCONUTS: {0}".format(coconut_total_number)
        inventory_to_screen.append(line)
        line = "TOTAL COCONUT WEIGHT: {0}".format(coconut_total_weight)
        inventory_to_screen.append(line)
        if __name__ == "__main__":
            for line in inventory_to_screen:
                print(line)
        else:
            return {"INVENTORIED COCONUTS": self.coconut_counts, "TOTAL NUMBER OF NUTS":  coconut_total_number,
                "TOTAL NUT WEIGHT": coconut_total_weight}
      
if __name__ == "__main__":
    inventory = Inventory()
    south_asian = South_Asian()
    inventory.add_coconut(south_asian, 3)
    inventory.remove_coconut(south_asian, 1)
    middle_eastern = Middle_Eastern()
    inventory.add_coconut(middle_eastern, 5)
    inventory.remove_coconut(middle_eastern, 4)    
    american = American()
    inventory.add_coconut(american, 5)
    inventory.remove_coconut(american, 2)    
    totals = inventory.display_inventory()