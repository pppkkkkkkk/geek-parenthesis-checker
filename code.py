class Solution:
    def isBalanced(self, s):
        # code here
        
        # Return True if Match, char1 is open bracket and is close
        def adp(char1, char2):
            if char1 == "(":
                return char2 == ")"
            elif char1 == "[":
                return char2 == "]"
            elif char1 == "{":
                return char2 == "}"
            else:
                return False
                
        stack = []
        
        for char in s:
            if char in ("(","[","{"):
                stack.append(char)
            elif char in (")","]","}"):
                if not stack:
                    return False
                tmp = stack.pop()
                if not adp(tmp, char):
                    return False
        
        if not stack:
            return True
        
        return False
        