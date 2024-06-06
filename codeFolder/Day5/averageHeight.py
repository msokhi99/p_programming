'''
Average Height.
'''

studentHeights=input().split()
print(type(studentHeights))
print(studentHeights)
sum=0
count=0
studentHeights=[int(students) for students in studentHeights]
for x in studentHeights:
    sum=sum+x
    count=count+1
print(f"Total Height: {sum}\nNumber of students: {count}\nAverage Height: {round((sum/count))}")