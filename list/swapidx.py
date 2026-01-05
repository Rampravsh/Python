n=int(input("Enter the number of elements in the list: "))
list1=[]
for i in range(n):
    list1.append(int(input("Enter the element: ")))
print("Original list is:",list1)
idx1=int(input("Enter the index of first element to be swapped: "))
idx2=int(input("Enter the index of second element to be swapped: "))
list1[idx1],list1[idx2]=list1[idx2],list1[idx1]
print("List after swapping elements at indices",idx1,"and",idx2,"is:",list1)