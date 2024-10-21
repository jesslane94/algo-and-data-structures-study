#usually used in combinatorial search problems -> finding permutations/subsets, solving sudoku, 8-queens

# 1. ID the state(s)
# 2. draw the state space tree.
# 3. DFS/backtrack on the state-space tree

# TEMPLATE 
""" def dfs(node, state):
    if state is a solution:
        report(state) # e.g. add state to final result list
        return

    for child in children:
        if child is a part of a potential solution:
            state.add(child) # make move
            dfs(child, state)
            state.remove(child) # backtrack """


def permutations(l):
    def dfs(path, used, res):
        if len(path) == len(l):
            res.append(path[:]) # note [:] make a deep copy since otherwise we'd be append the same list over and over
            return

        for i, letter in enumerate(l):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    res = []
    dfs([], [False] * len(l), res)
    return res
    
# Driver code
inputs = ["ab", "abc"]
for i in range(len(inputs)):
    print("Permutations :",permutations(inputs[i]))

