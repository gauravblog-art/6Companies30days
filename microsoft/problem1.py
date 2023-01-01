
# 150. Evaluate Reverse Polish Notation
def evalRPN(self, tokens: List[str]) -> int:    
    stack=[]
    for i in range(len(tokens)):
        if tokens[i]=="+":
            first=stack.pop()
            secound=stack.pop()
            stack.append(first+secound)
        elif tokens[i]=="-":
            first=stack.pop()
            secound=stack.pop()
            stack.append(secound-first)
        elif tokens[i]=="*":
            first=stack.pop()
            secound=stack.pop()
            stack.append(first*secound)
        elif tokens[i]=="/":
            first=stack.pop()
            secound=stack.pop()
            stack.append(int(secound/first))
        else:
            stack.append(int(tokens[i]))
    return stack[0]
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
        