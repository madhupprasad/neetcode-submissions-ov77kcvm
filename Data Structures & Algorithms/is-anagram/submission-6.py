class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        for i in t:
            if i in hashmap:
                hashmap[i]-=1
            else:
                return False
        count = 0
        print(hashmap)
        for k in hashmap.keys():
            if hashmap[k] != 0:
                return False

        return True