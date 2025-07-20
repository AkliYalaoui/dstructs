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

    def test_insert_at_index(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3, 1)
        self.ll.insert(4, 0)
        self.assertEqual(list(self.ll), [4,1,3,2])

    def test_getitem(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertEqual(self.ll[0], 1)
        self.assertEqual(self.ll[1], 2)
        self.assertEqual(self.ll[2], 3)
        with self.assertRaises(IndexError):
            _ = self.ll[3]

    def test_remove(self):
        self.ll.insert(1)
        self.ll.insert(2)
        self.ll.insert(3)
        self.assertTrue(self.ll.remove(2))
        self.assertNotIn(2, self.ll)
        self.assertEqual(len(self.ll), 2)
        self.assertFalse(self.ll.remove(4))
    