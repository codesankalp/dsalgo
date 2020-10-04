class dmath():
    '''
    dmath: discrete mathematics class
    #Call the following functions according to number of arguments :
    gcd(int a,int b)- gcd of two numbers
    list_gcd(list_type_array) - gcd of a list
    lcm(a,b) - returns lcm of two numbers
    list_lcm(list_type_array) - LCM of a list
    is_prime(number) - returns boolean true if number is prime
    list_prime(list_type_array) - Primes in a list
    next_prime(number) - next prime of a number
    prev_prime(number) - previous prime of a number
    series_prime(self,start = 2,count=10,reverse=False,end=None) - returns \
    list type array of prime as per arguments
    '''

    def gcd(self, a, b):
        '''
            args: int a ,int b
            logic: eucledians gcd
            returns: gcd of two integers

        '''
        while(b):
            a, b = b, a % b
        return a

    def list_gcd(self, list_array):
        '''
            args:
            :array: (list) : a python list
            :algo: (integer): hcf of list
            return:
                hcf of the provided list
        '''
        GCD = self.gcd(list_array[0], list_array[1])
        for el in range(2, len(list_array)):
            GCD = self.gcd(GCD, list_array[el])
        return GCD

    def lcm(self, a, b):
        '''
            args: int a ,int b
            logic:  a * b = gcd * lcm
            returns: lcm of two integers

        '''
        return (a*b)//self.gcd(a, b)

    def list_lcm(self, list_array):
        '''
            args:
            :array: (list) : a python list
            :algo: (integer): lcm of list
            return:
                lcm of the provided list
        '''
        LCM = list_array[0]
        for el in range(1, len(list_array)):
            LCM = self.lcm(LCM, list_array[el])

        return LCM

    def is_prime(self, number):
        '''
            args:
            - number - input number to check if it is prime or not

            returns - bool value (true if number is prime else false)
        '''
        i = 2
        while (i*i) <= number:
            if number % i == 0:
                return False
            i += 1
        return True

    def next_prime(self, number):
        '''
            args:
            - number - input number of which successive prime is needed
              returns - prime succeeding to input number
        '''
        if self.is_prime(number):
            return number
        else:
            while(True):
                number += 1
                if self.is_prime(number):
                    return number

    def prev_prime(self, number):
        '''
            args:
            - number - input number of which previous prime is needed
              returns - prime preceeding to input number
        '''
        while True:
            number -= 1
            if self.is_prime(number):
                return number

    def list_prime(self, list_array):
        '''
            args:
            - list_array -input list of integers from which primes are required
              returns - list of prime numbers
        '''
        return [n for n in list_array if self.is_prime(n)]

    def series_prime(self, start=2, count=10, reverse=False, end=None):
        '''
            args:
            - start - from which prime count needs to start
            - end - upto which prime counting needs to be done
            - reverse - whether counting succeed or preceed
            - count - how many primes needed

            returns- list

            note while passing reverse == True start must be the number from \
            where prime needs to be calculated
        '''
        n_count = 0
        p_list = []
        if end is None and reverse is False:
            while (n_count < count):
                if self.is_prime(start):
                    p_list.append(start)
                    n_count += 1
                start += 1
            return p_list

        elif end is None and reverse is True:
            while(start > 0 and n_count < count):
                if self.is_prime(start):
                    p_list.append(start)
                    n_count += 1
                start -= 1
            return p_list

        elif end is not None and reverse is False:
            while(start <= end and n_count < count):
                if self.is_prime(start):
                    p_list.append(start)
                    n_count += 1
                start += 1
            return p_list

        else:
            while(start >= end and n_count < count):
                if self.is_prime(start):
                    p_list.append(start)
                    n_count += 1
                start -= 1
            return p_list
