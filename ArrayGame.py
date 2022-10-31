from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline())
    inputa = list(map(int,stdin.readline().split()))
    game = deque()
    ma = []
    rounds = 0
    
    for i in range(0,n):
        game.append(inputa[i])
    
    for i in range(0,n):
        rounds+= 1
        print(i)
        if i == 0:
            if (game[0] >= game[len(game)-1]):
                ma.append(game.popleft())
            else:
                ma.append(game.pop())
        elif i>0:
            if((ma[i-1]< game[0]) and (ma[i-1]<game[len(game)-1])):
                break
            elif ((game[0] >= game[len(game)-1]) and (game[0] < ma[i-1])):
                ma.append(game.popleft())
            elif ((game[len(game)-1] > game[0]) and (game[len(game)-1] < ma[i-1])):
                ma.append(game.pop())
            else:
                break
        print(ma)
        print(game)
        
    if(rounds%2==0):
        print('Bob')
    else:
        print('Alice')
main()      