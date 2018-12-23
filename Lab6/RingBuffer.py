__author__ = 'TR tr7550@rit.edu'
"""
CSCI-603: Ring Buffer
Author: Tejas Raval

This program implements the RingBuffer using Nodes 
"""
class Node:

   def __init__(own, data=None):
       """
        Initializes a Node
        :param own: slef object
        :param data: data which this node will hold
        :return: none
        """
       own.data=data
       own.next=None


class RingBuffer:
    def __init__(own, capacity):
        """
        Initializes a Node for RingBuffer
        :param own: slef object
        :param capacity: The maximum lenght of RingBuffer
        :return: none
        """
        own.head=None
        own.tail=None
        own.capacityOf=capacity

    def print(own):
        """
        print's the RingBuffer
        :param own: slef object
        :return: result which will contain RingBuffer in String format
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        printList=own.head
        result="["
        while printList is not None:
            result += " " +str(printList.data)
            printList= printList.next
        result += " ]"
        print(result)

    def addAtFirst(own,newData):
        """
         Addes a data at the First Position in the RingBuffer
         :param own: slef object
         :param newData: Data to be added
        :return: returns the controll to caller function if data can't be added
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        NewNode=Node(newData)
        NewNode.next=own.head
        own.head=NewNode
        own.tail=NewNode
        #print("Size now is ", own.size)

    def addAtLast(own,newData):
        """
        Addes a data at the Last Position in the RingBuffer
        :param own: slef object
        :param newData: Data to be added
        :return: returns the controll to caller function if data can't be added
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        if own.tail == None:
            own.addAtFirst(newData)
            return
        NewNode=Node(newData)
        printList = own.head
        while printList.next is not None:
            printList = printList.next
        printList.next=NewNode
        printList = printList.next
        own.tail = printList
        #print("Size now is ", own.size)

    def addAnyWhere(own,newData,loc):
        """
        Addes a data at the specific Position in the RingBuffer
        :param own: slef object
        :param newData: Data to be added
        :loc newData: location where data to be added
        :return: returns the controll to caller function if data can't be added
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        #print("Size now is ", own.size+1)
        if loc == 1:
            own.addAtFirst(newData)
            own.size = own.size + 1
            return
        size=0
        NewNode=Node(newData)
        traverList=own.head
        while traverList.next is not None:
            size +=1
            if loc-1 == size:
                #print("size is",size)
                #print("at",size," is",traverList.data)
                NewNode.next=traverList.next
                traverList.next=NewNode
                own.size = own.size + 1
                return
            traverList=traverList.next
        if traverList.next is None:
            own.addAtLast(newData)
            own.size = own.size + 1
            return
    def Find(own,findIt):
        """
        Searches data in the RingBuffer
        :param own: slef object
        :param findIt: Data to be searched
        :return: returns the location of the data if its found
        """
        TempNode = own.tail
        if TempNode.data == findIt:
            print("Got",findIt," at last place")
            return

        TempNode = own.head
        if TempNode.data == findIt:
            print( "Got ",findIt," at first place")
            return

        TempNode= TempNode.next
        size=0
        #NewNode=Node(newData)
        #traverList=own.head
        while TempNode.next is not None:
            size +=1
            if TempNode.data == findIt:
                print("Got", findIt, " at index", size)
                return
            TempNode=TempNode.next

        print("Data not found")

    def removeFirst(own):
        """
        Removes the first element
        :return: returns the element removed
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        Temp=own.head
        own.head=Temp.next
        Temp=own.head
        return Temp.data
        #print("Size now is ", own.size)

    def removeLast(own):
        """
        Removes the last emelent
        :return: returns the element removed
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        Temp = own.head
        #Temp2 = own.tail
        while(Temp.next != own.tail ):
            Temp=Temp.next

        own.tail = Temp
        Temp.next = None
        return Temp.data

    def clear(own):
        """
        Clears the RingBuffer
        :param own: slef object
        """
        own.head = None
        own.tail = None

    def sizeOf(own):
        """
        Calculates the Size of the RingBuffer
        :param own: slef object
        :return: returns the size of the RingBuffer
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        len = 0
        sizeOfList = own.head
        while sizeOfList is not None:
            len += 1
            sizeOfList = sizeOfList.next

        #print("Size", len)
        return len

    def remove_oldest(own):
        """
        Removes the oldest element
        :param own: slef object
        :return: returns the removed element
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        return own.removeFirst()

    def remove_newest(own):
        """
        Removes the newest element
        :param own: slef object
        :return: returns the removed element
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        return own.removeLast()

    def insert_keep_new(own,newData):
        """
                Inserts the new element by removing the old element
                :param own: slef object
                :return: returns the added element element
                """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        if own.capacityOf == own.sizeOf():
            own.remove_newest()
            own.addAtLast(newData)

        else :
            own.addAtLast(newData)
        Temp=own.tail
        return Temp.data

    def insert_keep_old(own, newData):
        """
        Inserts the new element by keeping the old element
        :param own: slef object
        :return: returns the added element element
        """
        if own.capacityOf==0 or own.capacityOf<0:
            print("Capacity of RingBuffer is 0 or less than 1. Can't use this RingBuffer")
            return
        if own.capacityOf== own.sizeOf():
            print("RingBuffer is full. Can't add.")
            return
        if own.capacityOf == own.sizeOf():
            own.remove_oldest()
            own.addAtLast(newData)

        else:
            own.addAtLast(newData)
        Temp = own.tail
        return Temp.data

    def capacity(own):
        """
        Checks the capacity of the Ring buffer
        :param own: slef object
        :return: returns the capacity of the RingBuffer
        """
        return own.capacityOf
def test():
        """
        Test the functionality of  the RingBuffer
        """
        print("Assumed RingBuffer capacity is 5 for testing. All the test cases below are according to size 5")
        sizeOfRB = int(input("Enter size of RingBuffer"))
        list1 = RingBuffer(sizeOfRB)
        print("Adding 1")
        list1.insert_keep_new("1")
        print("Adding 2")
        list1.insert_keep_new("2")
        print("Adding 3")
        list1.insert_keep_old("3")
        print("Adding 4")
        list1.insert_keep_old("4")
        print("Orignal")
        list1.print()

        print("After insert_keep_new(5)")
        list1.insert_keep_new("5")
        list1.print()
        print("After insert_keep_new(6)")
        list1.insert_keep_new("6")
        list1.print()
        print("After insert_keep_old(7)")
        list1.insert_keep_old("7")
        list1.print()
        print("After insert_keep_old(8)")
        list1.insert_keep_old("8")
        list1.print()
        #data=
        print("Capacity is ",list1.capacity())
        print("Testing remove_newest()")
        list1.remove_newest()
        list1.print()

        print("Testing remove_oldest()")
        list1.remove_oldest()
        list1.print()
        print("Size of RingBuffer", list1.sizeOf())
        print("Capacity of RingBuffer", list1.capacity())
        print("Testing find. Searching for 3")
        list1.Find("3")

        print("Reseting the RingBuffer to capacity 0")
        list1 = RingBuffer(0)
        print("Trying to insert_keep_new(1)")
        list1.insert_keep_new("1")

# Calling the test function
if __name__ == '__main__':
    test()
