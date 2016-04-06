"""
Test defaultdict array implementations using tuple subscripting.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for x in range(N):
                for y in range(N):
                    for z in range(N):
                        self.assertEqual(a[x, y, z], 0)

    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for x in range(N):
                a[x, x, x] = 1
            for x in range(N):
                for y in range(N):
                    for z in range(N):
                        self.assertEqual(a[x, y, z], x==y==z)
                    
    def _index(self, a, x, y, z):
        return a[x, y, z]

    def test_key_validity(self):
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a ,-1, 1, 1)
        self.assertRaises(KeyError, self._index, a ,1, -1, 1)
        self.assertRaises(KeyError, self._index, a ,1, 1, -1)
        self.assertRaises(KeyError, self._index, a ,10, 1, 1)
        self.assertRaises(KeyError, self._index, a ,1, 10, 1)
        self.assertRaises(KeyError, self._index, a ,1, 1, 10)

if __name__ == "__main__":
    unittest.main()