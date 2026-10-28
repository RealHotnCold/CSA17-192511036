# Program 14: Alpha-Beta Pruning
def alpha_beta(node, depth, alpha, beta, maximizing):
    if depth == 0 or isinstance(node, int):
        return node
    if maximizing:
        value = -float("inf")
        for child in node:
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta: break
        return value
    value = float("inf")
    for child in node:
        value = min(value, alpha_beta(child, depth-1, alpha, beta, True))
        beta = min(beta, value)
        if alpha >= beta: break
    return value
tree = [[3,5,6], [9,1,2], [0,-1,4]]
print("Game tree:", tree)
print("Best value:", alpha_beta(tree, 2, -float("inf"), float("inf"), True))
