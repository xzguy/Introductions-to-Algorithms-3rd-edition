class Optimal_binary_search_trees:
    # a dummy zero at the beginning of p
    p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

    def OPTIMAL_BST(self, p: [int], q: [int], n: int) -> []:
        e = [[0] * (n+1) for _ in range(n+2)]
        w = [[0] * (n+1) for _ in range(n+2)]
        root = [[0] * (n+1) for _ in range(n+1)]

        for i in range(1, n+2):
            e[i][i-1] = q[i-1]
            w[i][i-1] = q[i-1]
        
        for l in range(1, n+1):
            for i in range(1, n-l+2):
                j = i + l - 1
                e[i][j] = float('inf')
                w[i][j] = w[i][j-1] + p[j] + q[j]
                for r in range(i, j+1):
                    t = e[i][r-1] + e[r+1][j] + w[i][j]
                    if t < e[i][j]:
                        e[i][j] = t
                        root[i][j] = r
        return e, root

    def CONSTRUCT_OPTIMAL_BST(self, root: [int]) -> None:

        def sub(i, j, prev) -> None:
            if prev == 0:
                print("k"+str(root[i][j]) + " is the root")
            elif j < prev:
                if i > j:
                    print("d"+str(j) + " is the left child of k" + str(prev))
                    return
                else:
                    print("k"+str(root[i][j]) + " is the left child of k" + str(prev))
            else:
                if i > j:
                    print("d"+str(j) + " is the right child of k" + str(prev))
                    return
                else:
                    print("k"+str(root[i][j]) + " is the right child of k" + str(prev))
            sub(i, root[i][j]-1, root[i][j])
            sub(root[i][j]+1, j, root[i][j])

        n = len(root)-1
        sub(1, n, 0)

'''
Exercises:
15.5-1, 15.5-2, 15.5-4
'''
# Exercise: 15.5-1
sol = Optimal_binary_search_trees()
e, root = sol.OPTIMAL_BST(sol.p, sol.q, len(sol.p) - 1)
print("The minimum cost is", e[1][-1])
print("Exercise 15.5-1:")
sol.CONSTRUCT_OPTIMAL_BST(root)

# Exercise: 15.5-2
p = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
sol = Optimal_binary_search_trees()
e, root = sol.OPTIMAL_BST(p, q, len(p) - 1)
print("Exercise 15.5-2:")
print("The minimum cost is", e[1][-1])
sol.CONSTRUCT_OPTIMAL_BST(root)

# Exercise: 15.5-4
def OPTIMAL_BST_Knuth(p: [int], q: [int], n: int) -> []:
        e = [[0] * (n+1) for _ in range(n+2)]
        w = [[0] * (n+1) for _ in range(n+2)]
        root = [[0] * (n+1) for _ in range(n+1)]

        for i in range(1, n+2):
            e[i][i-1] = q[i-1]
            w[i][i-1] = q[i-1]
        
        for i in range(1, n+1):
            root[i][i] = i
            w[i][i] = w[i][i-1] + p[i] + q[i]
            e[i][i] = e[i][i-1] + e[i+1][i] + w[i][i]
        
        # adjust range to make sure
        # 1 <= i < j <= n
        for l in range(1, n):
            for i in range(1, n-l+1):
                j = i + l
                e[i][j] = float('inf')
                w[i][j] = w[i][j-1] + p[j] + q[j]
                for r in range(root[i][j-1], root[i+1][j]+1):
                    t = e[i][r-1] + e[r+1][j] + w[i][j]
                    if t < e[i][j]:
                        e[i][j] = t
                        root[i][j] = r
        return e, root

e, root = OPTIMAL_BST_Knuth(p, q, len(p) - 1)
print("Exercise 15.5-4:")
print("The minimum cost is", e[1][-1])
sol.CONSTRUCT_OPTIMAL_BST(root)