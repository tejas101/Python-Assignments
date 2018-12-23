__author__ = 'TR tr7550@rit.edu'
"""
CSCI-603: Stack
Author: Tejas Raval

This program implements the Stack using Nodes 
"""
from ring_buffer import RingBuffer

class Stack:
    '''
    This is a list based implementation of a stack which will keep newest data
    and drop anything oldest that there is not room for
    '''

    __slots__ = "RB","capacity1", "top1"
    def __init__(self, capacity):
        """
        initlizes the Stack class
        :param own: slef object
        :param capacity: Capacity of the Stack
        """
        # create list of size capacity
        #self.list_stack = [None] * capacity
        self.RB = RingBuffer(capacity)
        # store as instance variable
        self.capacity1 = capacity
        # set other instance variable defaults
        self.top1 = None

    def __str__(self):
        """
        Convert Stack in a string format
        :param own: slef object
        :return: returns stack in the String format
        """
        if self.capacity1==0 or self.capacity1<0:
            print("Capacity of Stack is 0 or less than 1. Can't print Stack")
            return
        self.RB.print()

    def push(self, val):
        """
        push operation of the stack.
        :param own: slef object
        :return: returns the pushed element
        """
        if self.capacity1==0 or self.capacity1<0:
            print("Capacity of Stack is 0 or less than 1. Can't use this Stack")
            return
        if self.RB.sizeOf() == self.capacity1:
            print("As Stack is full, Removing top ", self.top1)
        self.top1=self.RB.insert_keep_new(val)
        return self.top1

    def pop(self):
        """
        pop operation of the stack.
        :param own: slef object
        :return: returns the poped element
        """
        if self.capacity1==0 or self.capacity1<0:
            print("Capacity of Stack is 0 or less than 1. Can't use this Stack")
            return
        if self.size()==0 :
            print("Stack is empty")
            return

        self.top1= self.RB.remove_newest()

    def peek(self):
        """
        peek operation of the stack.
        :param own: self object
        :return: returns the element at the top
        """
        if self.capacity1==0 or self.capacity1<0:
            print("Capacity of Stack is 0 or less than 1. Can't use this Stack")
            return

        if self.size()==0 :
            print("Stack is empty")
            return
        return self.top1

    def size(self):
        """
        check size of the stack
        :param own: self object
        :return: returns the size of the stack
        """
        return self.RB.sizeOf()

    def capacity(self):
        """
        check capacity of the stack
        :param own: self object
        :return: returns the capacity of the stack
        """
        return self.capacity1
def test():
    """
    tests the stack
    """
    print("Assumed Stack capacity is 5 for testing. All the test cases below are according to size 5")
    sizeOfS = int(input("Enter size of Stack"))
    list1= Stack(sizeOfS)
    print("Adding 1")
    list1.push(1)
    print("Adding 2")
    list1.push(2)
    print("Adding 3")
    list1.push(3)
    list1.__str__()
    print("poping ", list1.peek())
    list1.pop()
    list1.__str__()
    print("Pushing 4")
    list1.push(4)
    print("Pushing 5")
    list1.push(5)
    list1.__str__()
    print("Pushing 6")
    list1.push(6)
    list1.__str__()
    print("Pushing 7")
    list1.push(7)
    list1.__str__()
    print("Pushing 8")
    list1.push(8)
    list1.__str__()
    print("poping ",list1.peek())
    list1.pop()
    list1.__str__()
    print("poping ", list1.peek())
    list1.pop()
    list1.__str__()
    print("Peek", list1.peek())
    list1.__str__()

    print("Capacity", list1.capacity())

    print("Reseting the Stack with size 0")
    list1 = Stack(0)
    print("Now trying to add 1")
    list1.push(1)
    print("Now trying to print Stack")
    list1.__str__()
    print("Now trying to pop")
    list1.pop()


if __name__ == '__main__':
    test()

