import array
import random

import array
def f7(list):
    return array.array('B', list).tostring()

def g2(string):
    return array.array('b', string).tolist()

if __name__ == "__main__":
#    rand_alpha_list = [array.array('B', [random.sample(range(65,91), 1)[0]]).tostring() for _ in range(999)]
    rand_alpha_list = "".join([chr(random.sample(range(65,91), 1)[0]) for _ in range(999)])
#    print(array.array('B', map(ord,rand_alpha_list)).tostring())
    print(rand_alpha_list)
#    for c in map(chr, range(65, 91)):
#        print(c)
#    print(f7(rand_alpha_list))
#    print(g2([97,98,99]))