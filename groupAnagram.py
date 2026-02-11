# brute force

class Solution1:
    def groupAnagarm(self,strs:list[str])->list[str]:
        result=[]
        visited=[False]* len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue

        group=[strs[i]]
        visited[i]=True


        for j in range(i+1,len(strs)):
            if not visited[j] and sorted(strs[i])==sorted(strs[j]):
                group.append(strs[j])
                visited[j]=True
            result.append(group)

        return result




# brute force 2 
class Solution3:
    def groupAnagram(self, strs:list[str])->list[list[str]]:
        groups= {}
        for word in strs:
            key =tuple(sorted(word))
            if key in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())
            
    
# neetcode solution

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # hashmap mapping count tuple -> list of anagrams

        for s in strs:
            count = [0] * 26  # a to z

            for c in s:
                count[ord(c) - ord('a')] += 1  # count each character

            res[tuple(count)].append(s)  # list can't be key, so convert to tuple

        return list(res.values())
