def matched(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

# The function matched takes a string s as input and returns a boolean value indicating whether the brackets in the string are matched.
# stack = [] initializes an empty list to be used as a stack data structure.
# The for loop for char in s iterates through each character in the input string s.
# If the current character char is an open bracket (, it is pushed onto the stack using stack.append(char).
# If the current character char is a closing bracket ), the function first checks if the stack is empty using if not stack:.
# If the stack is empty, it means there is a closing bracket without a matching open bracket, so the function returns False immediately.
# Otherwise, the function pops the top of the stack using stack.pop().
# After the for loop, if the stack is not empty, it means there are open brackets without matching closing brackets, so the function returns not stack which is False.
# If the stack is empty, it means the brackets are matched, so the function returns not stack which is True.
