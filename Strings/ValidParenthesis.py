def isValid(s: str) -> bool:
        stack = []
        
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ')' and stack[-1] != '(':
                    return False
                if char == ']' and stack[-1] != '[':
                    return False
                if char == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        
        if len(stack) != 0:
            return False
        return True
    
string = "{}()[]{()}"
print(f"isValidParenthesis: {isValid(string)}")