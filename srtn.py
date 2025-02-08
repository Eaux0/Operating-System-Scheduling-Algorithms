# table=[[1,0,10],[2,1,6],[3,3,2],[4,5,4]]

def SRTN(table):
    from tabulate import tabulate
    n=len(table)

    def csort(x):
        return x[1]
    table.sort(key=csort)
    time=0
    process={}
    res={}
    timestamp=[]

    while table or process:
        while table and time>=table[0][1]:
            new_process=table.pop(0)
            process[new_process[0]]=new_process[2]
            res[new_process[0]]=[new_process[1],new_process[2]]
        if not process:
            new_process=table.pop(0)
            process[new_process[0]]=new_process[2]
            time=new_process[1]
            res[new_process[0]]=[new_process[1],new_process[2]]
        id=-1
        min_time_remaining=10**5
        for i in process:
            if process[i]<min_time_remaining:
                min_time_remaining=process[i]
                id=i
                
        if process[id]==1:
            process[id]=0
            timestamp.append(id)
            res[id].append(time+1)
            process.pop(id)
        else:
            timestamp.append(id)
            process[id]-=1
        time+=1

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

    return timestamp