count = 0
def tryp(sum, goal):
    if sum == goal:
        global count
        count += 1
        return
    if sum > goal:
        return
    if sum <= goal-3:
        tryp(sum+3, goal)
    if sum <= goal-2:
        tryp(sum+2, goal)
    if sum <= goal-1:
        tryp(sum+1, goal)
n = int(input())
tryp(0, n)
print(count)