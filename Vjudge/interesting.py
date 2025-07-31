#INTERESTING DRINK QUESTION

from sys import stdin

def binSearch(low, high, key, array):
    while(low<high):
        mid = int((low+high)/2)
        if(array[mid]<=key):
            low = mid+1
        else:
            high = mid
    return low

def main():
    bars = int(input())
    prices = list(map(int,stdin.readline().split()))
    days = int(input())
    prices.sort()
    
    while(days>0):
        coins = (int(input()))
        print(binSearch(0,bars, coins, prices))
        days-=1

main()