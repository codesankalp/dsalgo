import unittest
from dsalgo.sort import Sort
import random 
class TestSort(unittest.TestCase):
    def setUp(self):
         self.testArray=[]
         self.bySort=[]
         self.revBySort=[]
         for item in range(0,5):
             self.testArray.append(round(((item*random.random())*20),2))
         self.bySort=self.testArray.copy()
         self.revBySort=self.testArray.copy()
         self.bySort.sort()
         self.revBySort.sort(reverse=True)
            
    def test_bubble(self):
         sortedArray=Sort(self.testArray,"bubble")
         self.assertEqual(self.bySort,sortedArray)
         revsortedArray=Sort(self.testArray,"bubble",True)
         self.assertEqual(self.revBySort,revsortedArray)
    
    def test_merge(self):
         sortedArray=Sort(self.testArray,"merge")
         self.assertEqual(self.bySort,sortedArray)
         revsortedArray=Sort(self.testArray,"merge",True)
         self.assertEqual(self.revBySort,revsortedArray)

    def test_bubble_recursion(self):
         sortedArray=Sort(self.testArray,"merge")
         self.assertEqual(self.bySort,sortedArray)
         revsortedArray=Sort(self.testArray,"merge",True)
         self.assertEqual(self.revBySort,revsortedArray)

    def test_selection(self):
         sortedArray=Sort(self.testArray,"merge")
         self.assertEqual(self.bySort,sortedArray)
         revsortedArray=Sort(self.testArray,"merge",True)
         self.assertEqual(self.revBySort,revsortedArray)
         
    def test_quick(self):
         sortedArray=Sort(self.testArray,"merge")
         self.assertEqual(self.bySort,sortedArray)
         revsortedArray=Sort(self.testArray,"merge",True)
         self.assertEqual(self.revBySort,revsortedArray)
     
