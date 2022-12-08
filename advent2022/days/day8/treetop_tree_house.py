def is_tree_visible(tree, neighbor):
    return tree <= neighbor


forest = [[int(i) for i in line] for line in open('trees.txt').read().splitlines()]

scenic_score = 0
inner_trees = 0
edges_count = (2 * len(forest)) + (2 * (len(forest[0]) - 2))

for i in range(1, len(forest) - 1):
    for j in range(1, len(forest) - 1):
        tree = forest[i][j]
        left, right, up, down = j, j, i, i
        up_score, down_score, left_score, right_score = 0, 0, 0, 0
        left_visible, right_visible, up_visible, down_visible = True, True, True, True
        # Up
        while up > 0:
            up_score += 1
            if is_tree_visible(tree, forest[up-1][j]):
                up_visible = False
                break
            up -= 1
        # Down
        while down < len(forest) - 1:
            down_score += 1
            if is_tree_visible(tree, forest[down+1][j]):
                down_visible = False
                break
            down += 1
        # Left
        while left > 0:
            left_score += 1
            if is_tree_visible(tree, forest[i][left-1]):
                left_visible = False
                break
            left -= 1
        # Right
        while right < len(forest) - 1:
            right_score += 1
            if is_tree_visible(tree, forest[i][right+1]):
                right_visible = False
                break
            right += 1

        if up_visible or down_visible or left_visible or right_visible:
            score = (up_score * down_score * left_score * right_score)
            if score > scenic_score:
                scenic_score = score
            inner_trees += 1

print(inner_trees + edges_count)
print(scenic_score)
