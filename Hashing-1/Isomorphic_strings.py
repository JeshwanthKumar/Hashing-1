#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}    #Initialize an empty hashmap 
        seen = set()    #Initialize a hashset as seen
        for i in range(len(s)): #Continue the loop till the length of the string(s)
            if s[i] not in hashmap: #If the string is not in hashmap check if it's already in the hashset, if not add s[i] in the hashmap and add t[i] in the hashset
                if t[i] in seen:    #If it's in hashset then immediately return False
                    return False
                hashmap[s[i]] = t[i]
                seen.add(t[i])
                
            else:   #Else check if the characters in the hashmap is not equal to the characters in t[i], if it's true then return False
                if hashmap[s[i]] != t[i]:
                    return False
                
        return True     #Return True
                     