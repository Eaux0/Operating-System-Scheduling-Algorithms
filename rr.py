# table=[[1,0,5],[2,1,3],[3,2,1],[4,3,2],[5,4,3]]
    
def RR(table):
    from tabulate import tabulate
    n=len(table)
    def csort(x):
        return x[1]
    table.sort(key=csort)
    time=0
    timestamp=[]
    tq=int(input("Enter Time Quantum: "))
    res={}
    process={}
    prev=-1

    def get_id(prev,process):
        if len(process)==1:
            for i in process:
                return i
        curr=-1
        wt=-1
        for i in process:
            if i==prev:
                continue
            elif wt==process[i][0]:
                if process[curr][1]>process[i][1]:
                    curr=i
            elif wt<process[i][0]:
                wt=process[i][0]
                curr=i
        return curr

    while table or process:
        newly_added=[]
        while table and time>=table[0][1]:
            new_pr=table.pop(0)
            process[new_pr[0]]=[0,0,new_pr[2],new_pr[1]]
            newly_added.append(new_pr[0])
        if not process:
            new_pr=table.pop(0)
            process[new_pr[0]]=[0,0,new_pr[2],new_pr[1]]
            time=new_pr[1]
            newly_added.append(new_pr[0])
            timestamp.extend([-1 for _ in range(new_pr[1]-len(timestamp))])

        id=get_id(prev,process)
        
        if process[id][2]-process[id][1]<=tq:
            te=process[id][2]-process[id][1]
            res[id]=[process[id][3],process[id][2],time+te]
            process.pop(id)
        else:
            process[id][1]+=tq
            te=tq
        
        timestamp.extend([id for k in range(te)])
        time+=te

        for i in process:
            if i==id:
                process[i][0]=0
            elif i in newly_added:
                process[i][0]=time-process[i][3]
            else:
                process[i][0]+=te
        prev=id
    
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

# ts=RR([[1,0,2],[2,5,1],[3,8,2]])
# print(ts)