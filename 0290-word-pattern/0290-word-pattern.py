class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mapping={}
        used=set()
        words=s.split()
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]]!=words[i]:
                    return False
            else:
                if words[i] in used:
                    return False
                mapping[pattern[i]]=words[i]
                used.add(words[i])
        return True