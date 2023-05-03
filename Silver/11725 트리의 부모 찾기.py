'''
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''

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