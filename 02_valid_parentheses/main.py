class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parentheses_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        
        if len(s) <= 1:
            return False
        
        for i in s:
            # if i == open bracket push to stack
            if i in parentheses_dict.values():
                stack.append(i)
            # if i == close bracket -> last elmt should equal i else return false. make sure the stack is not empty
            elif i in parentheses_dict.keys() and len(stack) > 0:
                if parentheses_dict.get(i) == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0
    
if __name__ == "__main__":
    solution = Solution()
    s_input = "){"
    print(solution.isValid(s_input))