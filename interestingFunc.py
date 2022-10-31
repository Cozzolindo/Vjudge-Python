from sys import stdin

def main():
    tests = int(input())
    for i in range(tests):
        inputa = list(map(int,stdin.readline().split()))
        l =inputa[0]
        n = inputa[1]
        digits = 0
        k=10
        for i in range(l,n,k):
            k*=10
            digits = (digits+(n-i+1))
        print(digits)
        

main()