#Binary_Search
import random
list1 = []
# Use a loop to generate a list of non-repeating elements
for i in range(20):
    #rand_num = random.randint(1,101)          
    #list1.append(rand_num)                     
    rand_num = random.randint(1,101)
    while rand_num in list1:                 
        rand_num = random.randint(1,101)
    list1.append(rand_num)

#sortrows
list1.sort()
print(list1)

#find
num = int(input("Enter the number what you want："))
num_index = -1
low = 0                 # The subscript of the minimum (lowest boundary)
high = len(list1) - 1   #The subscript of the maximum value (maximum boundary)
while high >= low:
    mid = (low+high) // 2
    #1.If the key is smaller than the middle element, just continue looking for the key in the first half of the list.
    #2.If the key is equal to the intermediate element, the match is successful.  The search is complete.
    #3.If the key is larger than the middle element, just continue to look for the key in the second half of the list.
    if num<list1[mid]:
        high = mid-1
    elif num == list1[mid]:
        num_index = mid
        break
    else:
        low = mid + 1
if num_index != -1:
    print("{}the record the subscript of the number：{}.".format(num,num_index))
else:
    print("The number you are looking for is not in the list！")
 