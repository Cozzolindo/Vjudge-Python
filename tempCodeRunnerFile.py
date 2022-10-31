from math import sqrt

def main():
    num = 1
    while(num!=0):
        num = int(input())
        i = 1
        sum=0
        while(i <= sqrt(num)):
            if(num%i == 0):
                sum+=i
        print(sum-1-num)
main()
