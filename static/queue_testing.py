import unittest
from queues import Queues


class TestQueues(unittest.TestCase):
    def setUp(self):
        self.queue = Queues()

    def test_enqueue_dequeue(self):
        self.queue.enqueues(10)
        self.queue.enqueues(20)
        self.queue.enqueues(30)
        self.assertEqual(self.queue.dequeues(), 10)
        self.assertEqual(self.queue.dequeues(), 20)
        self.assertEqual(self.queue.dequeues(), 30)
        self.assertIsNone(self.queue.dequeues())

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueues(10)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeues()
        self.assertTrue(self.queue.is_empty())

    def test_peek(self):
        self.assertIsNone(self.queue.peek())
        self.queue.enqueues(10)
        self.assertEqual(self.queue.peek(), 10)
        self.queue.enqueues(20)
        self.assertEqual(self.queue.peek(), 10)

    def test_display(self):
        self.assertEqual(self.queue.display(), [])
        self.queue.enqueues(10)
        self.queue.enqueues(20)
        self.queue.enqueues(30)
        self.assertEqual(self.queue.display(), [10, 20, 30])

    def test_remove_at(self):
        self.queue.enqueues(10)
        self.queue.enqueues(20)
        self.queue.enqueues(30)
        self.assertEqual(self.queue.remove_at(1), 20)
        self.assertEqual(self.queue.display(), [10, 30])
        self.assertEqual(self.queue.remove_at(0), 10)
        self.assertEqual(self.queue.display(), [30])
        self.assertEqual(self.queue.remove_at(5), None)

if __name__ == '__main__':
    unittest.main()