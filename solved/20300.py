N = int(input())
losses = list(map(int, input().split()))
losses.sort()

MAX = 0
if len(losses) % 2 == 1:
    MAX = losses[len(losses) - 1]
    for i in range(len(losses) // 2):
        new = losses[i] + losses[len(losses) - 2 - i]
        if MAX < new:
            MAX = new

elif len(losses) % 2 == 0:
    for i in range(len(losses) // 2):
        new = losses[i] + losses[len(losses) - 1 - i]
        if MAX < new:
            MAX = new

print(MAX)
