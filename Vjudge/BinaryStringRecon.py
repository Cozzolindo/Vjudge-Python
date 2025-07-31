def BSR(s, x):
    n = len(s)
    st = ['1']*n
    
    okay = True
    for i in range(0,n):
        if(s[i] == '0'):
            if(i-x >= 0):
                st[i-x] = '0'
            elif(i+x < n):
                st[i+x] = '0'

    for i in range(0,n):
        if(s[i]== '1'):
            check = False
            if(i-x >= 0  and st[i-x] == '1'):
                check = True
            elif(i+x < n and st[i+x] == '1'):
                check = True
            elif(check == False):
                okay = False
                break

    if okay == True:
        value = ''.join(st)
                
    else:
        value = -1

    return value

def main():
    cases = int(input())
    
    for i in range(cases):
        binString = str(input())
        inte = int(input())
        print(BSR(binString, inte))
main()