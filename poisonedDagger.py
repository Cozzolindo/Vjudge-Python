from sys import stdin


def check(health, atk, procs, key):
    
    for i in range (1,atk):
        health-=min(key,procs[i]-procs[i-1])

        if(health<=0):
            return True

    health-=key
    return health<=0
    

def damage(health, atk, procs):
    low = 1
    high = health
    
    while(low<=high):
        
        mid = int((high+low)/2)
        
        if(check(health, atk, procs, mid)):
            high = mid-1
        else:
            low = mid+1
        
    
    return low

def main():
    
    tests = int(input())
    for i in range(0,tests):
        inputa = list(map(int,stdin.readline().split()))
        procs = list(map(int,stdin.readline().split()))
        
        print(damage(inputa[1],inputa[0],procs))

main()