class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        nums = []
        
        for e in tokens:
            if e not in ['+', '-', '*', '/']:
                nums.append(int(e))

            elif e == '+':
                mid_res = nums.pop() + nums.pop()
                nums.append(mid_res)

            elif e == '-':
                num2 = nums.pop()
                num1 = nums.pop()
                mid_res = num1- num2
                nums.append(mid_res)

            elif e == '*':
                mid_res = nums.pop() * nums.pop()
                nums.append(mid_res)

            elif e == '/':
                num2 = nums.pop()
                num1 = nums.pop()
                mid_res = int(num1 / num2)
                nums.append(mid_res)
        
        return nums.pop()