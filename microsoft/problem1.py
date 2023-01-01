
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
        