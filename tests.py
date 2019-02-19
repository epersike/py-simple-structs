# -*- coding: utf-8 -*-

import unittest

from stack import SimpleStack, SimpleStackPopException
from queue import SimpleQueue, SimpleQueueDequeueException


class SimpleStackTestCase(unittest.TestCase):

    def test_is_empty(self):
        stack = SimpleStack()
        assert stack.is_empty() is True

        stack.push(1)
        assert stack.is_empty() is False

        stack.pop()
        assert stack.is_empty() is True

    def test_size(self):
        stack = SimpleStack()
        assert stack.size() == 0

        stack.push(1)
        assert stack.size() == 1

        stack.pop()
        assert stack.size() == 0
        
    def test_push_items(self):
        stack = SimpleStack()

        tests = [1, '0', SimpleStack, lambda x: x, {}, [], None]

        for test in tests:
            stack.add(test)

        assert len(tests) == stack.size()

    def test_pop_items(self):
        stack = SimpleStack()

        with self.assertRaises(SimpleStackPopException):
            stack.pop()

        one = 1
        two = 2

        stack.push(one)
        stack.push(two)

        assert stack.size() == 2

        assert stack.pop() == two
        assert stack.pop() == one

        assert stack.size() == 0

    def test_print(self):
        stack = SimpleStack()

        assert str(stack) == ''

        stack.push(3)
        stack.push(1)
        stack.push(2)

        assert str(stack) == '2 -> 1 -> 3'


class SimpleQueueTestCase(unittest.TestCase):

    def test_is_empty(self):
        queue = SimpleQueue()
        assert queue.is_empty() is True

        queue.add(1)
        assert queue.is_empty() is False

        queue.dequeue()
        assert queue.is_empty() is True

    def test_size(self):
        queue = SimpleQueue()
        assert queue.size() == 0

        queue.push(1)
        assert queue.size() == 1

        queue.pop()
        assert queue.size() == 0

    def test_enqueue(self):
        queue = SimpleQueue()

        tests = [1, '0', SimpleQueue, lambda x: x, {}, [], None]

        for test in tests:
            queue.add(test)

        assert len(tests) == queue.size()

    def test_dequeue(self):
        queue = SimpleQueue()

        with self.assertRaises(SimpleQueueDequeueException):
            queue.dequeue()

        one = 1
        two = 2

        queue.add(one)
        queue.add(two)

        assert queue.size() == 2

        assert queue.dequeue() == one
        assert queue.dequeue() == two

        assert queue.size() == 0

    def test_print(self):
        queue = SimpleQueue()

        assert str(queue) == ''

        queue.add(3)
        queue.add(1)
        queue.add(2)

        assert str(queue) == '3 -> 1 -> 2'

if __name__ == '__main__':
    unittest.main()
