def CSOD(n):
    res = 0
    i = 2
    while(i*i<=n):
        j = (n//i)
        res+=((i+j)*(j-i+1))//2
        res+=i*(j-i)
        i+=1
    return int(res)

def main():
    num = 1
    case = 0
    while(num!=0):
        num = int(input())
        if(num==0):
            break
        else:
            
            case += 1
            res = (CSOD(num))
            print(f"Case {case}: {res}")
        
main()
