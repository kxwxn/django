myvar = 10
mylist =[100,200,300,400,500]

print(mylist[0])
print(mylist[0:3])

mylist.append(myvar)
print(mylist)

mylist.insert(1,myvar)
print(mylist)


item_removed = mylist.pop()
print(item_removed)
print(mylist)

mylist.reverse()
print(mylist)

random_list = [3,25,12,5,3,12,3,54,6,45,34,2,1,34,]
print("Random list: ",random_list)
random_list.sort()
print("Sorted list: ",random_list)