student = [" om " , 67.7 ,18 ,"west bengal"]
print(student[0:3])
student[0:3] = "sudu"
print(student)

list = [2,3,4]
list.append(5)
print(list)

list2 = [8,4,5,6,2,3,7]
print(list2.sort())
print (list2)

tup = (2,4,5,6)
print(tup.index(5))

list1 = [" 1,2,3,2,1"]
list2 = [" 1,2,3,4,5"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palendron")
else:
    print("no palo")