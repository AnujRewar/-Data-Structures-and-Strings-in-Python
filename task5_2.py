#creating a list from 1 to 10 and extracting first five elements out of it
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[0:5]

print(list2)             #storing first 5 elements in another list

print(list2[::-1])

list2.reverse()
print(list2)           #printing reversed list and will chante originale list 