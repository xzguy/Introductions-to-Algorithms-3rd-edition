class LCS:
    # input sequences
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']

    def LCS_LENGTH(self, X: [], Y: []) -> []:
        m = len(X) + 1
        n = len(Y) + 1
        b = [[0] * n for _ in range(m)]
        c = [[0] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if X[i-1] == Y[j-1]:
                    c[i][j] = c[i-1][j-1] + 1
                    b[i][j] = "match"
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = "X"
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = "Y"
        return c, b

    def PRINT_LCS(self, b: [[str]], X: [], i: int, j: int) -> None:
        if i == 0 or j == 0:
            return
        if b[i][j] == "match":
            self.PRINT_LCS(b, X, i-1, j-1)
            print(X[i-1], end="")
        elif b[i][j] == "X":
            self.PRINT_LCS(b, X, i-1, j)
        else:
            self.PRINT_LCS(b, X, i, j-1)

sol = LCS()
c, b = sol.LCS_LENGTH(sol.X, sol.Y)
print("The length of the longest common subsequence is", c[-1][-1])
sol.PRINT_LCS(b, sol.X, len(sol.X), len(sol.Y))
print("")
print("The other possible LCS is 'BDAB'.")

'''
Exercises:
15.4-1, 15.4-2, 15.4-3, 15.4-4, 15.4-5, 15.4-6
'''
# Exercise: 15.4-1
X = [1,0,0,1,0,1,0,1]
Y = [0,1,0,1,1,0,1,1,0]
# X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
# Y = ['B', 'D', 'C', 'A', 'B', 'A']
c, b = sol.LCS_LENGTH(X, Y)
print("Exercise 15.4-1:")
print("The length of the longest common subsequence is", c[-1][-1])
sol.PRINT_LCS(b, X, len(X), len(Y))
print("")
print("The other two possible LCS is '101010' and '010101'.")

# Exercise: 15.4-2
def PRINT_LCS_with_table_c(c: [[]], X, Y, i: int, j: int) -> None:
    if c[i][j] == 0:
        return
    if X[i-1] == Y[j-1]:
        PRINT_LCS_with_table_c(c, X, Y, i-1, j-1)
        print(X[i-1], end="")
    elif c[i-1][j] >= c[i][j-1]:
        PRINT_LCS_with_table_c(c, X, Y, i-1, j)
    else:
        PRINT_LCS_with_table_c(c, X, Y, i, j-1)

print("Exercise 15.4-2:")
PRINT_LCS_with_table_c(c, X, Y, len(X), len(Y))
print("")

# Exercise: 15.4-3
def LCS_LENGTH_MEMO(X: [], Y: []) -> int:
    
    def LCS_LENGTH_AUX(i: int, j: int, memo: dict) -> int:
        if i < 0 or j < 0:
            return 0
        if (i, j) not in memo: 
            res = 0
            if X[i] == Y[j]:
                res = 1 + LCS_LENGTH_AUX(i-1, j-1, memo)
            else:
                res = max(LCS_LENGTH_AUX(i-1, j, memo), LCS_LENGTH_AUX(i, j-1, memo))
            memo[i, j] = res
        return memo[i, j]
    
    return LCS_LENGTH_AUX(len(X)-1, len(Y)-1, {})

print("Exercise 15.4-3:")
print(LCS_LENGTH_MEMO(X, Y))

# Exercise: 15.4-4
def LCS_LENGTH_LESS_SPACE(X: [], Y: []) -> int:
    m = len(X)
    n = len(Y)
    # makes n <= m
    if n > m:
        X, Y = Y, X
        m, n = n, m

    # the upper row in the c table
    up = [0] * n

    for i in range(m):
        left = left_up = 0
        for j in range(n):
            if X[i] == Y[j]:
                cur = left_up + 1
            elif up[j] >= left:
                cur = up[j]
            else:
                cur = left
            left, left_up, up[j] = cur, up[j], cur
    return cur

print("Exercise 15.4-4:")
print(LCS_LENGTH_LESS_SPACE(X, Y))

# Exercise: 15.4-5
# return the longest monotonically increasing subsequence
# of a sequence of n numbers.
def MONO_INC_LCS_LENGTH(arr: [int]) -> None:
    sorted_arr = sorted(arr)
    c, b = sol.LCS_LENGTH(arr, sorted_arr)
    sol.PRINT_LCS(b, arr, len(arr), len(arr))
    print("")

arr = [3,1,2,4,5,4,9]
print("Exercise 15.4-5:")
MONO_INC_LCS_LENGTH(arr)

# Exercise: 15.4-6
import bisect
# array B: B[i-1] contains the last value of
# a longest monotonically increasing subsequence of length i.
# array C: C[i-1] contains the monotonically increasing
# subsequence of length i with smallest last element seen so far
def MONO_INC_LCS_LENGTH_FASTER(arr: [int]) -> None:
    n = len(arr)
    B = [float('inf')] * n
    C = [0] * n
    L = 1
    for i in range(n):
        if arr[i] < B[0]:
            B[0] = arr[i]
            C[0] = [arr[i]]
        else:
            j = bisect.bisect_left(B, arr[i], lo=0, hi=i+1)

            # only strictly increasing
            if B[j] == arr[i]:
                continue
            
            B[j] = arr[i]
            C[j] = C[j-1].copy()
            C[j].append(arr[i])
            if j+1 > L:
                L += 1
    print(C[L-1])

arr = [2,0,20,3,2,0,6,32,3]
print("Exercise 15.4-6:")
MONO_INC_LCS_LENGTH_FASTER(arr)