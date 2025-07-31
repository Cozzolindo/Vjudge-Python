from sys import stdin

def main():
    
    street = [0]*501
    t = int(input())
    for T in range(t):
        
        street = list(map(int,stdin.readline().split()))
        n = street.pop(0)
        
        for i in range(0,n):
            for j in range(i+1,n):
                if(street[i]>street[j]):
                    
                    temp = street[i]
                    street[i] = street[j]
                    street[j] = temp
        M = int((n/2)+1)
        
        sum = 0
        
        times = 1
        for c in range(1,M):
            sum+= times*abs(street[c] - street[c-1])
            times+=1
        times = 1
        for c in range(n-1, M-1, -1):
            sum+= times*abs(street[c] - street[c-1])
            times+=1    
        print(sum)
        
        
main()