# Enter your code here. Read input from STDIN. Print output to STDOUT

def containsAll(str, set):
    if len(str) != len(set):
        return False
    return 0 not in [c in str for c in set]

n = int(raw_input().strip())
lists = []
lengthL = []

for i in range(0,n):
    num = raw_input().strip()
    if len(lists) == 0:
        l1 = []
        l1.append(num)
        lists.append(l1)
        continue
    inserted = False
    duplicate = False
    for j in range(0,len(lists)):
        if inserted == True or duplicate == True:
            break
        for x in range(0,len(lists[j])):
            if num in lists[j]:
                duplicate = True
                break
            if containsAll(lists[j][x],num) and containsAll(num,lists[j][x]):
                lists[j].append(num)
                inserted = True
                break
    if inserted == False and duplicate == False:
        l1 = []
        l1.append(num)
        lists.append(l1)
    inserted = False
    duplicate = False
index = []
print len(lists)
for i in range(0,len(lists)):
    index.append(len(lists[i]))
max = 0
for i in range(0,len(index)):
    if index[i]>max:
        max = index[i]
finalList = []
for i in lists:
    if len(i) == max:
        intL =  map(int, i)
        intL.sort()
        intL.reverse()
        finalList.append(map(str,intL))
finalList.sort(key=lambda x: x[0])
for i in finalList:
    for j in i:
        print j,
    print 
    