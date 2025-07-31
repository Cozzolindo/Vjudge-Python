def main():
    tests = int(input())
    for i in range(tests):
        n = int(input())
        res = int(n/10)
        if(n%10==9):
            res+=1
        print(res)

main()