# Stack Parentheses Balanced ( Interview Question)
# Instructions
# Check to see if a string of parentheses is balanced or not.

# By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

# Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.

# Function name:
# is_balanced_parentheses

def is_balanced_parentheses(string):
    stack = []
    
    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
