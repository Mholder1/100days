import radbourne
import unittest

class TestCalc(unittest.TestCase):

    def test_printList(self):
        self.assertEqual(radbourne.printList(["duty", "one", "two"]), "duty, one and two.")
        self.assertEqual(radbourne.printList(["rocks", "paper", "scissors", "two"]), "rocks, paper, scissors and two.")
        self.assertEqual(radbourne.printList(["duty", "one"]), "duty and one.")

if __name__ == '__main__':
    unittest.main()