__author__ = 'TR tr7550@rit.edu'
"""
CSCI-603: Queue
Author: Tejas Raval

This program implements the Queue using Nodes 
"""
from ring_buffer import RingBuffer

class Queue:
    '''
    This is a list based implementation of a Queue
    '''

    __slots__ = "RB","capacity1", "front" , "back"

    def __init__(self, capacity):
        """
               initlizes the Queue class
               :param own: slef object
               :param capacity: Capacity of the Queue
         """
        # create list of size capacity
        #self.list_stack = [None] * capacity
        self.RB = RingBuffer(capacity)
        # store as instance variable
        self.capacity1 = capacity
        # set other instance variable defaults
        self.front = None
        self.back = None
        #self.sizeIs = 0

    def __str__(self):
        """
        Convert Queue in a string format
        :param own: slef object
        :return: returns Queue in the String format
        """
        if self.capacity1==0 or self.capacity1<0:
            print("Capacity of Queue is 0 or less than 1. Can't print this Queue")
            return
        if self.size()==0:
            print("Queue is empty")
            return
        self.RB.print()

    def is_empty(self):
        """
        check if empty
        :param own: slef object
        :return: returns the true if Queue is empty or false if not
        """
        return self.front == None

    def enqueue(self, val):
        """
        Addes the element to the Queue
        :param own: slef object
        :param val: Element to be added
        """
        if self.capacity1==0 or self.capacity1<0:
            print("Capacity of Queue is 0 or less than 1. Can't use this Queue")
            return
        #self.RB.insert_keep_new(val)
        if self.is_empty() == True:
            self.front = self.RB.insert_keep_old(val)
            self.back=self.front
            return
        elif self.RB.sizeOf() == self.capacity1:
            print("Queue is full. Can't add any value")
            return
        else:
         self.back=self.RB.insert_keep_old(val)

    def dequeue(self):
        """
        Removes the element from the Queue
        :param own: slef object
        """
        if self.capacity1==0 or self.capacity1<0:
            print("Capacity of Queue is 0 or less than 1. Can't use this Queue")
            return
        #print("Is empty in deque", self.is_empty())
        if self.is_empty() == True:
            print("Queue is empty")
            return
        elif self.RB.sizeOf() == 1:
            self.front=None
            self.back=None
            self.RB.clear()
            return
        self.front= self.RB.remove_oldest()

    def peek(self):
        """
        Peek operation for the Queue
        :param own: slef object
        :Return : the first element
        """
        if self.is_empty() == True :
            print("Queue is empty")
            return
        return self.front

    def capacity(self):
        """
        Checks the capacity of the Queue
        :param own: slef object
        :Return : the capacity of the Queue
        """
        return self.capacity1
    def size(self):
        """
        Checks the size of the Queue
        :param own: slef object
        :Return : the size of the Queue
        """
        return self.RB.sizeOf()

def test():
    """
    test code for the Queue
    """
    print("Assumed Queue capacity is 5 for testing. All the test cases below are according to size 5")
    sizeOfQ=int(input("Enter size of Queue"))
    list1= Queue(sizeOfQ)
    #Assumed size is 5
    print("Testing Queue")
    list1 = Queue(sizeOfQ)
    print("Adding 1")
    list1.enqueue(1)
    print("Adding 2")
    list1.enqueue(2)
    print("Adding 2")
    list1.enqueue(3)
    print("Adding 3")
    list1.enqueue(4)
    print("Adding 5")
    list1.enqueue(5)

    print("Printing Queue")
    list1.__str__()
    print("Adding 6 but it should not be added as Queue is full")
    list1.enqueue(6)
    print("Now doing dqueue and printing the queue")
    list1.dequeue()
    list1.__str__()

    print("Adding 6 now")
    list1.enqueue(6)
    print("Printing Queue")
    list1.__str__()
    print("Checking Queue's size")
    print(list1.size())

    print("Checking Queue's capacity")
    print(list1.capacity1)

    print("Peek on Queue returns")
    print(list1.peek())

    print("Reseting the Queue with size 0")
    list1 = Queue(0)
    print("Now trying to add 1")
    list1.enqueue(1)
    print("Now trying to print Queue")
    list1.__str__()
    print("Now trying to dequeqe")
    list1.dequeue()
if __name__ == '__main__':
    test()

