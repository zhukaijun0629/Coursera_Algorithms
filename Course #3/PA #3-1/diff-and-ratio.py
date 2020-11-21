import copy

########Load File#########
file = open('jobs.txt')
data = file.readlines()
schedule=[]
for line in data[1:]:
    if not line.strip():
        continue
    job = list(map(int,line.strip().split()))
    job.append(job[0]-job[1]) #job[0] is weight, job[1] is length
    job.append(job[0]/job[1])
    schedule.append(job)

scheduleA = copy.deepcopy(schedule)
scheduleB = copy.deepcopy(schedule)
scheduleA.sort(key = lambda x: (x[2],x[0]),reverse=True) #Sort first by diff then weight
scheduleB.sort(key = lambda x: (x[3],x[0]),reverse=True) #Sort first by ratio then weight

def sum_wt_ct(schedule):
    ct = 0
    sum_wt_ct = 0

    for job in schedule:
        ct += job[1]
        wt_ct = job[0] * ct
        sum_wt_ct += wt_ct

    return sum_wt_ct

print(sum_wt_ct(scheduleA)) # 69119377652 for diff
print(sum_wt_ct(scheduleB)) # 67311454237 for ratio
