# Last updated: 22/06/2026, 11:49:36
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False;
5
6        charObject ={}
7        totalMatch = 0
8
9        for singleChar in s:
10            if singleChar not in charObject:
11                charObject[singleChar] = 0
12            charObject[singleChar] = charObject[singleChar] + 1
13
14        for singleChar in t:
15            if singleChar in charObject and charObject[singleChar] > 0:
16                totalMatch = totalMatch + 1
17                charObject[singleChar] = charObject[singleChar] -1
18
19        if totalMatch == len(s):
20            return True
21
22        return False   
23        