import unittest
import prime 

class TestPrime(unittest.TestCase):

    def test_generatePrimes(self):
        self.assertEqual(prime.generatePrimes(10,100), [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(prime.generatePrimes(0,135), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47, 53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131])

    def test_Sieve(self):
        self.assertEqual(prime.SieveOfEratosthenes(23,250), [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241])
        self.assertEqual(prime.SieveOfEratosthenes(34,106), [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103])


if __name__ == "__main__":
    unittest.main()