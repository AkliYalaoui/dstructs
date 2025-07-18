import unittest
from dstructs.linear import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_and_length(self):
        self.ll.insert(1)
        self.assertEqual(len(self.ll), 1)
        self.ll.insert(2)
        self.assertEqual(len(self.ll), 2)

    def test_contains(self):
        self.ll.insert(1)
        self.assertIn(1, self.ll)
        self.assertNotIn(2, self.ll)

    def test_insert_at_tail(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.assertIn(2, self.ll) 