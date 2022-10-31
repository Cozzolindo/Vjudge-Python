def main():
    tests = int(input())
    
    for test in range(tests):
        n = int(input())
        solve = n*(n-1)//2 + n*(n-1)*(n-2)*(n-3)//24 + 1
        print(int(solve))
main()
