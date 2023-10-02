list1 = [55,66,22,11,88,77,99,33,44]
num = eval(input("Enter the number what you want："))
list1_index = -1              #Use the record the subscript of the number to found
# Use circular linear lookup  
for i in range(len(list1)):
    if num == list1[i]:
        list1_index = i
        break
if list1_index == -1:
    print("The number you are looking for is not in the list！")
else:
    print("{}the record the subscript of the number：{}.".format(num,list1_index))
# Use circular linear lookup  
