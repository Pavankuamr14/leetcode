class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-97]+=1
            key = tuple(count)
            if key in hash:
                hash[key].append(i)
            else:
                hash[key]=[i]
        
        return list(hash.values())

        
