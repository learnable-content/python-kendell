#Linear Search
def linear(list,target):
  for i in range(len(list)):
      if list[i]==target:
         return list[i]
  
  return -1 #(or print an error that says "item not found in list")

result1=linear([1,5,8.2,3,16,22,19,58,44,37], 22)
result2=linear([1,5,8.2,3,16,22,19,58,44,37], 45)
result3=linear (["soccer","basketball", "football", "baseball", "hockey", "rugby", "frisbee"], "baseball")
print(result1+"\n")
print(result2+"\n")

#Binary Search
def binary(list, target):
   start=0
   end=len(list)-1
   while start<end:
     mid=(start+end)/2
     if list[mid]==target:
        return target
     elif list[mid]>target:
        end=mid-1
     else:
        start=mid+1
   return -1
        
result4=binary([ 1, 7, 44, 45, 46, 58, 67, 99, 145], 67)
print(result4+"\n")
  


     
