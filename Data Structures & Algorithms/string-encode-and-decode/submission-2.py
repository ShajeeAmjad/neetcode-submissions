class Solution:

    def encode(self, strs: List[str]) -> str:

        new_str = ""
        for word in strs:
            new_str += f"{len(word)}#{word}"
        return new_str


    def decode(self, s: str) -> List[str]:

        new_strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            new_strs.append(word)
            i = j + 1 + length
        return new_strs