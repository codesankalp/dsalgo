import re


class StringAlgo:
    def string_is_url(self, s):
        # Using regular experession to extract URL from given string
        self.regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(self.regex, s)
        return [x[0] for x in url]

    def kmp_malgo(self, pat, s):
        """
        Modified kmp algo:

        Params:1.pat:Pattern string of length n>0 and not single char.
               2.s:Long string which required for pattern searching.
        return:List of index of first occurence of pattern.

        """
        self.len_pat = len(pat)
        self.len_str = len(s)
        self.index = []
        pat_count = 0
        if pat != "" and self.len_pat != 1:
            for i in range(0, self.len_str):
             if pat_count < self.len_pat:
                 if (s[i] == pat[pat_count]):
                      pat_count += 1
                 else:
                     pat_count = 0
             elif(pat_count == self.len_pat):
                  self.index.append(i-pat_count)
                  pat_count = 0
        else:
            print(" error:Pattern string is empty OR one char long!")
        return self.index
    def is_palindrome(self,s):
        if s==s[::-1]:
          return True
        else:
          return False
    # Rabin-Karp algorithm in python
    def search(self,pattern, text, q):
       d=10
       m = len(pattern)
       n = len(text)
       p = 0
       t = 0
       h = 1
       i = 0
       j = 0
 
       for i in range(m-1):
          h = (h*d) % q
 
       # Calculate hash value for pattern and text
       for i in range(m):
          p = (d*p + ord(pattern[i])) % q
          t = (d*t + ord(text[i])) % q
 
       # Find the match
       for i in range(n-m+1):
          if p == t:
                for j in range(m):
                   if text[i+j] != pattern[j]:
                      break
 
                j += 1
                if j == m:
                   print("Pattern is found at position: " + str(i+1))
 
          if i < n-m:
                t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
 
                if t < 0:
                   t = t+q
 

string="abcaab"
obj=StringAlgo()
ind=obj.is_palindrome(string)
print(ind)
