from math import gcd, sqrt
from functools import reduce


#Call the following functions according to number of arguments :

#list_hcf(l) - HCF of a list
#list_prime(l) - Primes in a list
#next_prime(n) - next prime of a number
#prev_prime(n) - previous prime of a number
#list_lcm(a) - LCM of a list
#hcf_k_elements(l,k) - HCF of k elements in a list
#lcm_k_elements(l, k) - LCM of k elements in a list


def list_hcf(l):
    '''
        args:
          :array: (list) : a python list
          :algo: (integer): hcf of list 
        return:
            hcf of the provided list
    '''
    x = reduce(gcd, l)
    return x
	
def list_prime(l):
    '''
        args:
          :array: (list) : a python list
          :algo: (integer): finding prime numbers
                   		    of list 
        return:
            the list of prime numbers from the provided list
    '''
    r = l[:]
    for i in l:
        if i == 1:
            r.remove(i)
            continue
        for j in range(2,int(sqrt(i))+1):
            if i%j == 0:
                r.remove(i)
                break
    return r
	
def next_prime(n):
    '''
        args:
          :number:: A python integer
          :algo: (integer): imidiate next prime 
        return:
            returns imidiate next prime 
    '''
    np=[]
    isprime=[]
    for i in range (n+1,n+200):
        np.append(i)
    for j in np:
        val_is_prime = True
        for x in range(2,j-1):
            if j % x == 0:
                val_is_prime = False
                break
        if val_is_prime:
            isprime.append(j)
    return min(isprime)


# def nextPrime(n):
#     while True:
#         n+=1
#         for i in range(2,n):
#             if n%i == 0:
#                 break
#         else:
#             return n
            
# print(nextPrime(1))
 
def prev_prime(n):
    '''
        args:
          :number:: A python integer
          :algo: (integer): imidiate previous prime 
        return:
            returns imidiate previous prime 
    '''
    while True:
        n-=1
        for i in range(2,n):
            if n%i == 0:
                break
        else:
            return n 

# def lcm(x,y):
#         '''
#         args:
#           :integer: (number) : a integer number
#           :algo: (integer): lcm of two numbers 
#         return:
#             lcm of the two numbers
#         '''
#     res=0
#     mx=max(x,y)
#     mn=min(x,y)
#     for i in range(1,mx+1,1):
#         temp=mx*i
#         try:
#             if(temp%mn==0):
#                 res=temp
#                 break
#         except ZeroDivisionError:
#             res=0
#             break
#     return res
	
def list_lcm(a):
  '''
        args:
          :array: (list) : a python list
          :algo: (integer): lcm of list 
        return:
            lcm of the provided list
  '''
  lcm = a[0]
  for i in a[1:]:
    lcm = int(lcm*i/gcd(lcm, i))
  return lcm

  
def hcf_k_elements(l,k):
    '''
        args:
          :array: (list) : a python list
          :algo: (integer): hcf of k elements of a list 
        return:
            hcf of the provided only those element which are 
			included in k places of a list
    '''
    
    def find_gcd(x, y): 
          
        while(y): 
            x, y = y, x % y 
          
        return x 
        
    num1 = l[0] 
    num2 = l[1] 
    gcd = find_gcd(num1, num2)              
      
    for i in range(2, k): 
        gcd = find_gcd(gcd, l[i]) 
        
    return gcd
	
	

def lcm_k_elements(l, k): 
    '''
        args:
          :array: (list) : a python list
          :algo: (integer): lcm of k elements of a list 
        return:
            lcm of the provided only those element which are 
			included in k places of a list
    '''      
 
    max_num = 0; 
    for i in range(k): 
        if (max_num < l[i]): 
            max_num = l[i] 
    res = 1 

    x = 2 
    while (x <= max_num): 

        indexes = [] 
        for j in range(k): 
            if (l[j] % x == 0): 
                indexes.append(j) 

        if (len(indexes) >= 2): 

            for j in range(len(indexes)): 
                l[indexes[j]] = int(l[indexes[j]] / x) 
  
            res = res * x 
        else: 
            x += 1 

    for i in range(k): 
        res = res * l[i] 
  
    return res 
