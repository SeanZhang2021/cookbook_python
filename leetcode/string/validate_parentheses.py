#!/usr/bin/python3

class Solution:
    def test(s: str) -> bool:
        if len(s) == 0:
            # python的Ture是True，False是False
            return True
        stack = []
        for i in s:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
                print(stack)
            elif (i == "]" and len(stack) > 0 and stack[len(stack) - 1]== "[") or (i == ")" and len(stack) > 0 and stack[len(stack) - 1]== "(") or (i == "}" and len(stack) > 0 and stack[len(stack) - 1] == "{"):
                stack.pop()
            else:
                return False
                # 一般栈空为退出条件
        return len(stack)==0

if __name__ == "__main__":
    print(Solution.test("({{}})"))
