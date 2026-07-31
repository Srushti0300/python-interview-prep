list = [35,44,10,3,4,22,17]
print(list)
print(type(list))
print(len(list))
print(list[0])

#list slicing
print(list[1:4])

#append
list.append(90)  #adds one element at the end
print(list)

#sort
list.sort()  #sorts in ascending order
print(list) 

list.sort(reverse=True)  #sorts in descending order
print(list)

list.reverse()   #reverse list
print(list)

list.insert(1,50) #insert a new elements
print(list)

list.remove(10)  #removes an element
print(list)

list.pop(3)
print(list)