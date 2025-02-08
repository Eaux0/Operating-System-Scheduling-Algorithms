def createGanttChart(ts):
    import random
    import matplotlib.pyplot as plt 

    ch={}
    prev=0
    l=prev

    while l<len(ts):
        curr=ts[l]
        while l<len(ts) and ts[l]==curr:
            l+=1
        if l-prev==1:
            if curr in ch:
                ch[curr].append((prev,l))
            else:
                ch[curr]=[(prev,l)]
        else:
            pr=f'{curr}'+''.join(' ' for i in range(l-1))
            if curr in ch:
                ch[curr].append((prev,l))
            else:
                ch[curr]=[(prev,l)]
        prev=l

    number_of_processes=len(ch)
    if -1 in ch:
        number_of_processes-=1

    fig, gnt = plt.subplots() 
    gnt.set_xlabel('Time') 
    gnt.set_ylabel('Process') 
    gnt.set_yticks([(12+5*i) for i in range(len(ch))]) 
    gnt.set_yticklabels([str(i) for i in range(1,len(ch)+1)]) 
    number_of_colors=len(ch)
    colours=["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_colors)]
    for i in range(1,number_of_processes+1):
        arr=[]
        for j in ch[i]:
            arr.append((j[0],j[1]-j[0]))
        gnt.broken_barh(arr, (10+5*(i-1), 4), facecolors=colours[i-1])

    plt.show()