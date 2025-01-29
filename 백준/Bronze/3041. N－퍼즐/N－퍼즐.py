goal = {
    'A': (0,0), 'B': (0,1), 'C': (0,2), 'D': (0,3),
    'E': (1,0), 'F': (1,1), 'G': (1,2), 'H': (1,3),
    'I': (2,0), 'J': (2,1), 'K': (2,2), 'L': (2,3),
    'M': (3,0), 'N': (3,1), 'O': (3,2)
}
total = 0
for r in range(4):
    line = input()
    for c, ch in enumerate(line):
        if ch == '.':
            continue
        goal_r, goal_c = goal[ch]
        total += abs(r - goal_r) + abs(c - goal_c)
print(total)
