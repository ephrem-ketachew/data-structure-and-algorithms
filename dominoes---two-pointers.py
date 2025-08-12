# 838. Push Dominoes
# Medium
# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:

# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

# Example 1:

# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
# Example 2:


# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
 

# Constraints:

# n == dominoes.length
# 1 <= n <= 105
# dominoes[i] is either 'L', 'R', or '.'.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        
        i = 0
        while i < n:
            while i < n and dominoes[i] != 'R':
                i += 1
            if i + 1 < n and dominoes[i + 1] == '.':
                i += 1
                left = i
                while i < n and dominoes[i] == '.':
                    i += 1
                if i < n and dominoes[i] == 'L':
                    right = i - 1
                    while left < right:
                        dominoes[left] = 'R'
                        dominoes[right] = 'L'
                        left += 1
                        right -= 1
                else:
                    i -= 1

            i += 1
            
        i = 0
        while i < n:
            if dominoes[i] == 'L':
                j = i - 1
                while j >= 0 and dominoes[j] == '.':
                    j -= 1    
                if j == -1 or dominoes[j] == 'L':
                    for k in range(j + 1, i):
                        dominoes[k] = 'L'
            i += 1
            
        i = 0
        while i < n:                  
            if dominoes[i] == 'R':
                i += 1
                j = i
                while i < n and dominoes[i] == '.':
                    i += 1
                if i == n or dominoes[i] == 'R':
                    for k in range(j, i):
                        dominoes[k] = 'R'
            else:
                i += 1
                
            
        return ''.join(dominoes)
        
        # n = len(dominoes)
        # forces = [0] * n
        
        # force = 0
        # for i in range(n):
        #     if dominoes[i] == 'R':
        #         force = n
        #     elif dominoes[i] == 'L':
        #         force = 0
        #     else:
        #         force = max(0, force - 1)
        #     forces[i] += force
            
        # force = 0
        # for i in range(n - 1, -1, -1):
        #     if dominoes[i] == 'L':
        #         force = n
        #     elif dominoes[i] == 'R':
        #         force = 0
        #     else:
        #         force = max(0, force - 1)
        #     forces[i] -= force
            
        # res = []
        # for force in forces:
        #     if force > 0:
        #         res.append('R')
        #     elif force < 0:
        #         res.append('L')
        #     else:
        #         res.append('.')
                
        # return ''.join(res)

            
# solution = Solution()
# dominoes = 'R...LR.....LLL..R.L'
# dominoes = "RR.L"
# dominoes = ".L.R...LR..L.."
# dominoes = "...RL....R.L.L........RR......L....R.L.....R.L..RL....R....R......R.......................LR.R..L.R."
# print(solution.pushDominoes(dominoes))