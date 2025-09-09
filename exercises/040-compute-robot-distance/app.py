# Your code here
def compute_robot_distance(n):
    x = 0
    y = 0
    for i in n:
        sep = i.split(' ')
        if sep[0] == 'UP':
            x += int(sep[1])
        elif sep[0] == 'DOWN':
            x -= int(sep[1])
        elif sep[0] == 'RIGHT':
            y += int(sep[1])
        elif sep[0] == 'LEFT':
            y -= int(sep[1])
    return(x, y)

print(compute_robot_distance(["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]))