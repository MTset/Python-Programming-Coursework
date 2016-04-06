#!/usr/local/bin/python3
""" Create a list of dogs names and breeds. """
dogs = []
prev_breed = ''

class Dog:
    
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def __add__(self, dog):
        global dogs
        dogs.append(dog)
        return dogs
    
    def __str__(self):
        global prev_breed
        if prev_breed != self.breed:
            prev_breed = self.breed
            return "\n{0}. Name: {1:30}Breed: {2:30}".format(i, self.name, self.breed)
        else:
            return "{0}. Name: {1:30}Breed: {2:30}".format(i, self.name, self.breed)
        

    def __lt__(self, other):
        """Less-than comparison."""
        return self.breed < other.breed


if __name__ == "__main__":
    import clear_screen
    user_input_prompt = "Please enter your dog's name, dog's breed: \n"

    user_input = input(user_input_prompt)
    while True:
        if user_input:
            user_input = user_input.split(",")
            clear_screen.clear()
            if (len(user_input) == 2 and (user_input[0] == '' or user_input[1] == '')) or len(user_input) == 1:
                print("Missing Input Field - Please Re-Enter")
                user_input = input(user_input_prompt)
                continue
            dog = Dog(user_input[0].strip().title(), user_input[1].strip().title())
            dog.__add__(dog)
            print("DOGS - Sorted by Breed\n" + 22 * "=")
            for i, dog in enumerate(sorted(dogs)):
                print(dog)
            print(80 * "=")
            user_input = input(user_input_prompt)
        else:
            break