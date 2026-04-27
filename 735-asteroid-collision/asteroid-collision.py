class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for num in asteroids:
            flag=False
            if stack and num<0 and stack[-1]>0:
                while stack and num<0 and stack[-1]>0:
                    if abs(num)<stack[-1]:
                        break
                    elif stack[-1]<abs(num):
                        stack.pop()
                    else:
                        stack.pop()
                        flag=True
                        break
                if flag==True:
                    continue
                if not stack or stack[-1]<0:
                    stack.append(num)
            else:
                stack.append(num)
        return stack