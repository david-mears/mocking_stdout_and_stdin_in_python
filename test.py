import unittest

from greeting import greeting

class GreetingTests(unittest.TestCase):

    def setUp(self):
        self.greeting = greeting.Greeting()

    def test_that_it_takes_user_input(self):
        greeting.input = lambda _: 'Arnold'
        self.assertEqual(self.greeting.greet(), 'Hello, Arnold')
        greeting.input = lambda _: 'Belinda'
        self.assertEqual(self.greeting.greet(), 'Hello, Belinda')

    def test_that_it_prints(self):
        pass        

if __name__ == "__main__":
    unittest.main()