from typing import Any


class MyStack:
    """A class representing a stack data structure."""

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, element=None) -> bool:
        """Push an element onto the stack."""

        self.stack.append(element)
        return True

    def pop(self) -> Any:
        """Remove and return the top element from the stack.

        Returns:
            Any: The top element of the stack.
        """
        if not self.stack:
            return None
        else:
            return self.stack.pop()

    def peek(self) -> Any:
        """Return the top element from the stack without removing it.

        Returns:
            Any: The top element of the stack.
        """
        if not self.stack:
            return ""
        else:
            return self.stack[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.size() == 0

    def size(self) -> int:
        """Return the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self.stack = []


def is_nested(string):
    stack = MyStack()
    couples = "()[]{}"
    for element in string:
        if element in "[{(":
            stack.push(element)
        elif element in ")}]":
            if stack.peek() + element in couples:
                stack.pop()
        else:
            print("invalid input")
    return stack.is_empty()


def test(func):
    legals = ['(()[[]][])',
              '[[]{}{{}}]',
              '{[]{[][]}}',
              '()((){[]})',
              '{([][]{})}',
              '[[][()]]{}',
              '(([]{[]}))',
              '[]{[[]{}]}',
              '{[[]]{}}()',
              '{{}}[{()}]']
    illegal = ['}}))[{)({]',
               '{)({([)){}',
               '{{}[((]}}]',
               '[){{{{{)}(',
               '{}[[}]}(]{',
               '}[]]{[})[{',
               '][[([}[)()',
               '[)(]){]}(]',
               '(]}}[)})]]',
               '[)((])]{(}']
    for s in legals:
        assert func(s), s
    for s in illegal:
        assert not func(s), s


test(is_nested)
