import random, copy


A1={'1':['8', '5', '6'], '2':['6','7', '9'], '3':['7', '10', '5'], '4':['8','10', '9'], '9':['4','5', '2'], '10':['3', '4', '6'], '5':['1', '9', '3'], '6':['1', '2', '10'], '7':['8', '2', '3'], '8':['7', '1', '4']}

def BFS(graf1, s):
    color,d,p={},{},{}
    for u in graf1:
       color[u],d[u],p[u]="white","inf",None
    color[s],d[s],p[s]="gray",0,None
    Q=[]
    Q.append(s)
    while Q!= []:
        u=Q.pop(0)
        for v in graf1[u]:
            #print v
            if color[v]=="white":
               color[v],d[v],p[v]="gray",d[u]+1,u
               Q.append(v)
        color[u]="black"
    return (p,d)

print BFS(A1,'1')
