def FCFS(table):
    from tabulate import tabulate
    timestamp=[]

    n=len(table)

    import functools
    def my_cmp(x, y):
        return x[1]-y[1]
    table=sorted(table, key=functools.cmp_to_key(my_cmp))
    res,time={},0
    for id,at,st in table:
        time=max(time,at)
        timestamp.extend([-1 for k in range(max(0,time-len(timestamp)))])
        timestamp.extend([id for k in range(st)])
        res[id]=[at,st,time+st]
        time=time+st
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
    print("Avg TAT: ",total_tat/n)
    print("Avg WT: ",total_wt/n)

    return timestamp