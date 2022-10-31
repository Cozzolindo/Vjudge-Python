from sys import stdin

def BNW(n,k,let):
    
    #let = list(let)
    count = [0]*(n+1)
    
    for i in range(1,n+1):
        count[i]=count[i-1]
        if(let[i-1] =='B'):
            count[i]+=1

    stripe = k
    for i in range(k,n+1):
        stripe = min(stripe, k-(count[i]-count[i-k]))
    return int(stripe)
        
def main():
    tests = int(input())
    

    for i in range(0,tests):
        inputs = list(map(int,stdin.readline().split()))
        let = str(input())
        print(BNW(inputs[0],inputs[1],let))
        

main()