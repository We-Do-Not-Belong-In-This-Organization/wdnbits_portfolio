import unittest
from deques import Deque


class TestDeque(unittest.TestCase):

    def setUp(self):
        self.deque = Deque()

    def test_enqueue_front(self):
        self.deque.enqueue_front(10)
        self.deque.enqueue_front(20)
        self.assertEqual(self.deque.display(), [20, 10])
        self.assertEqual(self.deque.head.data, 20)
        self.assertEqual(self.deque.tail.data, 10)

    def test_enqueue_rear(self):
        self.deque.enqueue_rear(10)
        self.deque.enqueue_rear(20)
        self.assertEqual(self.deque.display(), [10, 20])
        self.assertEqual(self.deque.head.data, 10)
        self.assertEqual(self.deque.tail.data, 20)

    def test_dequeue_front(self):
        self.deque.enqueue_rear(1)
        self.deque.enqueue_rear(2)
        self.deque.enqueue_rear(3)
        value = self.deque.dequeue_front()
        self.assertEqual(value, 1)
        self.assertEqual(self.deque.display(), [2, 3])

    def test_dequeue_rear(self):
        self.deque.enqueue_rear(1)
        self.deque.enqueue_rear(2)
        self.deque.enqueue_rear(3)
        value = self.deque.dequeue_rear()
        self.assertEqual(value, 3)
        self.assertEqual(self.deque.display(), [1, 2])

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())
        self.deque.enqueue_rear(5)
        self.assertFalse(self.deque.is_empty())
        self.deque.dequeue_front()
        self.assertTrue(self.deque.is_empty())

    def test_remove_at(self):
        for i in range(5):
            self.deque.enqueue_rear(i)  # [0,1,2,3,4]
        removed = self.deque.remove_at(2)  # remove index 2 (value 2)
        self.assertEqual(removed, 2)
        self.assertEqual(self.deque.display(), [0, 1, 3, 4])

        # Remove first and last
        self.deque.remove_at(0)
        self.deque.remove_at(self.deque.length() - 1)
        self.assertEqual(self.deque.display(), [1, 3])

    def test_remove_at_out_of_range(self):
        for i in range(3):
            self.deque.enqueue_rear(i)
        result = self.deque.remove_at(5)  # invalid index
        self.assertIsNone(result)

    def test_clear(self):
        self.deque.enqueue_rear(1)
        self.deque.enqueue_rear(2)
        self.deque.clear()
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(self.deque.display(), [])

    def test_length(self):
        for i in range(4):
            self.deque.enqueue_rear(i)
        self.assertEqual(self.deque.length(), 4)
        self.deque.dequeue_front()
        self.assertEqual(self.deque.length(), 3)
        self.deque.clear()
        self.assertEqual(self.deque.length(), 0)

    def test_display(self):
        self.deque.enqueue_rear('a')
        self.deque.enqueue_rear('b')
        self.deque.enqueue_front('c')
        self.assertEqual(self.deque.display(), ['c', 'a', 'b'])


if __name__ == '__main__':
    unittest.main()
