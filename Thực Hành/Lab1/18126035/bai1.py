import math
import random

#arr = [random.randint(0, 50) for r in range(10)]   # tạo random 10  số nguyên từ 0 ->50 ( maybe)
#print ( arr)
list = [1,1.5,2.8,3.5,2,7.4,3,7.8,-5]
print('list = ',list) 


print ('min=', min(list))
print ('max = ', max(list))

# tìm average 
average = sum(list) / len(list)    
print ('average = ', average)
print(list)

#check số nguyên 
count = 0
for i in list:
    k = math.ceil(i)   #làm tròn số float -> int ( ko bé hơn i) 3.6 ->4 ( ko bé hơn 3.6)
    if i % k == 0: 
        count+= 1
        print (i, "la so nguyen")
print("so nguyen trong list: ", count)

#   use sorted(list, reverse = True or False or None)
## True, None: ascending sort
## False: descending sort
## remember capitaline( nhớ Viết Hoa chữ T và F trong True False, tui đã mất 1 ngày trời ko hiểu tại sao bị bug á@@)


check = sorted(list)
print('check = ',check)
#check ascending sort:
print('Ascending list: ?')
if check == list:
    print ("true")
else:
    print("false")

#check descending sort
check = sorted(list,reverse = False)
print('Desscending list: ?')
if check == list:
    print('true')
else:
    print('false')




