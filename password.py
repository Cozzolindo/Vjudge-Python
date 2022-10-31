from sys import stdin
from operator import itemgetter

def main():
    while True:
        try:
            word = list(stdin.readline().split())
            n = int(word.pop(0))
            senha = word[0]
            senha_dick = {}
            
            for i in range(len(senha)-n+1):
                sub = senha[i:i+n]
                
                if sub in senha_dick:
                    senha_dick[sub]+=1
                else:   
                    senha_dick[sub] = 1
            
            max_sub = max(senha_dick.items(), key=itemgetter(1))[0]
            print(max_sub)
        except(EOFError):
            break

main()