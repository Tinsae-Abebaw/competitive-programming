class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dic={"+":"+","*":"+","-":"+","/":"/"}
        stack=[]
        a=0
        for i in range(0,len(tokens)):
            if len(tokens)==1:
                a=int(tokens[i])
                break
            elif tokens[i] not in dic:
                stack.append(int(tokens[i]))
            else:
                if tokens[i]=="+":
                    a=stack[-1]+stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                if tokens[i]=="-":
                    a=stack[-2]-stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                if tokens[i]=="*":
                    a=stack[-1]*stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                if tokens[i]=="/":
                    a=int(stack[-2]/(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack.append(a)
        return a

        