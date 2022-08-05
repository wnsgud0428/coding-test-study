T = int(input())
votes = [[] for i in range(T)]
for i in range(T):
    for j in range(int(input())):
        votes[i].append(int(input()))

# print(votes)

for vote in votes:
    i = vote.index(max(vote))
    if vote.count(max(vote)) >= 2:
        print("no winner")
    elif vote[i] > sum(vote) - vote[i]:
        print(f"majority winner {i+1}")
    else:
        print(f"minority winner {i+1}")
