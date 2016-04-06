def three_sets():
    vowels = set("aeiou")
    b_m = set("bcdfghjklm")
    n_z = set("npqrstvwxyz")
    output = []
    
    input_str = "people enjoy programming".split()
    for w in input_str:
        output += [[vowels.intersection(w), b_m.intersection(w), n_z.intersection(w)]]
    print(output)
            
if __name__ == "__main__":
    three_sets()
        