#Linear and Binary Search
num_list=[3,2,8,12,11,15,22,17,25,55,33]
target=100
def linearsearch(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return list[i]
            
    return -1 #return "Couldn't find value"
    
result=linearsearch(num_list,target)
print(result)

#Best Case Run Time-O(1)
#length of list--n
#Worst/Average Case--O(n)

  


     
