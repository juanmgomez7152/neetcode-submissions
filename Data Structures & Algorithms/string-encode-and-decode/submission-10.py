class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #initializing the response, so that a response is always given and concatination occurs
        # print(strs)
        for s in strs:
            # print(f"Res Before: {res}")
            conc = str(len(s)) + "#" + s # the concat var is a unique id where it is (len of letters)+ '#' symbol so that you can then strip based on the number of letters given
            #The assumption i made at first is that the enconding symbol had to be static, when you could make it dynamic
            res += conc
            # print(f"Res After: {res}")
        return res

    def decode(self, s: str) -> List[str]:
        res = [] #initialize a list as this is what var will return regardless of the size of s
        i = 0
        print(s)

        while i < len(s): #for loop through the len(s)
            # print(f"i Index: {i}")
            j = i # set the j var the same index as i
            while s[j] != '#':
                j += 1 #increase j until you get to the identifier
                # this accounts for strings that are double digit length
            # print(f"j Index: {j}")
            length = int(s[i:j]) # cast the string that represents the number to an Int; ex: "4"-> 4
            # print(f"{length}")
            i = j + 1 # because j stopped at "#" you must +1 so that you are at the initail letter
            j = i + length # to the starting letter index, add the amount of letters that are in the word
            print(f"word = {s[i:j]}")
            res.append(s[i:j]) # add the string into the list,
            #this format of string stripping is including the i index but until the j, not including the char at j
            i = j # set since j should be at the char representing the num representing the length of the word

        return res