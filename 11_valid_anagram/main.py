# sorting
from collections import defaultdict


class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)
    
# hashtable frequency
class Solution1:
    def isAnagram(self, s:str, t:str) -> bool:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        
        for j in t:
            count[j] -= 1
        
        for x in count.values():
            if x != 0:
                return False
        
        return True


    
if __name__ == "__main__":
    # measure running time

    import timeit
    import random
    input_list = [random.randint(0, 1000) for _ in range(1000)]
    sol = Solution()
    sol1 = Solution1()
    t1 = timeit.Timer(lambda: sol.isAnagram("anagram", "nagaram"))
    t2 = timeit.Timer(lambda: sol1.isAnagram("anagram", "nagaram"))
    print(t1.timeit(1000000))

    print(t2.timeit(1000000))

