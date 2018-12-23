__author__ = 'zjb'
__author__ = 'Tejas Raval'
import re

from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''
class _delobj: pass
DELETED = Entry(_delobj(),None)

class Hashmap:

    __slots__ = 'table','numkeys','cap','maxload', 'probes','collisions', 'maxList', 'maxVal', 'maxKey'

    def __init__(self,initsz=100,maxload=0.5):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.probes=0
        self.collisions=0
        self.maxList=[]
        self.maxVal=1
        self.maxKey=0

    def put(self,key,value=1):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        index = self.hash_func(key) % self.cap
        if self.table[index] is not None :
            self.collisions += 1
            self.probes +=1
            while self.table[index] is not None :
                if self.table[index].key == key:
                    temp=self.table[index].value
                    temp +=1

                    p=Entry(key,value)
                    p=p._replace(value=temp)
                    self.table[index]=p._replace(value=temp)
                    if self.maxVal <= temp :
                         if self.maxVal == temp:
                             if key not in self.maxList:
                                 self.maxList.append(key)
                         else :
                             self.maxVal=temp
                             del self.maxList[:]
                             self.maxList.append(key)
                    return
                index += 1
                if index == self.cap :
                    index=0

        while self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:
            index += 1
            self.probes += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is None:
            self.probes += 1
            self.numkeys += 1
        self.table[index] = Entry(key,value)
        if self.numkeys/self.cap > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None and entry != DELETED:
                    self.put(entry.key,entry.value)


    def remove(self,key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED


    def get(self,key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.probes += 1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self,key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            self.probes += 1
            if index == self.cap:
                index = 0
        return self.table[index] is not None

    def hash_func(self,key):
        '''
        This is the first custom hash function written by me.
        :param key: Key to store
        :return: Hash value for that key
        '''
        # if we want to switch to Python's hash function, uncomment this:
        #return hash(key)
        #return len(key)

        #First hashFunction written by me
        const=31
        hash=0
        for c in range(0, len(key)):
            #print(c)
            hash +=  ((const**c)*hash+ord(key[c]))*37
        return hash

    # Second hashFunction written by me
    def hash_func2(self,key,divBy):
        '''
                This is the 2nd custom hash function written by me.
                :param key: Key to store
                :param divBy: Number by which key(string will be divied). Typically number 2
                              gives decent results.
                :return: Hash value for that key
                '''
        leng=len(key)//divBy
        sum=0
        for i in range(0,leng):
            #print(i)
            sub=key[i * divBy:(i * divBy) + divBy]
            mul=1
            for m in range(0, len(sub)):
                sum +=ord(sub[m])*mul
                mul *=256

        sub=key[0:leng*divBy]
        mul=1
        for m in range(0, len(sub)):
            sum += ord(sub[m])*mul
            mul *=256

        return sum

def printMap(map):
    for i in range(map.cap):
        print(str(i)+": " + str(map.table[i]))



def testMap():

    map = Hashmap(initsz=5)
    countword=0
    with open('Book1.txt', 'r') as f:
        for line in f:
            for word in line.split():
                countword +=1
                word=re.split('\W+',word)
                word=word[0].lower()
                map.put(word, 1)
    printMap(map)
    print("Probes:", map.probes)
    print("Collision", map.collisions)
    print("Words occurred maximum", map.maxList)
    print("Number of times it occurred :", map.maxVal)


if __name__ == '__main__':
    testMap()
