mark = []
totMark = 0
print(end="Enter Number of course: ")
totSub = int(input())

print(end="Enter Marks Obtained in " + str(totSub) + " courses: ")
for i in range(totSub):
    mark.insert(i, int(input()))
	
print(end="Enter Maximum Mark: ")
maxMark = int(input())

for i in range(totSub):
    totMark = totMark + mark[i]
avg = totMark/totSub
perc = (totMark/(totSub*maxMark))*100

print("Average Mark = " + str(avg))
print("Percentage Mark = " + str(perc) + "%")
