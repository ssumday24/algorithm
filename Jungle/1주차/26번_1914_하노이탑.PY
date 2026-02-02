#1914: 하노이탑 (재귀)

def hanoi(n,from_pos,to_pos,aux_pos): # N개 , 출발지 , 도착지, 경유지
    if n==1:
        
        print(f'{from_pos} {to_pos}')
        return

    #원반 N-1개를 경유지로 이동
    hanoi(n-1,from_pos,aux_pos,to_pos)
    
    # 가장 큰 원반을 목적지로 이동
    
    print(from_pos,to_pos)
    
    # N-1개를 경유지-> 목적지로  이동 (from_pos 거쳐서)
    hanoi(n-1,aux_pos,to_pos,from_pos) 
    
N=int(input())

print(2**N -1)
if N<=20:
    hanoi(N,1,3,2)
