class rod_cutting:
    # for index n, the number is the price of rob of length of n + 1
    rod_price_table = [1,5,8,9,10,17,17,20,24,30]

    # for index n, the number is the maximum price of cutting rob of length of n + 1
    test_case = [1,5,8,10,13,17,18,22,25,30]

    # recursive
    def CUT_ROD(self, p: [int], n: int) -> int:
        if n == 0:
            return 0
        q = float('-inf')
        for i in range(1,n+1):
            q = max(q, p[i-1] + self.CUT_ROD(p, n-i))
        return q

    # memo, top-down method
    # python-style implementation
    def MEMOIZED_CUT_ROD(self, p: [int], n: int) -> int:

        def MEMOIZED_CUT_ROD_AUX(n: int, memo: dict):
            if n not in memo:
                if n == 0:
                    memo[n] = 0
                else:
                    q = float('-inf')
                    for i in range(1,n+1):
                        q = max(q, p[i-1] + MEMOIZED_CUT_ROD_AUX(n-i, memo))
                    memo[n] = q
            return memo[n]
    
        return MEMOIZED_CUT_ROD_AUX(n, {})

    # dp, bottom-up method
    # python-style implementation
    def BOTTOM_UP_CUT_ROD(self, p: [int], n: int) -> int:
        memo = {}
        memo[0] = 0
        for j in range(1, n+1):
            q = float('-inf')
            for i in range(1, j+1):
                q = max(q, p[i-1] + memo[j-i])
            memo[j] = q
        return memo[n]

    # dp, bottom-up method, with first cutting length
    def EXTENDED_BOTTOM_UP_CUT_ROD(self, p: [int], n: int) -> []:
        memo = {}
        s = {}
        memo[0] = 0
        for j in range(1, n+1):
            q = float('-inf')
            for i in range(1, j+1):
                if p[i-1] + memo[j-i] > q:
                    q = p[i-1] + memo[j-i]
                    s[j] = i
            memo[j] = q
        return memo, s

    # print result
    def PRINT_CUT_ROD_SOLUTION(self, p: [int], n: int) -> None:
        _, s = self.EXTENDED_BOTTOM_UP_CUT_ROD(p, n)
        while n > 0:
            print(s[n])
            n -= s[n]

sol = rod_cutting()
rod_len = 9
if rod_len > len(sol.rod_price_table):
    raise EnvironmentError
print("Recursive:", sol.CUT_ROD(sol.rod_price_table, rod_len))
print("Memo, top-down:", sol.MEMOIZED_CUT_ROD(sol.rod_price_table, rod_len))
print("DP, bottom-up:", sol.BOTTOM_UP_CUT_ROD(sol.rod_price_table, rod_len))
print("Print cutting lengths:")
sol.PRINT_CUT_ROD_SOLUTION(sol.rod_price_table, rod_len)
print("The corrent answer is ", sol.test_case[rod_len-1])

'''
Exercises:
15.1-3, 15.1-4, 15.1-5
'''
# Exercise: 15.1-3
# cutting rob gain is prices of robs minus cutting cost 'c' per cut
def BOTTOM_UP_CUT_ROD_with_cut_cost(p: [int], n: int, c: int) -> int:
    memo = {}
    memo[0] = 0
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            if i == j:  # no cut
                q = max(q, p[i-1] + memo[j-i])
            else:  # minus cut cost
                q = max(q, p[i-1] - c + memo[j-i])
        memo[j] = q
    return memo[n]

# simplified code of the above method
def BOTTOM_UP_CUT_ROD_with_cut_cost_simple(p: [int], n: int, c: int) -> int:
    memo = {}
    for j in range(1, n+1):
        q = p[j-1]
        for i in range(1, j):
            q = max(q, p[i-1] - c + memo[j-i])
        memo[j] = q
    return memo[n]

cut_cost = 1
print("Exercise 15.1-3:")
print(BOTTOM_UP_CUT_ROD_with_cut_cost_simple(sol.rod_price_table, rod_len, cut_cost))

# Exercise: 15.1-4
print("Exercise 15.1-4:")

def MEMOIZED_CUT_ROD_with_cutting_lengths(p: [int], n: int) -> None:
    s = {}

    def MEMOIZED_CUT_ROD_AUX(n: int, memo: dict):
        if n not in memo:
            if n == 0:
                memo[n] = 0
            else:
                q = float('-inf')
                for i in range(1,n+1):
                    if p[i-1] + MEMOIZED_CUT_ROD_AUX(n-i, memo) > q:
                        q = p[i-1] + MEMOIZED_CUT_ROD_AUX(n-i, memo)
                        s[n] = i
                memo[n] = q
        return memo[n]
    
    max_price = MEMOIZED_CUT_ROD_AUX(n, {})
    print("The maximum price is:", max_price)
    print("The corresponding cutting is:")
    while n > 0:
        print(s[n])
        n -= s[n]
    return

MEMOIZED_CUT_ROD_with_cutting_lengths(sol.rod_price_table, rod_len)

# Exercise: 15.1-5
print("Exercise 15.1-5:")
def Fibonacci(n: int) -> int:
    a,b = 1,1
    if n < 3:
        return 1
    for _ in range(n-2):
        a,b = b, a+b
    return b

n = 10
print(Fibonacci(n))