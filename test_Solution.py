import filecmp
from unittest import TestCase
from Solution import Solution


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sol1: Solution = Solution('hivas.txt')

    def test_stat_hours_print(self):
        self.assertEqual(self.sol1.stat_hours_print, "6 óra 13 hívás\n7 óra 89 hívás\n8 óra 78 hívás\n9 óra 80 hívás\n10 óra 85 hívás\n11 óra 88 hívás\n12 óra 18 hívás\n13 óra 2 hívás\n15 óra 2 hívás\n17 óra 1 hívás\n18 óra 2 hívás\n")

    def test_longest_call_line(self):
        self.assertEqual(self.sol1.longest_call_line, 152)

    def test_longest_call_length(self):
        self.assertEqual(self.sol1.longest_call_length, 341)

    def test_last_accepted_call_line(self):
        self.assertEqual(self.sol1.last_accepted_call_line, 432)

    def test_accepted_callers_text(self):
        self.assertEqual(self.sol1.accepted_callers_text, "sikeres.txt elkészült")

    def test_last_caller_waiting_time(self):
        self.assertEqual(self.sol1.last_caller_waiting_time, 184)