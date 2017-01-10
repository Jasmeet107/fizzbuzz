import unittest
from src import fizzbuzz_game

class TestFizzBuzzGame(unittest.TestCase): 

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_evaluates_correct_number(self):
        """
        Tests that a valid integer is properly evaluated based on the count
        """
        self.assertEqual(fizzbuzz_game.evaluate(1), '1')
        
    def test_evaluates_correct_fizz(self):
        """
        Tests that a valid mod 3 integer is properly evaluated based on the count
        """
        self.assertEqual(fizzbuzz_game.evaluate(3), 'fizz')

    def test_evaluates_correct_buzz(self):
        """
        Tests that a valid mod 5 integer is properly evaluated based on the count 
        """
        self.assertEqual(fizzbuzz_game.evaluate(5), 'buzz')

    def test_evaluates_correct_fizzbuzz(self):
        """
        Tests that a valid mod 3 and 5 integer is properly evaluated based on the count 
        """
        self.assertEqual(fizzbuzz_game.evaluate(15), 'fizzbuzz')

    
if __name__ == '__main__': 
    unittest.main()