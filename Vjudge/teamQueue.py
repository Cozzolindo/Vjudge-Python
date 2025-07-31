import heapq

import sys




        
def main():
    inp = int(sys.stdin.readline())
    scen = 1
    while(inp!=0):
        print("Scenario"+" "+"#"+str(scen))
        
        for i in range(inp):
            values = list(sys.stdin.readline().split())
            
        att = []
        heapq.heapify(att)
        value = list(sys.stdin.readline().split())
        while(value[0]!="STOP"):
            if(value[0] == "ENQUEUE"):
                heapq.heappush(att,value[1])
                
                
            else:
                
                print(heapq.heappop(att))
            value = list(sys.stdin.readline().split())
            
        print()
        inp = int(sys.stdin.readline())
        scen += 1
main()