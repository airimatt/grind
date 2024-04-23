class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # answer = []

        # for i, temp in enumerate(temperatures):
        #     found = False
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temp: 
        #             answer.append(j - i)
        #             found = True
        #             break
        #     if not found: answer.append(0)

        # return answer

        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_i = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append((temp, i))
        
        return answer

