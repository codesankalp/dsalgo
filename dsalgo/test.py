def kmp_algo(pat, s):
        len_pat = len(pat)
        len_str = len(s)
        index = []
        pat_count = 0
        if pattern != "":
            for i in range (0,len_str):
             if pat_count<len_pat:
                 if (s[i]==pat[pat_count]):
                      pat_count+=1
                 else:
                     pat_count=0
             elif(pat_count==len_pat):
                  index.append(i-pat_count)
                  pat_count=0
        else:
            print(" error:Pattern string is empty!")
          
        return index

str="abcaabpaas"
pattern="ab"
i=kmp_algo(pattern,str)
print(i)
# for item in i:
#     print(i)