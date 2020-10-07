class Strings:

    def encode(self, strs):
        """
        It is an algorithm to encode a list of strings to a string.
        The encoded mystring is then sent over the decoded()
        back to the original list of strings.
        eg:"Are you there"--> "3:Are3:you5:there"
        where k:str represents
        number of char of given word.

        Encodes a list of strings to a single string.
        params: List[str]
        returns: str
        """
        res = ""
        for string in strs.split():
            res += str(len(string)) + ":" + string
        return res

    def decode(self, s):
        """
        Decode() is just opposite of encode that is instead of
        encoding main string into other form
        it takes encoded string and convert it back to original state.
        Decodes a given string to a list of strings and each index of list contain word.
        eg:"3:Are3:you5:there" --> ['Are', 'you', 'there']
        
        params: str
        returns: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            index = s.find(":", i)
            size = int(s[i:index])
            strs.append(s[index+1:index+1+size])
            i = index + 1 + size
        return strs

    def repeat_substring(self,s):
          """
          Given a non-empty string check if it can
          be constructed by taking
          a substring of it and appending multiple
          copies of the substring together.
          For example:
          Input: "abab"
          Output: True
          Explanation: It's the substring "ab" twice.  

          params: str
          returns: bool
          """
          str = (s + s)[1:-1]
          return s in str

    def longest_palindrome(self, s):
        """
        params: string
        returns:longest palindrome string

        Given string s, find the longest palindromic substring.
        Example1:

        Input: "dasdasdasdasdasdadsa"
        Output: "asdadsa"
        Example2:
        Input: "acdbbdaa"
        Output: "dbbd"
        Manacher's algorithm
        """
        if len(s) < 2:
            return s

        n_str = "#" + "#".join(s) + "#"
        p = [0] * len(n_str)
        mx, loc = 0, 0
        index, maxlen = 0, 0
        for i in range(len(n_str)):
            if i < mx and 2 * loc - i < len(n_str):
                p[i] = min(mx - i, p[2 * loc - i])
            else:
                p[i] = 1

            while (
                p[i] + i < len(n_str)
                and i - p[i] >= 0
                and n_str[i - p[i]] == n_str[i + p[i]]
            ):
                p[i] += 1

            if i + p[i] > mx:
                mx = i + p[i]
                loc = i

            if p[i] > maxlen:
                index = i
                maxlen = p[i]
        s = n_str[index - p[index]+1:index+p[index]]
        return s.replace("#", "")

    def roman_to_int(self, s: "str") -> "int":
        """
        params:string
        returns:int

        Given a roman numeral, convert it to an integer.
        Input is guaranteed to be within the
        range from 1 to 3999.
        """
        number = 0
        rom = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in range(len(s) - 1):
            if rom[s[i]] < rom[s[i + 1]]:
                number -= rom[s[i]]
            else:
                number += rom[s[i]]
        return number + rom[s[-1]]
