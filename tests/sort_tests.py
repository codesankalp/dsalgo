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
     
    def test_radix(self):
      self.tarray=[2,7,5,1]
      self.bsort=self.tarray.copy()
      self.rsort=self.tarray.copy()
      self.bsort.sort()
      self.rsort.sort(reverse=True)
      sortedArray=Sort(self.tarray,"radix")
      self.assertEqual(self.bsort,sortedArray)
      revsortedArray=Sort(self.tarray,"radix",True)
      self.assertEqual(self.rsort,revsortedArray)

    def test_bucket(self):
            self.tarray=[2,7,5,1]
            self.bsort=self.tarray.copy()
            self.rsort=self.tarray.copy()
            self.bsort.sort()
            self.rsort.sort(reverse=True)
            sortedArray=Sort(self.tarray,"bucket")
            self.assertEqual(self.bsort,sortedArray)
            revsortedArray=Sort(self.tarray,"bucket",True)
            self.assertEqual(self.rsort,revsortedArray)

    def test_bitonic(self):
            self.tarray=[2,7,5,1]
            self.bsort=self.tarray.copy()
            self.rsort=self.tarray.copy()
            self.bsort.sort()
            self.rsort.sort(reverse=True)
            sortedArray=Sort(self.tarray,"bitonic")
            self.assertEqual(self.bsort,sortedArray)
            revsortedArray=Sort(self.tarray,"bitonic",True)
            self.assertEqual(self.rsort,revsortedArray)
      
          

if __name__=='__main__':
    unittest.main()




