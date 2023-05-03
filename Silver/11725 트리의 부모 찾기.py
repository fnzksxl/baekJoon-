import sys
from collections import deque

def bfs(start):
    q=deque()
    for node in graph[start]:
        q.append(node)
    parents[1]=1

    while q:
        node=q.popleft()
        if not parents[node[1]]:
            parents[node[1]]=node[0]
            for next in graph[node[1]]:
                q.append(next)

n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
parents=[0 for _ in range(n+1)]
# n = 노드의 개수

for _ in range(n-1):
    node1,node2=map(int,sys.stdin.readline().split())
    graph[node1].append((node1,node2))
    graph[node2].append((node2,node1))

bfs(1)

for i in range(2,n+1):
    print(parents[i])