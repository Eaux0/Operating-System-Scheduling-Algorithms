# table=[(1,1,7),(2,3,3),(3,6,2),(4,7,10),(5,9,8)]

def SJF(table):
    from tabulate import tabulate
    import heapq

    ts=[]
    res={}
    for i,j,k in table:
        res[i]=[j,k]
    n=len(table)

    def csort(x):
        return x[1]

    table.sort(key=csort)
    process,time=[],table[0][1]
    timestamp={}

    while process or table:
        while (table and time>=table[0][1]) or not process:
            heapq.heappush(process,(table[0][2],table[0][1],table[0][0]))
            table.pop(0)
        curr=heapq.heappop(process)
        if len(ts)<curr[1]:
            for _ in range(curr[1]-len(ts)):
                ts.append(-1)
        timestamp[curr[2]]=[(time,time+curr[0])]
        ts.extend([curr[2] for k in range(curr[0])])
        time+=curr[0]
        res[curr[2]].append(time)

    grid=[]
    head=['ID','Arival Time','Burst Time', 'Finish Time', 'Turn Around Time', 'Waiting Time']
    total_tat,total_wt=0,0
    for i in range(1,n+1):
        pid=i
        at,st,ft=res[i]
        tat=ft-at
        wt=tat-st
        total_tat+=tat
        total_wt+=wt
        grid.append([pid,at,st,ft,tat,wt])
        
    print(tabulate(grid, headers=head, tablefmt="grid"))

    print()
    print("Avg TAT: ",total_tat/n)
    print("Avg WT: ",total_wt/n)
    
    return ts
