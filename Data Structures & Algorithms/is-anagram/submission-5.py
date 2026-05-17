class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # optimal solution
        hash_map_s = {}
        hash_map_t = {}

        for char in s:
            if hash_map_s.get(char):
                hash_map_s[char] += 1
            else:
                hash_map_s[char] = 1
         
        for char in t:
            if hash_map_t.get(char):
                hash_map_t[char] += 1
            else:
                hash_map_t[char] = 1

        return True if hash_map_t == hash_map_s else False