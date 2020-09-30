import unittest
import dsalgo
from dsalgo import linked_list
from dsalgo.linked_list import LinkedList
from dsalgo.linked_list import Node
from unittest import mock
import pytest

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list=LinkedList()
        self.node1=Node(10)
        self.assertEqual(self.node1.value,10)
        self.assertEqual(self.node1.next,None)
        self.assertEqual(self.linked_list.head,None)
        self.linked_list.head=self.node1
        self.node2=Node(20)
        self.node3=Node(30)
        self.node4=Node(40)
        self.node1.next=self.node2
        self.node2.next=self.node3
        self.node3.next=self.node4
        self.assertEqual(self.linked_list.head.value,10)
        self.array=[50, 60]

    def test_append(self):
        temp=self.linked_list.head
        self.linked_list.append(50)
        while(temp.next is not None):
            temp=temp.next
        self.assertEqual(temp.value,50)
        self.assertEqual(self.linked_list.head.value,10)

    def test_print(self):
        self.assertEqual(self.linked_list.print(),None)

    def test_to_list(self):
        list=self.linked_list.to_list()
        self.assertEqual(list,[10, 20, 30, 40])

    def test_to_linked_list(self):
        temp=self.linked_list.head
        self.linked_list.to_linked_list(self.array)
        i=1
        while i is not 7:
            self.assertEqual(temp.value,i*10)
            i=i+1
            temp=temp.next

    def test_prepend(self):
        self.assertEqual(self.linked_list.head.value,10)
        self.linked_list.prepend(5)
        self.assertEqual(self.linked_list.head.value,5)
        pass

    def test_search(self):
        node=self.linked_list.search(20)
        self.assertEqual(node.value,20)
        self.assertRaises(ValueError,self.linked_list.search,70)

    def test_remove(self):
        self.linked_list.remove(10)
        self.assertRaises(ValueError,self.linked_list.search,10)
        self.linked_list.remove(30)
        self.assertRaises(ValueError,self.linked_list.search,30)
        self.assertRaises(ValueError,self.linked_list.remove,70)
        self.linked_list.remove(20)
        self.linked_list.remove(40)
        self.assertEqual(self.linked_list.head,None)

    def test_pop(self):
        self.assertEqual(self.linked_list.head.value,10)
        value=self.linked_list.pop()
        self.assertEqual(value,10)
        self.assertEqual(self.linked_list.head.value,20)

    def test_insert(self):
        self.linked_list.insert(25,3)
        temp=self.linked_list.head
        for i in range(0,3):
            temp=temp.next
        self.assertEqual(temp.value,25)
        self.linked_list.insert(45,10)
        while temp.next is not None:
            temp=temp.next
        self.assertEqual(temp.value,45)

    def test_size(self):
        size=self.linked_list.size()
        self.assertEqual(size,4)
        self.linked_list.append(45)
        size=self.linked_list.size()
        self.assertEqual(size,5)

    def  test_reverse(self):
        new_list=self.linked_list.reverse()
        temp=self.linked_list.head
        i=1
        while i is not 5:
            self.assertEqual(temp.value,(i*10))
            i=i+1
            temp=temp.next

        temp=new_list.head
        i=4
        while i is not 0:
            self.assertEqual(temp.value,(i*10))
            i=i-1
            temp=temp.next

    def test_iscircular(self):
        self.assertFalse(self.linked_list.iscircular())
        temp=self.linked_list.head
        while temp.next is not None:
            temp=temp.next

        temp.next=self.linked_list.head
        self.assertTrue(self.linked_list.iscircular)


    def test_swap_nodes(self):
        temp=self.linked_list.head
        self.assertEqual(temp.value,10)
        temp=temp.next.next
        self.assertEqual(temp.value,30)
        temp=self.linked_list.swap_nodes(0,2)
        self.assertEqual(temp.value,30)
        temp=temp.next.next
        self.assertEqual(temp.value,10)

    def test_sort_append(self):
        self.linked_list.sort_append(15)
        self.linked_list.sort_append(35)
        temp=self.linked_list.head.next
        self.assertEqual(temp.value,15)
        temp=temp.next.next.next
        self.assertEqual(temp.value,35)

    def test_sort(self):
        unsorted_list=LinkedList()
        unsorted_list.append(20)
        unsorted_list.append(40)
        unsorted_list.append(10)
        unsorted_list.append(30)
        sorted_list=unsorted_list.sort()
        temp1=self.linked_list.head
        temp2=sorted_list.head
        while temp1 is not None:
            self.assertEqual(temp1.value,temp2.value)
            temp1=temp1.next
            temp2=temp2.next

    def test_skip_i_delete_j(self):
        head=self.linked_list.skip_i_delete_j(0,2)
        self.assertEqual(head,None)
        head=self.linked_list.skip_i_delete_j(1,2)
        head=head.next
        self.assertEqual(head.value,40)

    def test_merge_linked_list(self):
        new_list=LinkedList()
        final_list=self.linked_list.merge_linked_list(new_list)
        temp1=self.linked_list.head
        temp2=final_list.head
        while temp1 is not None:
            self.assertEqual(temp1.value,temp2.value)
            temp1=temp1.next
            temp2=temp2.next

        new_list.append(5)
        new_list.append(15)
        new_list.append(25)
        new_list.append(35)
        new_list.append(45)
        final_list=self.linked_list.merge_linked_list(new_list)
        temp1=final_list.head
        i=1
        while i is not 10:
            self.assertEqual(temp1.value,(i*5))
            temp1=temp1.next
            i=i+1

if __name__=='__main__':
    unittest.main()
