class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s={}
        for ch in s:
            if ch not in freq_s:
                freq_s[ch]=1
            else:
                freq_s[ch] += 1
        freq_t={}
        for j in t:
            if j not in freq_t:
                freq_t[j]=1
            else:
                freq_t[j]+=1
        if freq_s==freq_t:
            return True
        else:
            return False
        