from sys import stdin
from collections import deque

def main():
    conta = 1
    n = int(stdin.readline())
    while n != 0:
        print("Scenario","#"+str(conta))
        nteam = [0] * 1000000 # 0...999999
        for i in range(n):
            m = list(map(int,stdin.readline().split()))
            for j in m[1:]:
                nteam[j] = i
        cola = deque()
        teams = []
        for i in range(n):
            teams.append(deque())
        com = list(stdin.readline().split())
        while com[0] != "STOP":
             if com[0] == "ENQUEUE":
                 x = int(com[1])
                 team = nteam[x] # revision a que equipo pertenece
                 if teams[team]:
                     teams[team].append(x)
                 else:
                     teams[team].append(x)
                     cola.append(teams[team])
             else:
                 t = cola.popleft()
                 print(t.popleft())
                 if t:
                     cola.appendleft(t)
             com = list(stdin.readline().split())
        conta+=1
        n = int(stdin.readline())
        print()
          
main()      