class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        v=""
        for word in words:
            v+=word
            if v==s:
                return True
            if len(v)>=len(s):
                return False
        return False            

