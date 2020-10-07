import random
import unittest
from dsalgo.linked_list import LinkedList

class TestList(unittest.TestCase):
     def setUp(self):
         self.list=[]
         self.ls = LinkedList()
         for self.item in range (0,5):
             self.x=random.randint(0,10)
             self.ls.append(self.x)
             self.list.append(self.x)

     def test_append(self):
         self.assertEqual(self.list, self.ls.to_list())

     def test_headValue(self):
         self.assertEqual(self.list[0], self.ls.to_list()[0])

     def test_toLinkedlist(self):
         self.list.append(6)
         self.list.append(7)
         self.ls.to_linked_list([6, 7])
         self.assertEqual(self.list, self.ls.to_list())

     def test_insert(self):
         self.appList=self.list.copy()
         self.appList.append(100)
         self.ls.insert(100, 12)
         self.assertEqual(self.appList, self.ls.to_list())

     def test_sort(self):
         self.Sortlist=self.list.copy()
         self.Sortlist.sort(reverse=True)
         self.ls.sort()
         self.assertEqual(self.list, self.ls.to_list())

     def test_swapNodes(self):
         self.list[1],self.list[2] = self.list[2],self.list[1] 
         self.ls.swap_nodes(1, 2)
         self.assertEqual(self.list, self.ls.to_list())
     
     def test_pre(self):
         self.ls.prepend(99)
         self.list.insert(0,99)
         self.assertEqual(self.list, self.ls.to_list())
     
     def test_pop(self):
         self.ls.pop()
         self.list.pop(0)
         self.assertEqual(self.list, self.ls.to_list())
     
     def test_length(self):
         self.assertEqual(self.ls.size(),len(self.list))

