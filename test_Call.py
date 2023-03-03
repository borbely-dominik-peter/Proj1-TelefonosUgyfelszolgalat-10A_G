from unittest import TestCase
from Call import Call


class TestCall(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.call1: Call = Call('6 51 8 6 54 58')
        cls.call2: Call = Call('6 52 30 6 57 54')
        

    def test_first_hour(self):
        self.assertEqual(self.call1.first_hour, 6)
        self.assertEqual(self.call2.first_hour, 6)

    def test_first_min(self):
        self.assertEqual(self.call1.first_min, 51)
        self.assertEqual(self.call2.first_min, 52)

    def test_first_sec(self):
        self.assertEqual(self.call1.first_sec, 8)
        self.assertEqual(self.call2.first_sec, 30)

    def test_last_hour(self):
        self.assertEqual(self.call1.last_hour, 6)
        self.assertEqual(self.call2.last_hour, 6)

    def test_last_min(self):
        self.assertEqual(self.call1.last_min, 54)
        self.assertEqual(self.call2.last_min, 57)

    def test_last_sec(self):
        self.assertEqual(self.call1.last_sec, 58)
        self.assertEqual(self.call2.last_sec, 54)

    def test_start_in_sec(self):
        self.assertEqual(self.call1.start_in_sec, 24668)
        self.assertEqual(self.call2.start_in_sec, 24750)

    def test_end_in_sec(self):
        self.assertEqual(self.call1.end_in_sec, 24898)
        self.assertEqual(self.call2.end_in_sec, 25074)

    def test_call_length(self):
        self.assertEqual(self.call1.call_length, 230)
        self.assertEqual(self.call2.call_length, 324)


