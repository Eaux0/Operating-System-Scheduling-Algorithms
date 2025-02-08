from ganttChart import createGanttChart
from rr import RR
from srtn import SRTN
from fcfs import FCFS
from sjf import SJF

n=int(input("Enter number of processes: "))

table=[]
for i in range(1,n+1):
    print()
    at=int(input(f"Enter the arival time for process {i}: "))
    st=int(input(f"Enter the service time for process {i}: "))

    table.append([i,at,st])

print()
print("Scheduling Algorithms: ")
print("1. First Come First Serve")
print("2. Shortest Job First")
print("3. Shortest Remaining Time Next")
print("4. Round Robin")
choice=int(input("Enter choice: "))
print()
if choice==1:
    timestamp=FCFS(table)
elif choice==2:
    timestamp=SJF(table)
elif choice==3:
    timestamp=SRTN(table)
elif choice==4:
    timestamp=RR(table)
else:
    print("Enter a value between 1 and 4.")

createGanttChart(timestamp)