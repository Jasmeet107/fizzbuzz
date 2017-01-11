import unittest
import mock
from mock import patch
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
        #do I want to be hardcoding these values? 
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

    @mock.patch('random.random', return_value=0)
    def test_returns_correct_number_when_arbitor_returns_True(self, getrandbits_function):
        """
        Tests that the count number is returned if the arbitor returns true and it is not mod 3 or 5 
        """
        self.assertEqual(fizzbuzz_game.answer(1, 0.5), '1')
        assert getrandbits_function.called

    @mock.patch('random.random', return_value=0)
    def test_returns_correct_fizz_when_arbitor_returns_True(self, getrandbits_function):
        """
        Tests that "fizz" is returned if the arbitor returns true and the count is mod 3  
        """
        self.assertEqual(fizzbuzz_game.answer(3, 0.5), 'fizz')
        assert getrandbits_function.called

    @mock.patch('random.random', return_value=0)
    def test_returns_correct_buzz_when_arbitor_returns_True(self, getrandbits_function):
        """
        Tests that "buzz" is returned if the arbitor returns true and the count is mod 5  
        """
        self.assertEqual(fizzbuzz_game.answer(5, 0.5), 'buzz')
        assert getrandbits_function.called

    @mock.patch('random.random', return_value=0)
    def test_returns_correct_fizzbuzz_when_arbitor_returns_True(self, getrandbits_function):
        """
        Tests that "fizzbuzz" is returned if the arbitor returns true and the count is mod 3 and 5  
        """
        self.assertEqual(fizzbuzz_game.answer(15, 0.5), 'fizzbuzz')
        assert getrandbits_function.called

    @mock.patch('random.random', return_value=1)
    def test_incorrectly_returns_fizz_buzz_or_fizzbuzz_when_arbitor_returns_False(self, getrandbits_function):
        """
        Tests that "fizz", "buzz", or "fizzbuzz" is returned if the arbitor returns true and it is not mod 3 or 5 
        """
        self.assertIn(fizzbuzz_game.answer(1, 0.5), ['fizz', 'buzz', 'fizzbuzz'])
        assert getrandbits_function.called

    @mock.patch('random.random', return_value=1)
    def test_incorrectly_returns_count_buzz_or_fizzbuzz_when_arbitor_returns_False(self, getrandbits_function):
        """
        Tests that the count, "buzz", or "fizzbuzz" is returned if the arbitor returns true and the count is mod 3  
        """
        self.assertIn(fizzbuzz_game.answer(3, 0.5), ['1', 'buzz', 'fizzbuzz'])
        assert getrandbits_function.called

    @mock.patch('random.random', return_value=1)
    def test_incorrectly_returns_count_fizz_or_fizzbuzz_when_arbitor_returns_False(self, getrandbits_function):
        """
        Tests that the count, "fizz", or "fizzbuzz" is returned if the arbitor returns true and the count is mod 5  
        """
        self.assertIn(fizzbuzz_game.answer(5, 0.5), ['fizz', '5', 'fizzbuzz'])
        assert getrandbits_function.called

    @mock.patch('random.random', return_value=1)
    def test_incorrectly_returns_count_fizz_or_buzz_when_arbitor_returns_False(self, getrandbits_function):
        """
        Tests that the count, "fizz", or "buzz" is returned if the arbitor returns true and the count is mod 3 and 5  
        """
        self.assertIn(fizzbuzz_game.answer(15, 0.5), ['fizz', 'buzz', '15'])
        assert getrandbits_function.called
    
if __name__ == '__main__': 
    unittest.main()