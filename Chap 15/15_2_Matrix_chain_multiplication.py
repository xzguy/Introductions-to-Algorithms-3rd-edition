class Matrix_chain_multiplication:
    def MATRIX_CHAIN_ORDER(self, p: [int]):
        n = len(p) - 1
        m = [[0] * n for _ in range(n)]
        s = [[0] * n for _ in range(n)]
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                m[i][j] = float('inf')
                for k in range(i, j):
                    q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k
        return m, s

    def PRINT_OPTIMAL_PARENS(self, s:[[int]], i: int, j: int):
        if i == j:
            print("A"+str(i+1), end='')
        else:
            print("(", end='')
            self.PRINT_OPTIMAL_PARENS(s, i, s[i][j])
            self.PRINT_OPTIMAL_PARENS(s, s[i][j]+1, j)
            print(")", end='')

'''
A1 = 30 X 35
A2 = 35 X 15
A3 = 15 X 5
A4 = 5 X 10
A5 = 10 X 20
A6 = 20 X 25
'''
p = [30, 35, 15, 5, 10, 20, 25]
sol = Matrix_chain_multiplication()
m, s = sol.MATRIX_CHAIN_ORDER(p)
print("The minimum number of operations is", m[0][-1])
sol.PRINT_OPTIMAL_PARENS(s, 0, len(p)-2)
print("")

'''
Exercises:
15.2-1, 15.2-2
'''
print("Exercise 15.2-1:")
p = [5, 10, 3, 12, 5, 50, 6]
m, s = sol.MATRIX_CHAIN_ORDER(p)
print("The minimum number of operations is", m[0][-1])
sol.PRINT_OPTIMAL_PARENS(s, 0, len(p)-2)
print("")

print("Exercise 15.2-2:")

import numpy as np
import time
def generate_matrics(p: [int]):
    matrics = []
    for i in range(len(p)-1):
        matrics.append(np.random.randint(0, high=101, size=(p[i], p[i+1])))
    return matrics

# for naive orderly multiplication, the order from left to right, or reverse matters
# here we use the order from left to right, multiply one by one
def MATRIX_CHAIN_MULTIPLY_naive(A):
    res = A[0]
    for i in range(1, len(A)):
        res = np.matmul(res, A[i])
    return res

def MAT_CHAIN_MUL_naive_num_of_ope(p: [int]) -> int:
    res = 0
    x = p[0]
    for i in range(1, len(p)-1):
        res += x * p[i] * p[i+1]
    return res

p = [50, 5, 100, 10]
p = [5, 10, 3, 15, 5, 50, 3]
m, s = sol.MATRIX_CHAIN_ORDER(p)
print("The minimum number of operations is", m[0][-1])
print("The number of operations for naive multiplication is", MAT_CHAIN_MUL_naive_num_of_ope(p))
print("The naive method is " + str(MAT_CHAIN_MUL_naive_num_of_ope(p)/m[0][-1]) + " times more operations over dp.")
sol.PRINT_OPTIMAL_PARENS(s, 0, len(p)-2)
print("")
A = generate_matrics(p)

def MATRIX_CHAIN_MULTIPLY(A, s, i, j):
    if i == j:
        return A[i]
    else:
        x1 = MATRIX_CHAIN_MULTIPLY(A, s, i, s[i][j])
        x2 = MATRIX_CHAIN_MULTIPLY(A, s, s[i][j]+1, j)
        return np.matmul(x1, x2)

start_time = time.time()
prod1 = MATRIX_CHAIN_MULTIPLY(A, s, 0, len(p)-2)
print("Time for dp in milliseconds is", 10**3 * (time.time() - start_time))

start_time = time.time()
prod2 = MATRIX_CHAIN_MULTIPLY_naive(A)
print("Time for naive in milliseconds is", 10**3 * (time.time() - start_time))

if np.array_equal(prod1, prod2):
    print("Two methods match.")